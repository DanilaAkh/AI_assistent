import speech_recognition as sprc
import os
import pyttsx3
import json
import vosk
from voice_settings.VoiceAssistant import VoiceAssistant

from commands.dictionary import commands
import random
import webbrowser




def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")


def record_n_recognize(*args: tuple):
    """
    Запись и распознование аудио
    """
    with micro:
        recognize_data = ""

        recognizer.adjust_for_ambient_noise(micro, duration=1)
        try:
            print("Listening...")
            audio = recognizer.listen(micro, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
        
        except sprc.WaitTimeoutError:
            print("Check your micro")
            return
        
        try:
            print("Starting recognition...")
            recognize_data = recognizer.recognize_vosk(audio, language='ru')
            recognize_data = json.loads(recognize_data)
        except sprc.UnknownValueError:
            print("Sorry, speech service is unavailable. Try again later")

        return recognize_data["text"]



if __name__ == "__main__":

    vosk.SetLogLevel(-1)

    # инициализация инструментов распознавания и ввода речи
    recognizer = sprc.Recognizer()
    micro = sprc.Microphone(1)

    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant("Alice", "female", "ru")

    # for index, name in enumerate(sprc.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    print("device_index", micro.device_index)
    while True:
        voice_input = record_n_recognize()
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]

        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command, command_options)