# TBL-House-Rent

TBL-Teletalk Bangladesh Limited
BTS-Base transciever Station

To run this project:
1.You need to first install Python 3.8
2.set virtual env for Django 
3.install Django==3.0.5
5.install PyCharm or Visual Studio Code
6.Download/clone my project
7.Open the project in Pycharm/VS Code
8.Do migrate if any migration has been missed that will be migrated
9.Use username:dpe and password:1234 for admin login
10.Use username:executive and password:1234 for executive login

User Requirements, System Requirements, Functional, non functional requirements for this project:

3.3.1 User Requirements for Agent:

1.	User can login to the software.
2.	User can see the dashboard of the system.
3.	User can add an agreement of their client.
4.	User can add BTS house rent.
5.	User can see the list of agreement.
6.	User can see the rent payable.
7.	User can add a payment.
8.	User can see the house rent list.

3.3.2 User Requirements for Admin:
1.	Admin can login to the software.
2.	Admin can assign an agent.
3.	Admin can delete an agent.
4.	Admin can update the information of agent.
5.	Admin can see the list of agent.
6.	Admin will recognize/accept an agreement.
7.	Admin will recognize/accept BTS payment.
8.	Admin can see the BTS list.
9.	Admin can delete a BTS information.
10.	Admin can update a BTS information.
11.	Admin can reject the request of adding agreement.
12.	Admin can see the Rent list.
13.	Admin can delete a payment.



3.4 System Requirements:
3.4.1 System Requirement for Agent:
1.	User can login to the software.
1.1	After assigning a user, user can get user id and password.
1.2	System will check whether user id and password is valid or not.
1.3	If id and password is valid, user can enter to the software.
2.	User can see the dashboard of the system.
2.1 After login user can see the dashboard of his own home page.
2.2 User can enter any module of his/her dashboard.
3.	User can add an agreement of their client
3.1 After clicking BTS details option he can see Add agreement option. And if he clicks Add Agreement option he will see a new form.
3.2 After seeing new form, he can fill up the form.
3.3 After fill upping the form he can submit it for approval of Admin.
4.	User can add Previous Agreement (previously paid).
4.1 User can add also previous agreement, but he should mention it that this a previously paid.
4.2 For adding Previous Agreement he need to click add agreement option.
4.3 After clicking add agreement option he will see a form.
4.4 After seeing a new form he will fill up every field and should mention that that is previously paid agreement.

5.	User can see the list of agreement
5.1.	After Approving Add Agreement request, Agent user can see the Agreement list.

6.	User can add a payment.
6.1 After clicking payment option of his dashboard he can see two option.
6.2 If he click the Add payment option he will see a new form of Adding payment.
6.3 After fill upping the form, he can submit it for approving of Admin.

7.	User can see the house rent list.
7.1 After clicking Payment he can see two option, Add payment and Rent List.
7.2 If Admin approve a payment it will store in Rent list. 
7.3 After clicking Rent list, Agent can see the all rent.

3.4.2 System Requirements for Admin:
1.	Admin can login to the software.
1.1	Admin must have User id and password.
1.2	System will check whether the User id and password is valid or not.
1.3	If the user id and password is valid, Admin can enter his own homepage.

2.	Admin can assign an agent.
2.1 After login to the software, user can assign a new agent user.
2.2 For assigning a new user, Admin must click on the Add user option.
2.3 After clicking, a new form will come.
2.4 Admin will fill up the form assigning a unique id and password.

3.	Admin can delete an agent.
3.1 After assigning a new user that will be stored in database.
3.2 For deleting a user admin should click on the delete option into Add User option.
3.3 After clicking delete a list of all user will come.
3.4 Admin can select a random user.
3.5 After clicking the delete button of selected user, user will be deleted.

4.	Admin can update the information of agent.
4.1 For updating Agent information, Admin need to click the Edit option.
4.2 A list of all user will come.
4.3 Admin can select a user and click the edit button.
4.4 Previous fil upped form will come with current user information.
4.5 Then Admin can edit and can submit it.

5.	Admin can see the list of agent.
5.1 After clicking List of agent, admin can see the all agent user.

6.	Admin will recognize/accept an agreement.
6.1 Admin will see the approval request.
6.2 After clicking approval request he will see all the request.
6.3 If he selects agreement request the issued agreement form will come.
6.4 After clicking approved option, the request will be approved.

7.	Admin will recognize/accept BTS payment.
7.1 After clicking approval request he will see all the request.
7.2 If he selects payment request the issued payment form will come.
7.3 After clicking approved option, the request will be approved.

8.	Admin can see the BTS list.
8.1	After clicking the BTS , admin can see the all BTS list.

9.	Admin can reject the request of adding agreement/adding payment.
9.1 After clicking approval option, all the requests will come.
9.2 After clicking on a request admin will see reject options besides this.
9.3 After clicking reject option Admin can reject a request.

10.	Admin can see the Rent list.
10.1 After clicking the Rent list option, Admin can see all the rent list.

3.5 Functional Requirements
1.	Sign in System.
2.	Report Generate.
3.	Admin can Delete the user.
4.	Deleted User can not login the system.
5.	With same user ID multiple User can not be created.
6.	Agent can see only his homepage.
7.	Agent can not delete any BTS Agreement, Payment.
8.	Agent can generate check.

3.6 Non- Functional Requirements
1.	Each user (admin, agent user) has his own account.
2.	Users have to sign in with his own password.
3.	Password will be encrypted.
4.	User ID & password for admin, Agent User saved in database for security purpose.
5.	Usability, reliability & availability requirements must be ensured.





#Uncomplited Work:
1. Missing Executive Authentication
2.Check PDF download


**Inshallah within next commit i will fix it 



---------------Najmul Ahsan Rakib-----------------------






