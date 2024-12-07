from wr import lang
import time, random, os
import speech_recognition as sp

languages = {'frances':'fr-FR','portugues':'pt-BR','ingles':'en-GB','italiano':'it-IT'}
levels = ['facil','intermedio','dificil']

def speech(lang_code):
    mic = sp.Microphone()
    recog = sp.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        try:
            return recog.recognize_google(audio, lang_code)
        except sp.exceptions.UnknownValueError:
            return
        except sp.RequestError:
            return



def playGame(language,level,lang_code):
    score = 0
    retry = False
    list = lang(language)[level]
    for i in range(len(list)):
        if not retry:
            word= random.choice(list)
        else:
            retry = False
        print(f"intenta decir: {word}...")
        output= speech(lang_code)
        if output == word:
            score += 1
            print('bien hecho')
            list.remove(word)
            time.sleep(1.25)
        elif output == None:
            print('no se reconocio la voz')
            retry = True
            i -= 1
            continue
        else:
            print('incorrecto...')
            list.remove(word)
            time.sleep(1.25)
            os.system('cls')
    return score

def menu():
    a = '-\n'.join(languages.keys())
    b = '-\n'.join(levels)
    language = input(f'{a}\n seleccione un idioma: ')
    while language not in languages.keys():
        os.system('cls')
        language = input(f'{a}\nlenguaje no valido seleccione uno de la lista: ')
    lang_code= languages[language]
    level = input(f'{b}\n seleccione un nivel de dificultad: ')
    while level not in levels:
        os.system('cls')
        level = input(f'{a}\nlenguaje no valido seleccione uno de la lista: ')
    score = playGame(language,level,lang_code)
    print(f'tu puntuacion fue de: {score}')

print("pronounce game")
time.sleep(1)
os.system('cls')

while True:
    menu()
    while True:
        replay= input('quieres jugar otra vez y/n:')
        if replay == 'y':
            os.system('cls')
            menu()
            continue
        elif replay == 'n':
            break
        else:
            print('opcion no valida')
            time.sleep(0.75)
            os.system('cls')
            continue
    break