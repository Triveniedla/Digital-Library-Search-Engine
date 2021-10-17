# Digital Library Search Engine for Electronic Thesis and Dissertation

In this project, a website is designed which provides a digital library search engine for electronic thesis and dissertation (ETD). The Django framework is used to build the website. Django is a high-level python web framework that enables rapid development of the secure and maintainable website and uses model-template-view architecture pattern. The technologies used in this project: Django framework, Elasticsearch, JavaScript, MYSQL, Bootstrap, HTML5, Kibana, and CSS.

Demo for the developed website: [https://youtu.be/U9EiKMsV6Yk](https://youtu.be/U9EiKMsV6Yk)

Install mysql and other dependies

```
sudo apt-get install mysql-server
```

Start mysql server in the github repo.
Create database and import tables;

'''
sudo mysql -u root -p
create user 'admin'@'localhost' identified by 'monarchs';
CREATE DATABASE tedlaweb default character set 'utf8';
use tedlaweb;
source tedlawebfinal.sql;
grant all privileges on tedlaweb to 'admin'@'localhost';
flush privileges;
'''

Install following dependencies before installing the requirements for 
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential


