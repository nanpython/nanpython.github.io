---
title: A Python console application - ToDos
tags: dict, list, function
author: Anand B
date: May 8, 2022
---

# A Python console application for ToDos
The objective of this post is to introduce Python list, dictionary and function definition. We will develop a small application to run on the console. A ToDo as you are probably aware is a task that we wish to complete, like what you see in a list of tasks to do.

### Intro to Python list, dictionary and function
### list
A list is a sequence of objects such as numbers, characters, strings or other Python objects. List is modifiable, that is once created we can add, remove or replace the contents of a list. The list contains elements in the order in which the elements are inserted.
```
# create an empty list
a_list = []

# create a list with some elements
num_list = [2, 4, 3, 56, 33, 12, -2, 0]
print(num_list)

# add elements to a list using the list's append function.
a_list.append('weather')
a_list.append('climate')
print(a_list)

num_list.append(89)
num_list.append(76)
num_list.append(-6)
print(num_list)

# The append operation adds the element to the end of the list. The length of the list grows as a result of the append operation.
a_list_size = len(a_list)
print(a_list_size)
```
We can insert elements at any location in the list using the insert function. The element location is computed using the index function. List elements start adding from index 0 to the length of the list - 1.
```
# print the third element in num_list
ptint(num_list[2])
```
The nth element is at location n-1 in the sequence, because indexing of the sequence starts from 0.

### dictionary
A Python dictionary is a collection of key-value pairs. 

```
# empty dictionary
a_dict = {}
# a dict with names and IDs as values
names_dict = {'jack' : 123456, 'sheela', 987865, 'san': 56748}
# print sheela's number. 
id_sheela = names_dict['sheela']
print(id_sheela)
```
The strings jack, sheela and sam are called keys. The numbers associated with the names are called values. A key and it value re linked by the colon (:). The key-value pairs are separated by a comma (,).

If a key is not present inthe dicfionary, then Python reports an error. Otherwise, it will returnthe value for the specified key.

### function
A function is a group of executable Python statements. It processes according to specified logic, and may or may not return a result after processing. Functions are also called methods or routines. 
```
# let us create a dictionary and code a function that returns a number given a name
names_dict = {'jack' : 123456, 'sheela', 987865, 'san': 56748}
# define a function. Returns a number from the names dictionary when a name is passed as a parameter to the function.
def get_number(name):
    if name in names_dict:
        number = names_dict[name]
        return number
    else:
        print('No such name in the dictionary')
```
We handle the error that will arise in case the name is not in the dictionary.
```
# call the function
num = get_number('sheela')
print(number)
```
Play around some more with this function and also write your own to get a grip on the concept.

Let us now turn to ourToDo application. We want to be able to perform the following tasks:
1. Store todos in a dictionary with key = todo task and value = todo status
2. Write functions to add, edit and show all todos and show completed todos
3. to show completed todos we will use a list

Let us start coding. We will follow the sound coding principle: *code a little and test a little*
Declare a dictionary object. Create an empty dictionary that will eventually hold all the todos.
```
todos = {}
```
A python dictionary holds data as key-value pairs. The keys in a dictionary are unique. Keys and values are separated by a semi-colon, and the pairs are separated by commas. The key can be numeric or character data and the value can contain any type - numeric, character, lists, dictionaries, including None.

Now we will define a function that will add a todo to the dictionary we created above. The key is a string for todo and the value contains true or false.

```
# funtion to add an item and its status
def add(item):
	todos[item] = False
```
The add function accepts a parameter which will be the key in the dictionary. The key is used to index into the dictionary for its value. When a todo is created, its value is set to false. When the todo is completed, its value changes to true.

Let us add a few todo items to the todos dictionary. The add function is called four times to create four todo items.

```
# add todo items to the todos dictionary
add('buy shoes')
add('learn to code')
add('do exercise')
add('order food')
```

We will now write a function to display the todos created above.

```
def show_all():
	for key in todos:
		print(f'todo = {key} - status = {todos[key]}')
```
Test the code now by calling the show_all function
```
show_all()
```
If all went well so far, we will see the following output in the format todo = <todo name> - status = <false>. We use an f-string to display the data.
### Output
todo = buy shoes - status = False
todo = learn to code - status = False
todo = do exercise - status = False
todo = order food - status = False

There is a *for* loop in the show_all function. For every key in the todos dictionary, the key is printed along with its value, using the scheme dict[key] = value. This scheme was already introduced in the add method. The structure in which the data is stored in the dictionary will be clear if we print the todos on the console.

```
print(todos)
```
### Output
{'buy shoes': False, 'learn to code': False, 'do exercise': False, 'order food': False}

Now we will need a function to change the status of a todo item in the todos dictionary. We will pass the name of a todo to the function and if it exists in the todos dictionary, the function will change its status from false to true. True indicates that the todo task is completed.

```
# change status of a todo from false to true
def set_status(todo):
	if todo in todos:
		todos[todo] = True
	else:
		print('No such item exists')
```
The function tests (using an if condition) to check whether the todo that we pass is in the dictionary. If the item passed is not in the dictionary, it prints a message that says:  No such item exists. If the item exists in the todos dictionary, then the function fetches that item's value (using the scheme dict[key]) and assigns True to it.

Let us the test the code to see if it is working properly.
```
# test
set_status('learn to code')
set_status('orders food')
show_all()
```
### Output
```
No such item exists
todo = buy shoes - status = False
todo = learn to code - status = True
todo = do exercise - status = False
todo = order food - status = False
```
The first line of output shows that the set_status function returned a message and failed to change the status of the todo item passed. That is correct, because there is no todo with the name "orders food" in the todos dictionary. It is a typo. The rest of the output is clear. The "learn to code" task is completed, and the remaining still show as incomplete (value/status = false).

Now that we have tested the code so far successfuly, let us proceed a define a function that will return a list of completed todo items.

```
# display completed todos - version 1

completed = list(filter(lambda key : todos[key] == True, todos.keys()))
print(completed)
```

Version 1 code to display completed todos uses list comprehension, a mechanism that employs anonymous function called lambda. 

The dictionary is filtered for keys whose values equal True. After filtering, the result is converted to a list. Beginning programmers may find this difficult to understand, but they are encouraged to learn more about comprehensions after this introduction.

```
# display completed todos - version 2
completed = []
def get_completed():
	for key in todos:
		if todos[key]:
			completed.append(key)

get_completed()
print(f'completed = {completed}')
```

Before defining the method, we created an empty list to hold the names of the completed todos. In the body of the function, we loop through the todos by keys and extract their values one by one. We test each value for its status. If the status of a todo item is true, we add it to the list using the list's append function.

Now we are ready to the call the function. The print statement displays the contents of the list of completed todos.

This completes the mini console project. It is best to enhance the project further by adding more functions. We will part here with a small function as an exercise.

**Excercise**
- Calculate and display the percentage of completed todos with respect to the total.
- Display the number of todos yet to be done