from alchemyapi import AlchemyAPI
import requests
import json
alchemyapi = AlchemyAPI()

GREETING_PROMPT = "Hey there, student!"
ERROR_PROMPT = "Hey, I couldn't really understand you. Try saying that again."
print("Hey, I'm Rayk! Your friendly neighborhood president!.")
rule_dict = {
    'hello': GREETING_PROMPT,
    'hi': GREETING_PROMPT,
    "what's up": GREETING_PROMPT,
    'hey': GREETING_PROMPT
  }
while True:
  myText = raw_input("")
  response_key = alchemyapi.keywords('text', myText, {'sentiment': 1})
  if response_key['status'] == 'OK':
      for keyword in response_key['keywords']:
        word = keyword['text'].encode('utf-8')
        if word.lower() in rule_dict:
          print(rule_dict[word])
        else:
          print(word.lower())
  else:
      print('Error in keyword extaction call: ', response_key['statusInfo'])
