#!/usr/bin/python

import uuid # for random unique identifiers

# http://blitzdb.readthedocs.org/en/latest/
from blitzdb import Docuement
from blitzdb import FileBackend

# /path/to/db
backend = FileBackend("./Programs/CS213/parallel-web-server-chatbot/db")

class Person(Docuement):
    pass


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
    filePath = "files/" + uid + ".txt"
    file = open(filepath, 'a')  # opens file for appending
                                # creates new file if not already there

    # get user input
    file.write(userInput.get('author') + ": " + userInput.get('message') + "\n")
    # get chatbot response
    file.write("bot does not respond yet\n")    

    file.close()

def start(message):

    currentUsername = '' # get username from prompt
    currentPassword = '' # get password from prompt
    # maybe one more identifier from prompt?

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
        


if __name__ == '__main__':
    start('')
