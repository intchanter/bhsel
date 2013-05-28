import time
from selenium.webdriver.support.ui import WebDriverWait

class SS():
    
    def __init__(self, selenium):
        self.selenium = selenium
    
    def get_to_simplescripts(self):
        #my $selenium = $self->{'selenium'};
        #$self->find_element('cPanel', 'link')->click;
        #Readonly my $SLEEP => 20;
        #sleep $SLEEP;
        #my $handles = $self->get_window_handles;
        #$self->switch_to_window($handles->[1]);

        # print Dumper($handles);
        #my $phpv = '53s';
        #print "Changing php version to 5.3 Single php.ini\n";
        #updatephp($self, $phpv);
        time.sleep(10)
        self.selenium.find_element_by_id('item_simplescripts-sb').click()
        time.sleep (10)
        handles = self.selenium.window_handles
        self.selenium.switch_to_window(handles[2])
        if (self.selenium.find_elements_by_link_text('My Installs')):
            print ("Wow Simple scripts actually worked\n")
        else:
            self.selenium.refresh();
            time.sleep(10);

            if (self.selenium.find_elements_by_link_text('My Installs')):
                print ("Wow simple script worked on try 2\n")
        
            else:
                self.selenium.refresh()
                time.sleep (10)

                #$driver->accept_alert
                if (self.selenium.find_elements('My Installs', 'link')):
                    print ("Wow Simple scripts worked on try 3\n")
            
                else:
                    raise Exception ("Simple Script didn't load after 3 attempts.\n")
                        
        return;

    def install_script(self, name, tries):
        timer = 5
        try:
            tries
        except NameError:
            tries = timer

        #my $domain_field = $selenium->find_element(@{$map->{'new_domain_field'}});
        time.sleep(10)
        wait_for_element = WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_css_selector('.footerA'))
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_link_text(name)).click()
        self.selenium.find_element_by_css_selector('a.link_button > div.submit > input.button').click()
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_id('install_dir')).clear()
        self.selenium.find_element_by_id('install_dir').send_keys(name);
        self.selenium.find_element_by_link_text('Click here to display').click()
        time.sleep(5)
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_name('data[Script][ss_tags][ss_admin_pass]')).clear()
        self.selenium.find_element_by_name('data[Script][ss_tags][ss_admin_pass]').send_keys('Test1234')
        self.selenium.find_element_by_id('license_box').click()
        wait_for_element
        self.selenium.find_element_by_id('install_button').click()
        wait_for_element
        if (self.selenium.find_elements_by_id('ScriptOverwrite')):
            self.selenium.find_element_by_id('ScriptOverwrite').click()
            self.selenium.find_elementby_id('install_button').click()
            wait_for_element
    
        self.selenium.find_element_by_link_text('My Installs').click()
        wait_for_element
        while ((self.selenium.find_element_by_css_selector('.status_count_text').text == 'installing') or (self.selenium.find_element_by_css_selector('.status_count_text',).text == 'queued')  or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'removing') or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'pending')):
            print ("Waiting on install\n")
            time.sleep(5);
    
        print (self.selenium.find_element_by_css_selector( '.status_count_text',).text)
        if (self.selenium.find_element_by_css_selector( '.status_count_text').text == 'error'):
            #$selenium->find_element('a.fakebutton', 'css')->click;
            wait_for_element
            tries = tries - 1
            if (tries <= 0 ):
                raise Exception ("\nWe Tried to install $script 5 Times and failed please restart script\n")
        
            else:
                print ("\n " + name + "failed Should be retrying "+ tries +" Remaining\n")
                self.install_script(name,tries)
        
    
        else:
            print (name + " Installed\n")
    