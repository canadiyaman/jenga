
# jenga_bookapp

# Installment (Manuel)
 * Get project your computer
 
 
    $ git clone https://github.com/canadiyaman/jenga_bookapp.git
    
 * Install Virtualenv to your computer. (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
 
    
    $ pip install virtualenvwrapper
    $ export WORKON_HOME=$HOME/.virtualenvs
    $ export PROJECT_HOME=$HOME/Devel
    $ source /usr/local/bin/virtualenvwrapper.sh
    
 * Install requirements for the project
 
    
    $ pip install -r requirements.txt
    
 * Create .env file for your local settings.
 
 
    $ cp .env-example .env
    
 * Make Migration if everythings is good until now.
 
 
    $ python manage.py migrate

 * It's done! Start server with this command and visit site (http://127.0.0.1:8000)
 
   
    $ python manage.py runserver
    

# Deployment on AWS EC

 * Get Access and Secret Key
    * Log in to your AWS Management Console.
    * Click on your user name at the top right of the page.
    * Click on the Security Credentials link from the drop-down menu.
    * Find the Access Credentials section, and copy the latest Access Key ID.
    * Click on the Show link in the same row, and copy the Secret Access Key.
    * Run this command in project root directory
    
    
    $ eb deploy
    
    
    
## About Jenga Bookapp

This project created by Can ADIYAMAN. 
You can use it what every you want.