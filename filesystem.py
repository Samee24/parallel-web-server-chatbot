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
        print("Failing to open")
        return None
    else:
        lines = [line.strip('\n') for line in file]
        file.close()
        return lines
        



def chat(uid, userInput, botResponse):
    # current display trigger word is 'print transcript'
   # if userInput.get('message') == 'print transcript' or userInput.get('message') == 'print transcript\n':
 #       displayFile(uid)
    if uid == 0:
        pass
    else:
        filePath = "./files/" + str(uid) + ".txt"
        try:
            file = open(filePath, 'a')  # opens file for appending
                                        # creates new file if not already there
        except IOError:
            print("Problem opening file")
        else:
            # get user input
            file.write(userInput.get('user') + ":" +
                       userInput.get('message') + "\n")
            # get chatbot response
            file.write(botResponse.get('user') + ":" +
                       botResponse.get('message') + "\n")

            file.close()

def start(message):

    currentUsername = message.get('user')       # get username from prompt
    currentPassword = message.get('password')   # get password from prompt

    if message.get('user') == 'Anonymous':
        return 0
    
    try:
        currentUser = backend.get(Person,{'user' : currentUsername,
                                          'password' : currentPassword
                                          })

    except Person.DoesNotExist:
        newUser = Person({ 'user' : currentUsername,
                           'password' : currentPassword,
                           'unique_id' : str(uuid.uuid4())
                           })
        print("DNE")
        backend.save(newUser)
        backend.commit()
        
        return newUser.unique_id

    except Person.MultipleDocumentsReturned:
        print("ERROR: Multiple Documents Returned")
    
    else:
        return currentUser.unique_id
        
