# import pyttsx3
# import json
# from termcolor import colored

# from voice_settings.VoiceAssistant import VoiceAssistant

# class Translation:
#     """
#     Получение вшитого в приложение перевода строк для создания мультиязычного ассистента
#     """
#     with open("translations.json", "r", encoding="UTF-8") as file:
#         translations = json.load(file)

#     def get(self, text: str):
#         """
#         Получение перевода строки из файла на нужный язык (по его коду)
#         :param text: текст, который требуется перевести
#         :return: вшитый в приложение перевод текста
#         """
#         if text in self.translations:
#             return self.translations[text][assistant.speech_language]
#         else:
#             # в случае отсутствия перевода происходит вывод сообщения об этом в логах и возврат исходного текста
#             print(colored("Not translated phrase: {}".format(text), "red"))
#             return text


# def setup_assistant_voice(ttsEngine: pyttsx3.Engine, assistant: VoiceAssistant):
#     """
#     Установка голоса по умолчанию (индекс может меняться в 
#     зависимости от настроек операционной системы)
#     """
#     voices = ttsEngine.getProperty("voices")

#     if assistant.speech_language == "en":
#         assistant.recognition_language = "en-US"
#         if assistant.sex == "female":
#             # Microsoft Zira Desktop - English (United States)
#             ttsEngine.setProperty("voice", voices[1].id)
#         else:
#             # Microsoft David Desktop - English (United States)
#             ttsEngine.setProperty("voice", voices[2].id)
#     else:
#         assistant.recognition_language = "ru-RU"
#         # Microsoft Irina Desktop - Russian
#         ttsEngine.setProperty("voice", voices[0].id)