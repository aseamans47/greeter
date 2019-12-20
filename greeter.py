import pyttsx3
import time


currTime = time.localtime()

engine = pyttsx3.init()
engine.setProperty('voice', 'irish-gaeilge')

#Time is 24 hour configuration with the assumption that 1700 is considered evening.
if currTime.tm_hour < 12:
    engine.say("Good Morning ")
elif (currTime.tm_hour >= 12) & (currTime.tm_hour < 17):
    engine.say("Good Afternoon")
else:
    engine.say("Good Evening")


engine.runAndWait()

