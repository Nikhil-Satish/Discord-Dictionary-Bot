import discord
import requests
import random
from discord import channel

from discord.message import Message
dict = {'word': '', 'apiLink': '', 'result': '', 'response': []}
TOKEN = 'OTE0MjUzOTEyNzkyNTMwOTU0.YaKXTg.-Gx7_NzYhB8bqis9QtEmBqurT9Q'
client = discord.Client()


def definit(word):
    defList = ''
    for array in dict['response']:
        if array['word'] == word:
            meanings = array['meanings']
            for item in meanings:
                definitions = item['definitions']
                for element in definitions:
                    defList += element['definition']
                    defList += '\n'
    return defList


def synonym(word):
    synoList = ''
    for array in dict['response']:
        if array['word'] == word:
            meanings = array['meanings']
            for item in meanings:
                definitions = item['definitions']
                for element in definitions:
                    synonyms = element['synonyms']
                    for k in synonyms:
                        synoList += '\n'+k
    return synoList


def antonym(word):
    antoList = ''
    for array in dict['response']:
        if array['word'] == word:
            meanings = array['meanings']
            for item in meanings:
                definitions = item['definitions']
                for element in definitions:
                    antonyms = element['antonyms']
                    for k in antonyms:
                        antoList += '\n'+k
    return antoList


def pos(word):
    posList = ''
    for array in dict['response']:
        if array['word'] == word:
            meanings = array['meanings']
            for item in meanings:
                partOfSpeech = item['partOfSpeech']
                posList += partOfSpeech
                posList += '\n'
    return posList


def allDetails(word):
    all = ''
    all += 'Word : '+word
    for array in dict['response']:
        if array['word'] == dict['word']:
            phonetics = array['phonetics']
            for item in phonetics:
                all += '\nPhonetics text : '+item['text']
                all += '\nPhonetics audio : '+item['audio']
            origins = array['origin']
            all += '\nOrigin : '+origins
            meanings = array['meanings']
            for item in meanings:
                partOfSpeech = item['partOfSpeech']
                all += '\nPart of Speech : '+partOfSpeech
                definitions = item['definitions']
                for element in definitions:
                    all += '\nDefinition : '+element['definition']
                    synonyms = element['synonyms']
                    all += '\nSynonyms : '
                    for k in synonyms:
                        all += '\n'+k
                    antonyms = element['antonyms']
                    all += '\nAntonyms : '
                    for k in antonyms:
                        all += '\n'+k
    return all


@client.event
async def on_ready():
    print('{0.user}'.format(client)+' has logged in successfully!')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    user_message = user_message.lower()
    channel = str(message.channel.name)

    if message.author == client.user:
        return

    if message.channel.name == 'discord-bot':
        if user_message != 'hello' and user_message.isnumeric() == False:
            dict['word'] = user_message
            dict['apiLink'] = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+dict['word']
            dict['result'] = requests.get(dict['apiLink'])
            dict['response'] = dict['result'].json()
            await message.channel.send(f'Enter a number from 1 to 4 to print the respective details of the entered word' +
                                       '\n1.Definition\n2.Synonyms\n3.Parts of Speech\n4.All details ')
            return
        if user_message == 'hello':
            await message.channel.send(f'Hello {username}! Enter a word')
            return
        if user_message.isnumeric():
            if user_message == '1':
                s = definit(dict['word'])
                if s == '':
                    await message.channel.send(f'Sorry no definitions found!')
                    return
                await message.channel.send(f'{s}')
                return

            elif user_message == '2':
                s = synonym(dict['word'])
                if s == '':
                    await message.channel.send(f'Sorry no synonyms found!')
                    return
                await message.channel.send(f'{s}')
                return
            elif user_message == '3':
                s = pos(dict['word'])
                if s == '':
                    await message.channel.send(f'Sorry no parts of speech found!')
                    return
                await message.channel.send(f'{s}')
                return
            elif user_message == '4':
                s = allDetails(dict['word'])
                if s == '':
                    await message.channel.send(f'Sorry no details found!')
                    return
                await message.channel.send(f'{s}')
                return
            else:
                await message.channel.send(f'Invalid entry!')
                return

client.run(TOKEN)
