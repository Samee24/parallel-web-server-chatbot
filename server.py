# Basic chat implementation from http://code.runnable.com/UqDMKY-VwoAMABDk/simple-websockets-chat-with-tornado-for-python
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.options
import json
import alchemy
import time
import filesystem as fs

clients = []


class IndexHandler(tornado.web.RequestHandler):
  '''get call loads the webpage at index.html'''
  @tornado.web.asynchronous
  def get(request):
    request.render("index.html")

class WebSocketChatHandler(tornado.websocket.WebSocketHandler):

  unique_id = 0 # id for the logged-in user

  '''open is called when the websocket connection is opened'''
  def open(self, *args):
    print("open", "WebSocketChatHandler")
    clients.append(self)

  ''' on_message is triggered when the client sends a string. All messages
  should be received in stringified JSON, and should be sent back to the client
  in the same form. Messages have a "type", either "message" or "username".
  Messages that are usernames include a username and password to be processed
  in the database. Messages that are simply messages should be handled by
  getting a response from the chatbot, and returning both the message and its
  response to the client (separately).
  '''
  def on_message(self, message):
    dict = json.loads(message)
    print message
    # handle different types of messages
    if dict["type"] == "username":
      self.unique_id = fs.start(dict)
      self.load_user(dict)
    elif dict["type"] == "message":
      self.process_chat(dict)



  '''load_user takes a dictionary containing the message data for a
  log-in type of message. It checks if the user is interested in logging
  in, and if they have an existing chat history and the correct password.
  If they do, it loads the entire transcript for that user.'''
  def load_user(self, message_dict ):
    # Send a confirmation message to the client
    d = { 'user': '[SYSTEM]',
          'message': "User is %s." % (message_dict["user"])}
    self.write_message(json.dumps(d))

    # Get the existing transcript
    lines = fs.displayFile(self.unique_id)
    # If the transcript exists, send it to the client to display
    if lines != None:
      for line in lines:
        if line != '':
          l = line.split(':')
          d = { 'user': l[0], 'message': l[1] }
          self.write_message(json.dumps(d))
    # TODO: load or create user data
    return

  '''process_chat is called when the socket receives a standard message
  from the client. It sends that message back to the client to be displayed
  in the chat, and then sends the message to our Alchemy program to generate
  an appropriate response. It then sends that response back to the server as
  well.'''
  def process_chat(self, message_dict ):
    message_dict.pop( "type", None )
    self.write_message(json.dumps(message_dict))
    # fetch reponse from bot
    bot_response = alchemy.getRaykResponse(message_dict["message"])
    # create message dict
    d = { 'user': 'RayK',
          'message': "%s." % bot_response,
          'time': message_dict["time"]}
    fs.chat(self.unique_id, message_dict, d)
    print bot_response
    # calculate delay using WPM = 90
    delay = alchemy.calculateDelay(bot_response)
    # sleep for the length of our delay (which is in seconds)
    time.sleep(alchemy.calculateDelay(bot_response))
    # send response to client
    self.write_message(json.dumps(d))

  '''on_close removes the websocket from the server's list when the socket
  is closed.'''
  def on_close(self):
    clients.remove(self)


app = tornado.web.Application([(r'/chat', WebSocketChatHandler), (r'/', IndexHandler)])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
