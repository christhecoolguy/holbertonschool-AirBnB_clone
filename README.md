howdy everyone so your probly wondering what this is about? its airBnB console! A section of this AirBnB project oh you havent heard about this well its just the consol so when writing an interperter that will manage the objects of our project:

The command interpreter is a command-line interface that provides interaction with the AirBnB clone and enables users to manage the objects within the application. Here are the details on how to start and use the command interpreter: How to Start the Command Interpreter

Create a new object (ex: a new User or a new Place) Retrieve an object from a file, a database etc… Do operations on objects (count, compute stats, etc…) Update attributes of an object Destroy an object Starting the command interpreter You are able to start the command interpreter by running the following command:

./console Using the command interpereter Once you have ran

./console you are now able to run commands within the interpreter while using the following format!

create: Create a new instance of an object.
show: Display detailed information about a specific object.
destroy: Delete an object from the system.
all: Retrieve all objects or all objects of a specific class.
update: Update the attributes of an object.
quit: Exit the command interpreter.

## Examples

Starting the Program and Running Commands
To start the console

**Input:**
```python
./console
```
**Output:**
```python
	(hbnb)
```

Now here are some examples on how to use the console using the create, show, update, all, and destroy commands.

To create a new user
Steps:
1) To get the new user id
**Input:**
```python
(hbnb) create BaseModel
```
**Output:**
```python
49faff9a-6318-451f-87b6-910505c55907
```
2) Copy and paste the id
3) Now you'll need to update the BaseModel id
**Input:**
```python
(hbnb) update BaseModel <id> <"Name">
```
4) To check and see if your username was saved into the storage file you will
need to use either the command show command or the all command
**Input:**
```python
	(hbnb) show BaseModel <id>
```
**Output:**
```python
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
or
**Input:**
```python
(hbnb) all BaseModel
```
**Output:**
```python
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
And to destroy a user
**Input:**
```python
(hbnb) destroy BaseModel <id> 
```
**Output:**
```python
** no instance found **
```
Once you are ready to quit the program you will simply type quit into the terminal
**Input:**
```python
(hbnb) quit
```
