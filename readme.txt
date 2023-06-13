Starting the Program and Running Commands
To start the console 
Input:
	./console
Output:
	(hbnb)

Now here are some examples on how to use the console using the create, show, update, all, and destroy commands.

To create a new user
Steps:
1) To get the new user id
Input:
	(hbnb) create BaseModel
Output:
	49faff9a-6318-451f-87b6-910505c55907

2) Copy and paste the id
3) Now you'll need to update the BaseModel id
Input:
	(hbnb) update BaseModel <id> <"Name">

4) To check and see if your username was saved into the storage file you will
need to use either the command show command or the all command
Input:
	(hbnb) show BaseModel <id>
Output:
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	
or
Input:
	(hbnb) all BaseModel
Output:
	[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
And to destroy a user

Input:
	(hbnb) destroy BaseModel <id> 
Output:
	** no instance found **

Once you are ready to quit the program you will simply type quit into the terminal
Input:
	(hbnb) quit
