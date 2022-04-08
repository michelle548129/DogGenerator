# DogGenerator

## Table of Contents:
* [Project Brief](#Project-Brief)
    * [Service 1](#Service-1)
    * [Service 2](#Service-2)
    * [Service 3](#Service-3)
    * [Service 4](#Service-4)
* [Project Tracking](#Project-Tracking)
* [Version Control](#Version-Control)
* [Build Server](#Build-Server)
* [Risk Assessment](#Risk-Assessment)
* [The Application](#The-Application)
    * [Service 1](#Service-1)
    * [Service 2](#Service-2)
    * [Service 3](#Service-3)
    * [Service 4](#Service-4)
* [Rolling Updates](#Rolling-Updates)
* [Testing](#Testing)
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

The aim was to create an application that is made up of 4 services which work together to create a functional application. The 4 services are:
### Service 1
This is the main service that uses Jinja2 templates to allow interaction with the application. This service communicates with services 2,3 and 4 and also stores data in and SQL database container.

### Service 2 & 3
These services create a random object. 

### Service 4
This service creates an object that is based on the random objects generated in Service 2 and 3. 

## Project Tracking
Due to this being a rather complex project, I knew it was common sense to use best practices when it comes to project tracking, and would use a software to help me plan out the tasks as needed. To this end, I decided to use Jira as it is a tool I have used ever since my first project and find it a valuable and trusted tool to help me map out my project and all the issues and to-dos that will no doubt crop up.

I decided to employ the use of a KanBan-style board as it is rather helpful and helps me use the software to its full potential for me. Below is a Sprint in action. I also employed the traditional style of user stories often used as a standard in the industry, as well as stories from a developer perspective.

![As-a-user](https://github.com/michelle548129/DogGenerator/blob/main/As-a-user.PNG)


![As-a-developer](https://github.com/michelle548129/DogGenerator/blob/main/As-a-developer.PNG)


The picture below shows the Jira roadmap with various dates timelines and progress tracking set up.

![Jira Roadmap](https://github.com/michelle548129/DogGenerator/blob/main/Jira%20Roadmap2.PNG)

The picture below shows the Jira Board.

![Jira Board](https://github.com/michelle548129/DogGenerator/blob/main/jira%20board.PNG)  

The entire Jira board can be found here: https://michelle548129.atlassian.net/jira/software/projects/DG/boards/4

My burndown chart is shown below:

![Burndown chart](https://github.com/michelle548129/TheImpossibleQuiz/blob/main/Burndown%20chart.PNG)

## Version Control
For my Version Control, I used Git, which I am very familiar with at this point. I created a new repository, along with all the required webhooks, tokens and integrations needed to ensure the success of the project. My repository can be found at: https://github.com/michelle548129/DogGenerator

I used Git so that I could continuously push my work to a remote repository, where I knew the code would be safe if anything were to happen to my local machine. I also employed the use of a dev branch, and carrying on from my last project and learning from my mistakes, this time I also used an additional "Feature" branch. I found this particularly helpful as I could test out a lot of things on the feature branch that were experimental, and if I resolved bugs I could push them to dev, and if there was a fully working copy I could then merge by creating a pull request to the main branch. This also gave me additional peace of mind were anything to go wrong, as I knew I could revert to a previous commit or pull data down from a more stable branch if, when and as needed.

The network diagram below shows all the commits made and the main,dev and feature branch. As you can see, I was mainly working on the feature branch and commiting there, then when the code worked, I pushed it onto dev then main. At times, I had to push from dev onto main as well in order for me to run the Jenkins pipeline successfully.

![Image showing the network diagram](https://github.com/michelle548129/DogGenerator/blob/main/network%20graph.PNG)
 
![Image showing the network diagram](https://github.com/michelle548129/DogGenerator/blob/main/webhook.PNG)

## Build Server
For my build server, I used Jenkins which allowed my project to be built and tested automatically. First, I created a new firewall rule on Google Cloud Platform. I then created a new instance and used the external IP address to run Jenkins on my broswer. I had to initiate an SSH connection to the VM and get the Admin password through there so that I could get through to Jenkins, make an account and create a freestyle project.

During this project, I once again just used Jenkins as I had become familiar with its uses, and as I learnt more about it I realised how invaluable it was going forward and made sure to familiarize myself with its many features and automation tools it provided. I created new firewall rules via GCP's management ui, and then created a new instance, using the external IP address to run Jenkins on my browser. This entailed the use of an SSH connection to the virtual machine, obtaining the Admin password, installing all the default plugins and then proceeding to create a freestyle project which would allow me the freedom of using my own tools and resources to go ahead with the project.

![Creating firewall rule](https://github.com/michelle548129/DogGenerator/blob/main/Firewall.PNG)
![Creating Jenkins instance](https://github.com/michelle548129/DogGenerator/blob/main/VM%20instances.PNG)
![Initiating SSH connection to VM](https://github.com/michelle548129/DogGenerator/blob/main/ssh%20to%20vm.PNG)
![Getting Admin password for Jenkins](https://github.com/michelle548129/DogGenerator/blob/main/adminpassword.PNG)

Below are some screenshots of the directory and the folders/ files I had created for this project in Visual Studio Code. 

![Creating firewall rule](https://github.com/michelle548129/DogGenerator/blob/main/ansible%20roles.PNG)
![Creating Jenkins instance](https://github.com/michelle548129/DogGenerator/blob/main/Front-end%20service.PNG)
![Initiating SSH connection to VM](https://github.com/michelle548129/DogGenerator/blob/main/important%20application%20files%20and%20docker%20yaml%20etc.PNG)

## Risk Assessment
I created a risk assessment for possible hazards that can occur and how I could overcome them. It's important to analyse these situations and be prepared for them as well as have a plan for them so that when a hazard occurs, it can be easily overcome. It's also helpful to think of ways to prevent these hazards in advance to minimise the risk of them occuring. 
As you can see, when the control and response measures are put into place, the likelihood of these hazards occuring or the affect they'll have will drastically descrease. 

![Image showing the Risk Assessment Table](https://github.com/michelle548129/DogGenerator/blob/main/Risk%20Assessment.PNG)

## The Application
I created a dog generator that tells a user what dog they should get. It prints out the dog breed, what the dog sohuld be called and the characteristic of the dog. It's randomly generated so the user is always printed a different result.  
 
### Service 1:
This is the front end of the application that is visible to the user. This is where they'll see the random generator printing th eoutput of what dog th euser should get next. A http request is sent to the other three services. The result of what's randomly generated is stored in a mysql database container. From the database, the previous results are also displayed to the user. 

Here is the front end of the application:
![List of items](https://github.com/michelle548129/DogGenerator/blob/main/Application%20in%20action%20with%20random%20generated%20outputs.PNG)

### Service 2:
My service 2 is my breed API. It randomly generates the dogs breed when Service 1 sends out a GET request. 

### Service 3:
My service 3 is my name API. It randomly generates the dogs name when Service 1 sends out a GET request. 

### Service 4:
My service 4 is type API where it provides the user with a characteristic of the dog whether it be colour, type of hair or personality. 
An nginx instance was created as a loadbalancer so that too much traffic wasn't being sent to just one instance and the traffic would instad be split between the two.  

## Rolling Updates
I made an update to change the background colour of the application from blue to red. When refreshed, the application then changed with it.

![test.sh](https://github.com/michelle548129/DogGenerator/blob/main/update.PNG)

## Testing
After creating the application, I had to test it to make sure that everything was working and was fully functional. This would prevent errors being thrown to the user later down the line when the application is being used. The tests were made to check:
- whether the application was running
- whether data was being stored in the database correctly
- whether the right output was being printed

![test.sh](https://github.com/michelle548129/DogGenerator/blob/main/test.PNG)

## Known Issues

![Testing report](https://github.com/michelle548129/DogGenerator/blob/main/connection%20fail.PNG) 

![Jenkins build failed](https://github.com/michelle548129/DogGenerator/blob/main/jenkins%20fail.PNG)

As shown above, I ran into errors when trying to run the pipeline successfully as it wasn't working. This is something I had trouble completing as I was on a tight deadline too. 
I couldn't get my Jenkins to build successfully becuase I had trouble connecting swarm manager ssh with jenkins ssh. This was a very vague error which was hard to fix as I wasn't sure what part of the code was wrong or what I had to do with the SSH instances for it to work. 

![test.sh](https://github.com/michelle548129/DogGenerator/blob/main/error%20fixed.PNG)

I was able to fix this error later on, despite it having taken up a lot of time.


## Future Work/Improvements
Future improvements would be to work on the aesthetics of the application. For this project, my main focus was ensuring the application was fully functional and getting the 4 services implemented and working which took up the majority of the time. In the future, I would add CSS to make the websit elook more appealing.

I would also want to fix the issues brought up in the Jenkins pipeline where the testing failed. I needed more time so that I could fix the testing code and successfully deploy my Jnekins pipeline. 


