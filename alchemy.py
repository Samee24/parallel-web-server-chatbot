from alchemyapi import AlchemyAPI
import requests
import json
alchemyapi = AlchemyAPI()
# Some phrases that will be used by the bot
GREETING_PROMPT = "Hey there, student!"
ERROR_PROMPT = "Hey, I couldn't really understand you. Try saying that again."
# Print opening message
# print("Hey, I'm Rayk! Your friendly neighborhood president!.")
# Our set of rules --  a dictionary
rule_dict = {
    'hello': GREETING_PROMPT,
    'hi': GREETING_PROMPT,
    "what's up": GREETING_PROMPT,
    'hey': GREETING_PROMPT
  }

def getRaykResponse(user_input):    # return chat bot response
  myText = user_input
  response_key = alchemyapi.keywords('text', myText, {'sentiment': 1})
  # If we got a response back from the API
  if response_key['status'] == 'OK':
    # Loop over all identified keywords
      for keyword in response_key['keywords']:
        word = keyword['text'].encode('utf-8')
        # If a rule exists for our word, then use it
        if word.lower() in rule_dict:
          return rule_dict[word.lower()]
        else:
          print(ERROR_PROMPT)
  else:
      print('Error in keyword extaction call: ', response_key['statusInfo'])

def calculateDelay(response):  # return delay in seconds for each reponse using WPM = 90
  delay = len(response.split())/1.5
  if (delay > 4):
    delay = 4
  return delay


