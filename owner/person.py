class Person():
    name = ''
    age = 0
    city = "Moskow"
    lang = "ru"
    def __init__(self, name, age, city, lang="ru"):
        self.name = name
        self.age = age
        self.city = city
        self.lang = lang