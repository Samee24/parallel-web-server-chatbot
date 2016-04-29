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
        file = open(filepath, 'r')

        packet = file.read(2000) # read 2 kilobytes from file
        while packet != '': # while not EOF
            # send packet to page
            packet = file.read(2000)

    except IOError:
        pass                    # send info that file 

   file.close()


def chat(uid):
    filePath = "files/" + uid + ".txt"
    file = open(filepath, 'a')  # opens file for appending
                                # creates new file if not already there

    stillChatting = True       #need some way to determine when still chatting

    while stillChatting:
        file.write()            #get user input
        file.write("\n")
        file.write()            #get chatbot response


    file.close()

def start():

    returningUser = True        # need to see if user is returning

    if returningUser:

        currentUsername = ''    # have user enter their name
        currentAge = 0          # have user enter age
        currentPassword = '1234' # have user enter their password

        try:
            currentUser = backend.get(Person,{'name' : currentUsername, 'age' : currentAge, 'password' : currentPassword})

            wantsToChat = True  # see if user wants to chat or see file
    
            if wantsToChat:
                chat(currentUser.unique_id)

            else:
                displayFile(currentUser.unique_id)
                
        except Person.DoesNotExist:
            pass                # if can't find user

    else: # new user
        newName = ''            # get their name
        newAge = 30             # get their age
        newPassword = ''        # get their password
        newID = uuid.uuid4()
    
        newUser = Person({ 'name' : newName,
                           'age' : newAge,
                           'password' : newPassword,
                           'unique_id' : newID
                           })

        backend.save(newUser)
        backend.commit()        # commits changes to disk

        

if __name__ == '__main__':
    start()
