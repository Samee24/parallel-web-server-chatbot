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
    try:
        #requires that files are stored in seperate directory files
        filePath = "files/" + uid + ".txt"

        lines = [line.strip('\n') for line in open(filepath, 'r')]
        self.write_message(packet) # send packet to page
        file.close()
    except IOError:
        self.write_message("404: File Not Found")



def chat(uid):
    filePath = "files/" + uid + ".txt"
    file = open(filepath, 'a')  # opens file for appending
                                # creates new file if not already there

    stillChatting = True       #need some way to determine when still chatting

    while stillChatting:
        file.write(message.get('author')            #get user input
        file.write("\n")
        file.write()            #get chatbot response


    file.close()

def start():

    returningUser = True        # need to see if user is returning

    if returningUser:

        currentUsername = message.get('author')    # have user enter their name
        currentAge = message.get('age')          # have user enter age
        currentPassword = message.get('password') # have user enter their password

        try:
            currentUser = backend.get(Person,{'author' : currentUsername, 'age' : currentAge, 'password' : currentPassword})

            wantsToChat = True  # see if user wants to chat or see file
    
            if wantsToChat:
                chat(currentUser.unique_id)

            else:
                displayFile(currentUser.unique_id)
                
        except Person.DoesNotExist:
            pass                # if can't find user

    else: # new user
        newName = message.get('author')   # get their name from message in python.py
        newAge = message.get('age')   # optional, would need another field
        newPassword = message.get('password')   # get their password
        newID = uuid.uuid4()
    
        newUser = Person({ 'author' : newName,
                           'age' : newAge,
                           'password' : newPassword,
                           'unique_id' : newID
                           })

        backend.save(newUser)
        backend.commit()        # commits changes to disk

        

if __name__ == '__main__':
    start()
