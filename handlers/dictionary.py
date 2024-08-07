import random
import webbrowser
from googlesearch import search
import traceback
import pyttsx3

from owner.person import Person
from assistant.speech import play_speech
from voice_settings.VoiceAssistant import VoiceAssistant


# Инициализация мастера ассистента
person = Person("Данила", 23, "Екатеринбург")

# Инструмент вывода голоса
ttsEngine = pyttsx3.init()

# настройка данных голосового помощника
assistant = VoiceAssistant("Alice", "female", "ru")

def execute_command(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    for key in command.keys():
        if command_name in key:
            command[key](*args)
        else:
            pass  # print("Command not found")


def play_greetings(*args: tuple):
    """
    Проигрывание случайной приветственной речи
    """
    greetings = [
        f"Здравствуйте!, {person.name}! Чем я могу Вам помочь?",
        f"Доброго дня, {person.name}! Чем я могу Вам помочь?"
    ]
    play_speech(ttsEngine, greetings[random.randint(0, len(greetings) - 1)])


def play_farewell_and_quit(*args: tuple):
    """
    Проигрывание прощательной речи и выход
    """
    farewells = [
        f"До свидания, {person.name}! Хорошего Вам дня!",
        f"Всего доброго, {person.name}!"
    ]
    play_speech(ttsEngine,farewells[random.randint(0, len(farewells) - 1)])
    ttsEngine.stop()
    quit()


def search_for_term_on_google(*args: tuple):
    """
    Поиск в Google с автоматическим открытием ссылок (на список результатов и на сами результаты, если возможно)
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)

    # альтернативный поиск с автоматическим открытием ссылок на результаты (в некоторых случаях может быть небезопасно)
    search_results = []
    try:
        for _ in search(search_term,  # что искать
                        tld="com",  # верхнеуровневый домен
                        lang=assistant.speech_language,  # используется язык, на котором говорит ассистент
                        num=1,  # количество результатов на странице
                        start=0,  # индекс первого извлекаемого результата
                        stop=1,  # индекс последнего извлекаемого результата (я хочу, чтобы открывался первый результат)
                        pause=1.0,  # задержка между HTTP-запросами
                        ):
            search_results.append(_)
            webbrowser.get().open(_)

    # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
    except:
        play_speech(f"Похоже возникла ошибка. Подробнее в логах")
        traceback.print_exc()
        return

    print(search_results)
    play_speech(ttsEngine, f"Вот что я нашел по запросу {search_term} в google")


def search_for_video_on_youtube(*args: tuple):
    """
    Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    play_speech(ttsEngine, f"Вот что я нашел по запросу {search_term} в youtube")


command = {
    ("hello", "hi", "morning", "привет"): play_greetings,
    ("bye", "goodbye", "quit", "exit", "stop", "пока"): play_farewell_and_quit,
    ("search", "google", "find", "найди"): search_for_term_on_google,
    ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    #("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    #("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
    #("language", "язык"): change_language,
    #("weather", "forecast", "погода", "прогноз"): get_weather_forecast,
}