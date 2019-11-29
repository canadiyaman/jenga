# jenga_bookapp
> WARNING: This document tested only on MacOS High Sierra and Ubuntu 18.

> You can test it on live! [Click here.](http://jenga-env.pmpg82nvv4.eu-west-3.elasticbeanstalk.com)


## Manuel Setup

1. **Install project with the following command to your computer.**

	$ `git clone https://github.com/canadiyaman/jenga_bookapp.git`
2. **Install virtualenv to your computer(https://virtualenvwrapper.readthedocs.io/en/latest/install.html).**

    $ `pip install virtualenvwrapper`
    
    $ `export WORKON_HOME=$HOME/.virtualenvs`
    
    $ `export PROJECT_HOME=$HOME/Devel`
    
    $ `source /usr/local/bin/virtualenvwrapper.sh`
 3. **Install requirements for the project.**
 
    $ `pip install -r requirements.txt`
 4. **Create .env file for your local settings and configure .env file.**
 
    $ `cp .env-example .env`
 5. **Create Database on terminal (or you can create with PgAdmin3~4 It's up to you)**
 	 * If you get psql: could not connect to server: error
	 
 	   $ `sudo chown -R postgres:postgres /var/lib/postgresql/9.6`
	   
	   $ `sudo chmod -R u=rwX,go= /var/lib/postgresql/9.6`
	  
	 * Now you can continue create database
	 
	   $ `psql postgres`
    
    `postgres=# create role {database_user} with password '{database_password}';`
    
    `postgres=# alter role {username} createrole superuser;`
    
    `postgres=# alter role {username} createrole login;`
    
    `postgres=# create database {database_name};`
    
    `postgres=# grant all privileges on database {database_name} to {database_user};`
    
    `postgres=# \q`
 6. **Make Migration if everythings is good until now.**
 
    $ `python manage.py migrate`
 7. **Run server**
 
	 $ `python manage.py runserver`

 ### It's done! Now you can visit site (http://127.0.0.1:8000)
 
# Deployment on AWS EC

> First you must create an aws account and set trier Elastic Beanstalk server.
> [You can find more information in this link.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

> Create postresql database.
> [How to configure Postgresql on Elastic Beanstalk](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)

**Install project to your computer and move to main directory of project**

 1. **Connect your elastic beanstalk server with ssh.** [About ssh settings](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-ssh.html)
 
	 $ `eb ssh`
	
2. **Create .env file use with .env-example file.**

	$ `cp .env-example .env`
	$ `nano .env`
3. **Your .env must be like below. Fill with your settings save and exit(CTRL+X).**

	  ```
	  THEME=blue
	  CACHE_TIME_TYPE_MINUTES=1
	  DATABASE_NAME=ebdb
	  DATABASE_USER=
	  PASSWORD=
	  DATABASE_HOST=
	  DATABASE_PORT=5432
	  ```
4. **Go back to local directory**

	$ `exit`
5. **Deploy project.**

    $ `eb deploy`
    
    
    
## About Jenga Bookapp
This project created by Can ADIYAMAN. 
You can use it what every you want.
