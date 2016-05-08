from alchemyapi import AlchemyAPI
import requests
import json
alchemyapi = AlchemyAPI()
# Some phrases that will be used by the bot
GREETING_PROMPT = "Hey there, student!"
ERROR_PROMPT = "Hey, I couldn't really understand you. Try saying that again."
DIVERSITY_PROMPT = "We are a very inclusive college, by virtue of our data-driven approach"
SHACS_PROMPT = "Have you heard of SHACS? It's a magical place where all of your health problems will get solved! It's open Mon-Fri, 8 am - 5 pm and is located at the bottom of the forum!\nHere's a Google maps link: https://goo.gl/maps/T472hRBidgN2"
DARI_BARN_PROMPT = "Here's a neat little thing made by the S&B to help you choose you what you should get!\n http://www.thesandb.com/wp-content/uploads/2016/05/dari-barn.jpg\n Where is Dari Barn? Here's a Google maps link: https://goo.gl/maps/52VVtLN4tbo"
ICE_CREAM_PROMPT = "You should try going to Dari Barn -- Grinnell's favorite place to get ice-cream!\n Here's a Google maps link: https://goo.gl/maps/52VVtLN4tbo"

# Print opening message
# print("Hey, I'm Rayk! Your friendly neighborhood president!.")
# Our set of rules --  a dictionary
rule_dict = {
    'hello': GREETING_PROMPT,
    'hi': GREETING_PROMPT,
    "what's up": GREETING_PROMPT,
    'hey': GREETING_PROMPT,
    'health': SHACS_PROMPT,
    'stressed': SHACS_PROMPT,
    'help': SHACS_PROMPT,
    'sick': SHACS_PROMPT,
    'inclusivity': DIVERSITY_PROMPT,
    'diversity': DIVERSITY_PROMPT,
    'ice-cream': ICE_CREAM_PROMPT,
    'ice' : ICE_CREAM_PROMPT,
    'cream': ICE_CREAM_PROMPT,
    'dari': DARI_BARN_PROMPT,
    'barn': DARI_BARN_PROMPT
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
      print('Error in keyword extaction call: ', response_key['statusInfo'])
  # if nothing is returned, return error
  return ERROR_PROMPT

def calculateDelay(response):  # return delay in seconds for each reponse using WPM = 120
  delay = len(response.split())/2
  if (delay > 2):
    delay = 2
  return delay


