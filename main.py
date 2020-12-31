import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

intro = 'Hi! I\'m Cooly, your personal assistant. Ask me anything you want.'


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk(intro)


def do():
    try:
        with sr.Microphone() as source:
            engine.say('What can I do for you?')
            engine.runAndWait()
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            talk(f'Ok looking for {command}')
            print(command)
            if 'coolie | coolly' in command:
                command = command.replace('coolie | coolly', '')

    except:
        talk('Can you say that again?')
      if command == '':
        pass
      else:
        return command


def run():
    command = do()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Ok, Playing {song}')
        print(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'The time right now is{time}')
    elif 'wikipedia' in command:
        command = command.replace('wikipedia', '')
        info = wikipedia.summary(command, 5)
        print(info)
        tosay = wikipedia.summary(command, 1)
        talk(tosay)
    elif 'thanks' in command:
        talk('It was my pleasure to help you.')
    elif 'thank' in command:
        talk('It was my pleasure to help you.')
    elif 'boss' in command:
        say = 'Mohammed Mubashir Hasan is my boss. He is awesome.'
        talk(say)
    elif 'owner' in command:
        say = 'Mohammed Mubashir Hasan is my boss. He is awesome.'
        talk(say)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'jokes' in command:
        jokes = pyjokes.get_jokes()
        print(jokes)
        talk(jokes)

    else:
        info = wikipedia.search(command)
        print(info)
        pywhatkit.search(command)


while True:
    run()
