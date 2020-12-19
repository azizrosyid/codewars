class create_message(str):
    def __call__(self, s=""):
        if s == "":
            return create_message(self)
        return create_message(self+" " + s)


print(create_message("Hello")("World!")("how")("are")("you?")())
