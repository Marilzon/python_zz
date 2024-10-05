class Username:
    description_username = "this is a user:"

    def __init__(self, name, surname) -> str:
        self.name = name
        self.surname = surname

    def fullname(self):
        self.fullname = f"{self.name} {self.surname}"
        return f"{self.description_username} {self.fullname}"

monza = Username("chevrolet", "monza")
audio = Username("audi", "C4")

print(monza.fullname())
print(audio.fullname())
