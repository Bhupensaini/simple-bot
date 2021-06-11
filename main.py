import wikipedia
import pyttsx3
import datetime
import json
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak("Good Morning")

	elif hour >= 12 and hour <= 18:
		speak("Good Afternoon")

	else:
		speak("Good Evening")

	speak("I am friday. How may I help You?")


# data = json.loads(commands)
# print(data)

if __name__ == "__main__":
	wishMe()
	while True:
		cmd = input(">> ")
		if cmd == "quit":
			break

		elif 'who is' in cmd:
			speak("...please wait")
			cmd = cmd.replace("who is","")
			results = wikipedia.summary(cmd, sentences=3)
			speak(results)

# 		elif 'open youtube' in cmd:
			
