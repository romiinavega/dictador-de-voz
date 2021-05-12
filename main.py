import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, intenta de nuevo')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexión')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang="es")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'Tiempo' in voice_data:
        alexa_speak('Las elecciones en Mexico seran el 6 de junio de 2021')
    if 'Cargos'in voice_data:
        alexa_speak('Este año se elegirán 500 cargos federales y 19 mil 915 de carácter local.')
    if 'Busqueda' in voice_data:
        buscar = record_audio('Que quieres buscar mas especificamente?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto es lo que encontre para: ' + buscar)
    if 'Nacional' in voice_data:
        alexa_speak('A nivel nacional, se elegirán 15 gubernaturas de los estados: Baja California, Baja California Sur, Sonora, Chihuahua, Sinaloa, Zacatecas, San Luis Potosí, Nayarit, Querétaro, Colima, Michoacán, Guerrero, Campeche, Tlaxcala y Nuevo León.')
    if 'Loca' in voice_data:
        alexa_speak('A nivel local, se eligen mil 923 presidencias municipales, 14 mil 222 regidurías, 2 mil 057 sindicaturas, 204 concejalías, 431 juntas municipales y presidencias de comunidad, 642 diputados por mayoría relativa del Congreso y 421 legisladores locales de representación proporcional.')
    if 'Extranjero' in voice_data:
        alexa_speak('10 mil 992 ciudadanos residentes en el extranjero se han registrado en el INE para participar en las elecciones 2021')  
    if 'Casillas' in voice_data:
        alexa_speak(' En todo el país, el INE instalará 163 mil 244 casillas para que los mexicanos acudan a ejercer su derecho al voto.')  
    if 'Dinero' in voice_data:
        alexa_speak('El Instituto Nacional Electoral destinó un total de 7 mil 226 millones 003 mil 636 para financiamiento de los partidos políticos nacionales durante el año electoral. ')    
    if 'Partidos' in voice_data:
        alexa_speak('Partido Acción Nacional, Partido Revolucionario Institucional, Partido de la Revolución Democrática, Partido del Trabajo, Partido Verde Ecologista de México, Movimiento Ciudadano, Movimiento Regeneración Nacional, Partido Encuentro Solidario, Fuerza por México, Redes Sociales Progresistas. ')    
    if 'Gracias' in voice_data:
        exit()
    if 'Bai' in voice_data:
        exit()


time.sleep(1)
alexa_speak('Bienvenido a tu asistente, aqui podras obtener informacion sobre la politica en Mexico. ¿Que necesitas saber?')
while 1:
    voice_data = record_audio()
    respond(voice_data)    