
## RayKay Websocket Chatbot ##
* The chatbot can be run on any machine with the command 'python server.py'. By default, it is hosted on local port 5000.
* Users may choose to log in with a specified username and password, prompted when the webpage is open.
 * If the username is not already in the database, a new entry is created with that username and password.
 * If the username is already in the database with the corresponding password, the transcript of all previous chats will be loaded to the screen.
 * If the username is already in the database with a different password, a new entry will be created for the new password, with a separate record.
 * If no username is entered, the conversation will not be recorded, and the user will be labeled "Anonymous"
* When the user sends a message, the server will search for keywords, and respond accordingly.
 * The current implementation is very limited in its responses (perhaps more closely resembling the man it is modeled after). The only keywords it recognizes are "hey", "hello", "health", and "diversity".
 * The server artificially creates a delay to make the bot seem more realistic. Messages are not processed until all prior messages have been responded to.
 
The following is an example of Ray Kay's response system:
```
[SYSTEM]: User is Anonymous.
Anonymous: hey
RayK: Hey there, student!.
Anonymous: health
RayK: Have you heard of SHACS? It's a magical place where all of your health problems will get solved! It's open Mon-Fri, 8 am - 5 pm and is located at the bottom of the forum! Here's a Google maps link: https://goo.gl/maps/T472hRBidgN2.
Anonymous: diversity
RayK: We are a very inclusive college, by virtue of our data-drive approach.
```


Dependencies (WIP):
```
python2.7
tornado-4.3-py2.7
blitzdb
requests
```
TODO: script to handle dependency installations
