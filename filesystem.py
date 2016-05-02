#!/usr/bin/python

import uuid # for random unique identifiers

# http://blitzdb.readthedocs.org/en/latest/
from blitzdb import Docuement
from blitzdb import FileBackend

# /path/to/db
backend = FileBackend("./db")

class Person(Docuement):
    pass


# current display trigger word is 'print transcript'
def displayFile(uid):
    #requires that files are stored in seperate directory files
    filePath = "files/" + uid + ".txt"

    try:
        lines = [line.strip('\n') for line in open(filepath, 'r')]       
    except IOError:
        self.write_message("404: File Not Found")

    else:
        for line in lines:
            self.write_message(line) 
        file.close()



def chat(uid, userInput, botResponse):
    # current display trigger word is 'print transcript'
    if userInput.get('message') == 'print transcript':
        displayFile(uid)

    else:
        filePath = "files/" + uid + ".txt"
        try:
            file = open(filepath, 'a')  # opens file for appending
                                        # creates new file if not already there
        except IOError:
            pass
        else:
            # get user input
            file.write(userInput.get('author') + ": " +
                       userInput.get('message') + "\n")
            # get chatbot response
            file.write("bot does not respond yet\n")    

            file.close()

def start(message):

    # TODO
    currentUsername = '' # get username from prompt
    currentPassword = '' # get password from prompt
    # maybe one more identifier from prompt?
    # /TODO
    
    try:
        currentUser = backend.get(Person,{'user' : currentUsername,
                                          'password' : currentPassword
                                          # would add identifier here
                                          })

    except Person.DoesNotExist:
        newUser = Person({ 'user' : currentUsername,
                           'password' : currentPassword,
                           # would add identifier here
                           'unique_id' : uuid.uuid4()
                           })
        
        backend.save(newUser)
        backend.commit()
        
        return newUser.unique_id

    except Person.MultipleDocumentsReturned:
        pass
    
    else:
        return currentUser.unique_id
        
