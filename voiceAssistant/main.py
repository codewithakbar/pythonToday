import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'play_music': ['включить музыку', 'дискотека']
    }
}


def listen_command():
    """The function will return the recognized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        
        return query
    except speech_recognition.UnknownValueError:
        return f"Hmmm... Nima dedingiz chunmadim :/"



def greeting():
    """Greeting function"""

    return "Salom Jora"


def create_task():
    """Creating todo task"""

    print(f"TODO listga nimalarni qoshamiz?")

    query = listen_command()
        
    with open('todo-list.txt', 'a', encoding='utf8') as file:
        file.write(f"!!! {query}\n")
    
    return f"{query} TODO listga buyruklar qoshildi!!!"
    

def play_music():
    """Play a random music"""

    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'xdg-open {random_file}')

    return f'Hozirgi sound {random_file.split("/")[-1]} 🔉🔉🔉'


def main():
    query = listen_command()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())




if __name__ == '__main__':
    main()


