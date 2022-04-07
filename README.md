# DogGenerator

create git repository
create instances
create firewall rules
git clone repository in instance-1 vscode
SSH setup for instance-1 and installed docker, ansible and python
create ansible folder
create roles folder in ansible and use code "ansible-galaxy init *docker*" to create roles file structure with:
- docker 
- docker-compose
- jenkins
- nginx
- python
- swarm-manager
- swarm-worker

edited playbook.yml and inventory.yml
edited main.yml in tasks folder of every folder in roles
create new user and add it to visudo. Add instance-1 ssh to authorized_keys

installed jenkins and created a new item as a pipeline project


SSH
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMZ05IvEvkHYtkwvE6u973hQW56HfBJ8b8SbWjkQTwb+xMolf92b4sUcLr0OMVn6Rkuz9tvmG2vtkb2iGJeoJqMsGjKs9GXzblsGcQbjFzVm+HRyAjhW6eSV+CrGB4TqY5hWxsOzaX5cEA7jo3FrpxueQ3r3BOE2KDBZMrQ1NPMjl2taSTHNUqqTNFXzeCSxgU+BESaEPYUl/3br4heW5ie4FpQzPG5QwGuX+acO+mY8lxu7AX7Hv/r2Kz827bI529f436gVAQgT+jaHQb9XUdVk/K3TiMn7P7e/zCpV6ocVW/oi6UPWFDZAqzl2x/wVbEiGJZfzN+FoRfCpZoyKKt5BcZteKv+Ni99rNe+BDQdfTTX8Kqd5eoHr73p5wADtUwOg0x5TwBqWpMO9Ef5ZU4Fb5DX70qX5/C/arR+mS7TI400pxjCWIg6YDGcRWq7SsXEdSErW7g2qpCY88BEEejxR0CcKGVXL8+8r2H6QuS8g1na8gDRxspCNUCgOL0JG9y/TZP7MgmrKA/ecTqUMX/KHxLG+uEhDfLHMQSesB+5AuOabMGqqR1WSW6Sy0XWY8jbXBcQEQo7ai4B7uKqXFbwAFQ40TPYnEwNg9fhuowOTADN+1lsGi0HeJkpVzZKtTHmwKdC7bhaer6x4Ln3lCqdtedk1yLydYcNR7PxLsAzw== fiercepc@Michelle-Gaming-PC


ssh for instance-1
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDbZg0cIdHtT8zirMwLAQWXSm1V+aTFsONj04QlUeTWseUdDmUzborMKwr0lnmBsMLSPna/pgcGOGRgQHDfoyyJBMi0H3QCQKE7RBLd1UiRl5ciVapITObG3VWna/fmy6EX7vFlZwcLQ2G14ww8RiRsg3s6mylDrE4KGMxZuEw7cPzs6Mttbz+lS9tDl13fAvIe6iBoiGSSfy/FSkrNB9y6BnaMqyg0nAIflngt94+za/I1F0G0sEzRHK2/qjnEnHg872qZ7uCYkhTZMuaA7CQlvtu9O9uy9Sy5guxBVxFeSL52yV9XgdKEo95zLde3WTwd88kgPJ8U/47ePFx1noQub9B5gKqTV+szN45b90Mwbv+Y/BDa+QrGgflG5NSpLI2HkYjfVMRtseoc2lA0Juxdz9PvMQ6WOYOJSUtqVW6A1IEu7ldzwMMnQkrZNrUAX9/QRDSnUTWfBW2Y8xWQXxUUP07qW55F8XXIHS1r8E2JsY0moxYXnve06nV7sEGpHIk= smellyshelly269@instance-1

jenkins password: cacd2488ab8b407aa789b3b7bd0c4283
jenkins link: http://35.197.254.246:8080/




# DogGenerator

## Table of Contents:
* [Project Brief](#Project-Brief)
* [Entity Relationship Diagram](#ERD)
* [CI Pipeline](#ci-pipeline)
    * [Project Tracking - Jira](#project-tracking)
    * [Version Control - Git](#version-control)
    * [Build Server - Jenkins](#build-server)
* [SQL](#sql)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
    * [Unit Testing](#Unit-Testing)
    * [Integration Testing](#Integration-Testing)
* [The Application](#The-Application)
    * [Create](#create)
    * [Read](#read)
    * [Update](#update)
    * [Delete](#delete)
* [Known Issues](#known-issues)
* [Improvements for the future](#future-workimprovements)


## Project Brief
The project brief was to create a service orientated architecture for an application that involves the concepts:
- Software Development with Python
- Continuous Integration
- Cloud Fundamentals


To complete the above, I would need to do:
- Kanban Board: Asana or an equivalent Kanban Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX

The aim was to create an application that 
The framework for my project can be seen below:

![framework](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/framework.PNG) 


## ERD
The Entity relationship diagram helped me plan out the tables I was to create in my database and outline the relationships between them. This was then helpful when creating the database tables in MySQL Workbench , assigning primary and foreign keys and also knowing what columns each table consisted of.  
The screenshot below shows the ERD I created for my Candy shop application.

![ERD](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/ERD.PNG)

As seen in the ERD, I have created three tables: item, purchase and user. 
The user table will consist of the fields: username, email and address.
The item table will consist of the fields: item_name, price, description and quantity.
The purchase table will consist of the fields: fk_user_id and fk_item_id. 
For each field, I have given it a data type of either int, varchar or dec and written NOT NULL so that the fields can't be left empty.
The user table has a one to many relationship with item and purchase. 
The purchase table has a one to many relationship with item.

## CI Pipeline
The CI Pipeline consists of: project tracking, version control, development environment and build server. Below is the diagram of my complete CI Pipeline. 

![CI Pipeline](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/CI.PNG)

### Project Tracking
To track and manage my project, I used Jira. I had to create user stories of everything that would be needed in my project and put them under Epics. I created four epics: planning, database, coding in Python using Flask and Testing. All the user stories are stored in the product backlog and were moved to each sprint when they needed to be completed.
I created sprints and put individual deadlines so that i can manage my time better and make sure to get the entire project done on time. Once a sprint was complete, I would create a new one with the user stories that need to be completed next. 

The picture below shows the Jira roadmap.

![Jira Roadmap](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Roadmap.PNG)

The picture below shows the Jira Board.

![Jira Board](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Jira%20Board.PNG)  

The entire Jira board can be found here: https://michelle548129.atlassian.net/jira/software/projects/CS/boards/3

My burndown chart is shown below:

![Burndownn chart](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Burndown%20chart.PNG)

### Version Control
I used Git for my Version Control. I created a new repositiory on GitHub for this project. The repo can be found here: https://github.com/michelle548129/TheImpossibleQuiz.git
I used Git so that I could continually commit my work there and be able to pull previous versions if needed. This came in handy when the code stopped working due to an error, so the previous code could be pulled from git.
I created a dev branch so that new code could be written and run there first. Once it was working and fully functional, it was pushed onto the main. This prevented me from only using main and having a bunch of errors that prevented my application from running. Anything that was pushed onto main was working at all times. The dev branch was essentially my 'testing' branch where I could figure out how to implement different functions.

The network diagram below shows all the commits made and the main and dev branch. As you can see, I was mainly working on the dev branch and commiting there, then when the code worked, I pushed it onto main. 

![Image showing the network diagram](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Network%20graph.PNG)
 

### Build Server
For my build server, I used Jenkins which allowed my project to be built and tested automatically. First, I created a new firewall rule on Google Cloud Platform. I then created a new instance and used the external IP address to run Jenkins on my broswer. I had to initiate an SSH connection to the VM and get the Admin password through there so that I could get through to Jenkins, make an account and create a freestyle project.

![Creating firewall rule](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/firewall.PNG)
![Creating Jenkins instance](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/jenkins%20instance.PNG)
![Initiating SSH connection to VM](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/ssh%20to%20vm.PNG)
![Getting Admin password for Jenkins](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/adminpassword.PNG)
![Creating Jenkins freestyle project](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/jenkins.PNG)
![Execute shell](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/executeshell.PNG)


## SQL
I created my database on MySQL Workbench. Below is the SQL code I used to create my three tables that I created on my ERD earlier. It shows the item, user and purchase tables with all the fields shown on the ERD created within them. They are then joined together using Foreign keys. 

![SQL code](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/SQL%20code.PNG)

Here is a screenshot of the item table I created:

![Item table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemtable.PNG)


## Risk Assessment
I created a risk assessment for possible hazards that can occur and how I could overcome them. It's important to analyse these situations and be prepared for them as well as have a plan for them so that when a hazard occurs, it can be easily overcome. It's also helpful to think of ways to prevent these hazards in advance to minimise the risk of them occuring. 
As you can see, when the control and response measures are put into place, the likelihood of these hazards occuring or the affect they'll have will drastically descrease. 

![Image showing the Risk Assessment Table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Risk%20Assessment.PNG)


## Testing
After creating the application, I had to test it to make sure that everything was working and was fully functional. This would prevent errors being thrown to the user later down the line when the application is being used. The tests were made to check:
- whether the application was running
- whether data was being stored in the database correctly
- user input validation
- whether the CRUD functions were implemented correctly

![test.sh](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/testsh.PNG)
 
Both unit testing and integration testing is needed to ensure that everything was running smoothly. Unit testing tested the CRUD functionality of my application. Integration testing tested the forms by ensuring that they were working when iputs were made.


## The Application
The main objective in this project was to create an application that fulfils the CRUD functionality. Below I will discuss how I've implemented the CRUD functions to my project.
 
### Create:
#### CREATE used for user:
I have implemented 2 CREATE functions in my application. 
The first is to register a user. In the application, the user is able to register with their details through a form and the data is automatically stored in the 'user' table in the SQL database. 
![Register form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/createwebpage.PNG)
![User Input for registering](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/addusercreate.PNG)
![User Table](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/usertable.PNG)
As you can see, when the user enters their details to register, the 'user' table in the MySQL database adds the data there.

#### CREATE used for item:
The same function is done for the 'item' table.
![Add item form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/additemform.PNG)
![Adding in new item](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/newitemadded.PNG)
![New item in list](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemlistupdated.PNG)
As you can see, here, the admin of the shop is able to add new items to the shop. When the item has been added, it is added to the 'item' table and list of items on the website is also updated, containing the newly put item.


### Read:
I have included the READ function so that the list of items is displayed on the shop. This enables users to see what candy bars the shop has to be bought. The list is read from the 'item' table created on the MySQL database, hence any data in that table will be displayed on the website.

![List of items](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/itemlistupdated.PNG)

I have also created a drop down function so that the data in both the user adn item tables are displayed. If the user wants to make an order, they need to select the name of the customer and the product they would like to buy.

![Drop down function](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/dropdown.PNG)


### Update:
For the UPDATE functionality, I have implemented it so that the user is able to update the quantity of the candy available. This lets them change the stock if needed. This change also update the data in the item table.

![Update quatity form](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updateform.PNG)
![Quantity updated](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updating.PNG)


### Delete:
I have implemented the DELETE function by allowing the user to delete an item if they need to. This can be if the candy is no longer is stock or if it'll no longer be sold. Like with all the other CRUD functions, deleting an item form the website will also delete the item form the MySQL database. 

![Deleting Review](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/updateform.PNG)
![Deleting Review](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/deleted.PNG)



## Known Issues

![Testing report](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/testreport.PNG)

As shown above, I ran into errors when trying to run tests as they weren't working. This is something I had trouble completing as I was on a tight deadline too. With more time, I would've been able to create working tests so that the coverage reports would've displayed 100%. 

![Jenkins build failed](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/jenkins%20error.PNG)

As shown in the screenshot above, I also couldn't get my Jenkins to build successfully, again because the testing was flawed. This can be fixed with more time by creating working tests.



## Future Work/Improvements
Future improvements would be to work on the aesthetics of the application. For this project, my main focus was ensuring the application was fully functional and getting CRUD implemented which took up the majority of the time. In the future, I would add CSS to make the websit elook more appealing.

I would also want to fix the issues talked about in known issues so that the testing side of the project is complete. Despite knowing the website is functional due to manual testing, automated testing would be much easier to spot mistakes and errors that wouldn't be caught otherwise until used by a user. 

I would also like to implement a login function that separates both the admin(shop owner) of the website from the users(customers). Right now, the users are able to go onto the admin section and add new items and delete them etc. I would implement a login function so that it's only accessible to the admin and the users are only able to make a purchase.