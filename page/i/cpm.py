'''
Represent the cPanel Manager page
'''

from page.page import Page
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException
import re
import time

elements = {
    'bluehost': {
        'expected_title': (
            ' Manager'
        ),
        'tasks': ('css', '.task_error li'),
        'toggle_expand_cpflag': ('css', '#indicator_cpflag'),
        'toggle_expand_custflag': ('css', '#indicator_custflag'),
        'v_flag': ('css', '#custflag_v'),
        'update_button': ('css', 'input[value="Update"]'),
        'wait_element': ('css', '#fraud_content'),
    },
    'fastdomain': {
    },
    'hostmonster': {
    },
    'justhost': {
    },
}


class SignupFailure(RuntimeError):
    '''
    Signup didn't complete in time.
    '''
    pass


class CPM(Page):
    '''
    cPanel Manager page object
    '''
    def __init__(self, config):
        super(CPM, self).__init__(config)
        self.expected_title = elements[self.config.brand]['expected_title']
        self.elements = elements[self.config.brand]
        self.is_the_current_page()

    def get_tasks(self):
        '''
        Parse and return information about the current tasks for an account
        '''
        tasks = []
        statuses = {
            'Running for': 'running',
            'Scheduled in': 'scheduled',
            'Re-Scheduled in': 'failed',
            'Backlog SuperCHOKED for': 'choked',
            'Re-Backlog SuperCHOKED for': 'choked',
            'Sleeping for': 'sleeping',
            'Paused': 'paused',
        }
        try:
            task_elements = self.selenium.find_elements(
                *self.elements['tasks']
            )
        except NoSuchElementException:
            # We didn't find any tasks to add
            return tasks
        for task_element in task_elements:
            # YYYY-MM-DD hh:mm:ss #9999 #/# Doing thingy (Module_Action)
            # - Error Stuck for/To run in: 99 minutes and 99 seconds
            task_lines = task_element.text
            task = {}
            try:
                info_line, status_line = task_lines.split('\n')
            except ValueError:
                info_line = task_lines
                status_line = ''
            (task['date'],
                task['time'],
                task['id'],
                step_info,
                task['message']
             ) = info_line.split(None, 4)
            task['step'], task['total_steps'] = step_info.split('/')
            task['id'] = task['id'][1:]
            task['type'] = re.findall(r'\w+_\w*', task['message'])[0]
            if status_line:
                status_line = status_line.split(': ')[0]
                try:
                    task['status'] = statuses[status_line]
                except KeyError:
                    raise KeyError('Found unknown status: ' + status_line)
            else:
                task['status'] = 'completed'
            tasks.append(task)
        if self.config.debug:
            print(tasks)
        return tasks

    def is_signup_finished(self):
        '''
        Return true if the tasks on the page indicate that the account has
        finished the signup process.  Otherwise, return false.
        '''
        tasks = self.get_tasks()
        for task in tasks:
            if task['status'] == 'completed':
                continue
            if task['type'] != 'Signup_WaitingForVerification':
                if task['type'].startswith('Signup_'):
                    return 0
        return 1

    def wait_for_signup(self):
        '''
        Refresh and check the page until the signup completes.
        '''
        reload_interval = 20
        max_attempts = 20
        current_attempt = 1
        url = self.selenium.current_url
        while not self.is_signup_finished():
            time.sleep(reload_interval)
            self.selenium.get(url)
            self.validate()
            if current_attempt >= max_attempts:
                raise SignupFailure('Signup did not complete: '
                                    '%s checks made, %s seconds apart'.format(
                                    max_attempts, reload_interval))
        return self

    def hide_inactive_custflags(self):
        '''
        Expand the customer flags section.
        '''
        toggle = self.selenium.find_element(
            *self.elements['toggle_expand_custflag']
        )
        if self.custflags_expanded():
            toggle.click()
        return self

    def show_all_custflags(self):
        '''
        Expand the customer flags section.
        '''
        toggle = self.selenium.find_element(
            *self.elements['toggle_expand_custflag']
        )
        if not self.custflags_expanded():
            toggle.click()
        return self

    def custflags_expanded(self):
        '''
        Return whether the custflags section is expanded on this page.
        '''
        toggle = self.selenium.find_element(
            *self.elements['toggle_expand_custflag']
        )
        classes = toggle.get_attribute('class').split()
        return 'none' not in classes

    def flag_active(self, flag):
        '''
        Set a given flag.
        '''
        checkbox = self.selenium.find_element(
            *self.elements[flag + '_flag']
        )
        return checkbox.is_selected()

    def save(self):
        '''
        Save changes made in this page.
        '''
        update_button = self.selenium.find_element(
            *self.elements['update_button']
        )
        update_button.click()
        return self

    def set_flag(self, flag):
        '''
        Return whether the flag is set.
        '''
        checkbox = self.selenium.find_element(
            *self.elements[flag + '_flag']
        )
        if not self.flag_active(flag):
            checkbox.click()
        return self

    def verify_account(self):
        '''
        Mark the account as verified.
        '''
        self.show_all_custflags()
        self.set_flag('v')
        self.save()
