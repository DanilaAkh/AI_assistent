class VoiceAssistant():
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""

    def __init__(self, name: str, sex: str, speech_language: str="ru", recognition_language: str="ru"):
        self.name = name
        self.sex = sex
        self.speech_language = speech_language
        self.recognition_language = recognition_language