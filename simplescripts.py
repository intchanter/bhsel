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
        if (self.selenium.find_elements_by_link_text('My Installs')) or (self.selenium.find_elements_by_link_text('One-Click Installs')):
            print ("Wow Simple scripts actually worked\n")
        else:
            self.selenium.refresh();
            time.sleep(10);

            if (self.selenium.find_elements_by_link_text('My Installs')) or (self.selenium.find_elements_by_link_text('One-Click Installs')):
                print ("Wow simple script worked on try 2\n")
        
            else:
                self.selenium.refresh()
                time.sleep (10)

                #$driver->accept_alert
                if (self.selenium.find_elements_by_link_text("My Installs")) or (self.selenium.find_elements_by_link_text('One-Click Installs')):
                    print ("Wow Simple scripts worked on try 3\n")
            
                else:
                    raise Exception ("Simple Script didn't load after 3 attempts.\n")
                        
        return;

    def wait_for_element(self):
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_css_selector('.footerA'))
    
    def install_script(self, name, tries, domain):
        timer = 5
        try:
            tries
        except NameError:
            tries = timer
            
        if self.selenium.find_elements_by_link_text("Got it! Don't show this again"):
            self.selenium.find_element_by_link_text("Got it! Don't show this again").click()
        #my $domain_field = $selenium->find_element(@{$map->{'new_domain_field'}});
        time.sleep(10)
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_link_text('One-Click Installs')).click()
        #wait_for_element = WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_css_selector('.footerA'))
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_link_text(name)).click()
        time.sleep(3)
        self.selenium.find_element_by_link_text('Start').click()
        time.sleep(3)
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_id('install_dir')).clear()
        self.selenium.find_element_by_id('install_dir').send_keys(name);
        self.selenium.find_element_by_css_selector('button.btn.btn-primary.script-install-action').click()
        time.sleep(40)
        if (self.selenium.find_elements_by_id('data[Script][overwrite]')):
            self.selenium.find_element_by_id('data[Script][overwrite]').click()
            self.selenium.find_element_by_css_selector('button.btn.btn-primary.script-install-action').click()
        WebDriverWait(self.selenium, 30).until(lambda d : d.find_element_by_css_selector('input.install-domain-advanced.show-hide')).click()
        time.sleep(5)
        WebDriverWait(self.selenium, 40).until(lambda d : d.find_element_by_name('data[Script][ss_tags][ss_admin_pass]')).clear()
        self.selenium.find_element_by_name('data[Script][ss_tags][ss_admin_pass]').send_keys('Test1234')
        self.selenium.find_element_by_id('license_box').click()
        #self.wait_for_element()
        time.sleep(3)
        self.selenium.find_element_by_id('install_button').click()
        time.sleep(3)
        #self.wait_for_element()
        #if (self.selenium.find_elements_by_id('data[Script][overwrite]')):
        #   self.selenium.find_element_by_id('data[Script][overwrite]').click()
        #   self.selenium.find_element_by_css_selector('button.btn.btn-primary.script-install-action').click()
            #self.wait_for_element()
        
        self.selenium.find_element_by_link_text('One-Click Installs').click()
        time.sleep(5)
        self.selenium.find_element_by_link_text('View Progress').click()
        
        #self.wait_for_element()
        time.sleep(5)
        print (self.selenium.find_element_by_css_selector( '.status_count_text').text)
        while ((self.selenium.find_element_by_css_selector('.status_count_text').text == 'Running the installation on your server.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Queued for processing - preparing for install.')
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Preparing to install script.')
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Building configuration.')
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Extracted files for installation.')
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Uploading script package.')
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Starting the installation.')  
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Starting the removal process.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Acquiring the file structure.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Uploading script package.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Removing the files from http://' + domain + '/NoahsClassifieds/.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Removing the files from http://' + domain + '/' + name + '/.') 
               or (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Something went wrong with the installation of this application. Running cleanup.')):
            print ("Waiting on install\n")
            time.sleep(5);
    
        print (self.selenium.find_element_by_css_selector( '.status_count_text').text)
        if ( (self.selenium.find_element_by_css_selector('.status_count_text').text == 'Unfortunately something went wrong. We cannot upload files to your server with the FTP credentials provided. In order to proceed please confirm that there are no ongoing FTP issues with your host and that the credentials supplied are valid')
            or (self.selenium.find_element_by_css_selector( '.status_count_text').text == 'Unfortunately something went wrong. We cannot reach the installation domain to run necessary processes. Since we made it this far this likely indicates a disconnect between where we are uploading the files and where the domain is currently routing caused by DNS issues or restricted access caused by a .htaccess file on your account. This could also indicate a failure in a required procedure which we must run before we can continue. If your name servers have recently been updated you may need to wait few hours and try this again.')
            or (self.selenium.find_element_by_css_selector( '.status_count_text').text == 'Unfortunately something went wrong. While attempting to step through the normal user procedures required to complete your request something went wrong. This typically means we ran in to an unforeseen event in the process which caused the process to fail in order to avoid delivering an incomplete or damaged application post process.')):
            #$selenium->find_element('a.fakebutton', 'css')->click;
            #self.wait_for_element()
            time.sleep(3)
            tries = tries - 1
            if (tries <= 0 ):
                raise Exception ("\nWe Tried to install $script 5 Times and failed please restart script\n")
        
            else:
                print ("\n " + name + "failed Should be retrying "+ str(tries) +" Remaining\n")
                self.install_script(name,tries,domain)
        
    
        else:
            print (self.selenium.find_element_by_css_selector( '.status_count_text',).text)
            print (name + " Installed\n")
    