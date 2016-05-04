# Basic chat implementation from http://code.runnable.com/UqDMKY-VwoAMABDk/simple-websockets-chat-with-tornado-for-python
import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import alchemy
import time

clients = []

class IndexHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(request):
    request.render("index.html")

class WebSocketChatHandler(tornado.websocket.WebSocketHandler):
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
      self.load_user(dict)
    elif dict["type"] == "message":
      self.process_chat(dict)



  def load_user(self, message_dict ):
    d = { 'user': '[SYSTEM]',
          'message': "Login attempt by %s." % (message_dict["user"])}
    self.write_message(json.dumps(d))
    # TODO: load or create user data
    return

  def process_chat(self, message_dict ):
    message_dict.pop( "type", None )
    self.write_message(json.dumps(message_dict))
    # fetch reponse from bot
    bot_response = alchemy.getRaykResponse(message_dict["message"])
    # create message dict
    d = { 'user': 'RayK',
          'message': "%s." % bot_response}
    print bot_response
    # calculate delay using WPM = 90
    delay = alchemy.calculateDelay(bot_response)
    # sleep for the length of our delay (which is in seconds)
    time.sleep(alchemy.calculateDelay(bot_response))
    # send response to client
    self.write_message(json.dumps(d))

  def on_close(self):
    clients.remove(self)

app = tornado.web.Application([(r'/chat', WebSocketChatHandler), (r'/', IndexHandler)])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
