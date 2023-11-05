import speech_recognition 
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    print('Robot: ...')

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print('You: ', you)

    if you == '':
        robot_brain = "I can't hear you, try again"
    elif 'hello' in you:
        robot_brain = 'Xin chào ngài bơ tơ Trần'
    elif 'today' in you:
        today = date.today()

        d2 = today.strftime("%B %d, %Y")
        robot_brain = d2
    elif 'time' in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif 'millionar' in you:
        robot_brain = 'ngài bơ tơ Trần'
        print('Robot:', robot_brain) 
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

        break
    elif 'bye' in you:
        robot_brain = 'Bye ngài bơ tơ Trần'
    else:
        robot_brain = "I'm fine thank you and you"

    print('Robot:', robot_brain) 

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
