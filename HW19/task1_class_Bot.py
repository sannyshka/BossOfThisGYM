class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(self.name)


bot = Bot("Jarvis")
bot.say_name()
bot.send_message("Hi, mister Stark")
