from pprint import pprint


class Profile():
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }
    def set_profile(self,profile):
        self.profile = profile
    def get_name(self):
        return self.profile["name"]
    def get_gender(self):
        return self.profile["gender"]
    def get_birthday(self):
        return self.profile["birthday"]
    def get_age(self):
        return self.profile["age"]
    def get_phone(self):
        return self.profile["phone"]
    def get_email(self):
        return self.profile["email"]

profile = Profile()
profile.set_profile({
    "name": "Kim",
    "gender": "man",
    "birthday": "06/09",
    "age": 28,
    "phone": "01012341234",
    "email": "python@sparta.com",
})

print(profile.get_name())
print(profile.get_gender())
print(profile.get_birthday())
print(profile.get_age())
print(profile.get_phone())
