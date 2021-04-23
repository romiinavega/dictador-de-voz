import speech_recognition as sr
r= sr.Recognizer()
import time
import webbrowser

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data =''
        try:
            voice_data =r.recognize_google(audio)
        
        except sr.UnknownValueError:
            print('Lo siento no te entiendo')
        except sr.RequestError:
            print('Lo siento, error de conexion')
        return voice_data

def respond(voice_data):
    if 'nombre' in voice_data:
        print('Mi nombre es alexis')
    if 'hora' in voice_data:
        print(time.ctime())
    if 'saludo' in voice_data:
        print('Hola, que tengas buen dia')
    if 'adios' in voice_data:
        print('Hasta luego')
    if 'buscar' in voice_data:
        buscar = record_audio('¿que necesitas buscar?')
        url= 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('esto es lo que encontre para:'+buscar)
    if 'lugar' in voice_data:
        lugar = record_audio("¿Que lugar?")
        url='https://google.nl/maps/place/'+lugar +'/&amp;'
        print('Esto es lo que encontre para '+lugar)

time.sleep(1)
print('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
#print(voice_data)