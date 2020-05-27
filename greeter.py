import pyttsx3
import time
import json
import requests


#Initial setup of voice engine.
engine = pyttsx3.init()
engine.setProperty('voice', 'irish-gaeilge')

#Checks for configuration file and returns a boolean value.
def validateConfig():
    
    try:
        config = json.load(open('config.json'))
        return True
    except IOError:
        print('Configuration file not found\nCreating new Configuration file')
        return False


#Prompts the user for configuration information and stores it in a JSON file
def userConfig():
    
    userInfo = {
        'name' : '',
        'zip code' : ''}

    userInfo['name'] = raw_input('Enter Your Name \n')
    userInfo['zip code'] = raw_input('Enter your ZIP Code \n')

    with open('config.json', 'w') as c:
        userInfo["name"] = userInfo['name']
        userInfo['zip code'] = userInfo['zip code']
        json.dump(userInfo, c)


#pulls time and gives proper greeting
def greet(userName):

    currTime = time.localtime()
    
    if currTime.tm_hour < 12:
        engine.say("Good Morning {}".format(userName))
    elif (currTime.tm_hour >= 12) & (currTime.tm_hour < 17):
        engine.say("Good Afternoon {}".format(userName))
    else:
        engine.say("Good Evening {}".format(userName))
    
    engine.runAndWait()

#pulls weather using zip code from config file.
def getTemp(location):
    weatherData = requests.get("http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=16f2529eb6bf744dc55161010e203414&units=imperial".format(location))
    currTemp = weatherData.json()['main']['temp']

    engine.say("The temperature is {}".format(currTemp))

    engine.runAndWait()


def main():
    
    if validateConfig() == False:
        userConfig()

    with open('config.json', 'r') as c:
        userData = json.load(c)
        userName = userData['name']
        zipCode = userData['zip code']
 
    greet(userName)
    getTemp(zipCode)


main()




