from alchemyapi import AlchemyAPI
import requests
import json
alchemyapi = AlchemyAPI()


myText = raw_input("Hey, I'm Rayk! Your friendly neighborhood president!.\n")
response_ent = alchemyapi.entities('text', myText, {'sentiment': 1})
response_key = alchemyapi.keywords('text', myText, {'sentiment': 1})

if response_ent['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response_ent, indent=4))

    print('')
    print('## Entities ##')
    for entity in response_ent['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response_ent['statusInfo'])

if response_key['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response_key, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response_key['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response_key['statusInfo'])
