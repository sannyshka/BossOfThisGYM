Bot = type("Bot", (), {
    "__init__": lambda self, name: setattr(self, "name", name),
    "send_message": lambda self, message: print(message),
    "say_name": lambda self: print(self.name)
})


bot = Bot("Jarvis")
bot.say_name()
bot.send_message("Hi, mister Stark")
