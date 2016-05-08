#!/usr/bin/python

import uuid # for random unique identifiers
import os
import errno
# http://blitzdb.readthedocs.org/en/latest/
from blitzdb import Document
from blitzdb import FileBackend

# /path/to/db
backend = FileBackend("./db")

# create directory for saving chat logs if directory does not already exist
try:
    os.makedirs("./files")
except OSError as exception:
    if exception.errno == errno.EEXIST:
        pass
    else:
        raise

# needed for storing user info in database
class Person(Document):
    pass


# Parameters:   takes unique ID representing a specific user
# Returns:      a list containing the lines of the user's chat file
def displayFile(uid):
    if uid == 0:  # don't bother for anonymous users
        pass
    
    else:
    
        #requires that files are stored in seperate directory files
        filePath = "./files/" + str(uid) + ".txt"

        try: # attempt to open file
            file = open(filePath, 'r')
        except IOError:  # if open fails
            print("Failing to open")
            return None
        else: # otherwise make list of lines and return it
            lines = [line.strip('\n') for line in file]
            file.close()
            return lines
        

# Parameters: uid, unique ID representing a specific user
# Function appends new user chat and bot response to user's file
def chat(uid, userInput, botResponse):
    if uid == 0: # if user is anonymous 
        pass
    else:
        filePath = "./files/" + str(uid) + ".txt"
        try:
            file = open(filePath, 'a')  # opens file for appending
                                        # creates new file if not already there
        except IOError:
            print("Problem opening file")
        else:
            # get user input and write to file
            file.write(userInput.get('user') + ":" +
                       userInput.get('message') + "\n")
            # get chatbot response and write to file
            file.write(botResponse.get('user') + ":" +
                       botResponse.get('message') + "\n")

            file.close()


# Parameters:   message, a dictionary with entries for a username and password
# Returns:      the unique ID of the user, to be used by server.py
def start(message):

    currentUsername = message.get('user')       # get username from prompt
    currentPassword = message.get('password')   # get password from prompt

    if currentUsername == 'Anonymous':
        return 0  # default value for anonymous user
    
    try:  # attempt to find user
        currentUser = backend.get(Person,{'user' : currentUsername,
                                          'password' : currentPassword
                                          })
    except Person.DoesNotExist:
        # if user has not used system before, create database entry
        newUser = Person({ 'user' : currentUsername,
                           'password' : currentPassword,
                           'unique_id' : str(uuid.uuid4())
                           })
        backend.save(newUser)
        backend.commit()
        
        return newUser.unique_id

    else:
        return currentUser.unique_id
        
