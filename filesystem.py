#!/usr/bin/python

import uuid # for random unique identifiers

# http://blitzdb.readthedocs.org/en/latest/
from blitzdb import Document
from blitzdb import FileBackend

# /path/to/db
backend = FileBackend("./db")

class Person(Document):
    pass


# current display trigger word is 'print transcript'
def displayFile(uid):
    #requires that files are stored in seperate directory files
    filePath = "./files/" + str(uid) + ".txt"

    try:
        file = open(filePath, 'r')
    except IOError:
        print("404: File Not Found")
    else:
        lines = [line.strip('\n') for line in file]   
        for line in lines:
            print(line) 
        file.close()



def chat(uid, userInput, botResponse):
    # current display trigger word is 'print transcript'
    if userInput.get('message') == 'print transcript' or userInput.get('message') == 'print transcript\n':
        displayFile(uid)

    else:
        filePath = "./files/" + str(uid) + ".txt"
        try:
            file = open(filepath, 'a')  # opens file for appending
                                        # creates new file if not already there
        except IOError:
            print("Problem opening file")
        else:
            # get user input
            file.write(userInput.get('user') + ": " +
                       userInput.get('message') + "\n")
            # get chatbot response
            file.write("bot does not respond yet\n")    

            file.close()

def start(message):

    currentUsername = message.get('user')       # get username from prompt
    currentPassword = message.get('password')   # get password from prompt
    
    
    try:
        currentUser = backend.get(Person,{'user' : currentUsername,
                                          'password' : currentPassword
                                          })

    except Person.DoesNotExist:
        newUser = Person({ 'user' : currentUsername,
                           'password' : currentPassword,
                           'unique_id' : str(uuid.uuid4())
                           })
        
        backend.save(newUser)
        backend.commit()
        
        return newUser.unique_id

    except Person.MultipleDocumentsReturned:
        print("ERROR: Multiple Documents Returned")
    
    else:
        return currentUser.unique_id
        
