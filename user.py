import re
class User:
    users = []  

    def __init__(self,name,age,username,email,password,gender):
        self.name = name 
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        self.gender = gender
        self.users = []


    def register_user(self):
           user =list (
                    name=self.name,
                    username=self.username,
                    email=self.email,
                    password=self.password,
                    age=self.age
            )

    def check_password(self):

        if len(input("password")) >= 4:
            return True
        return False

        if re.search(r"[a-z]",input("password")):
            return True
        return False
        if re.search(r"[A-Z]", input("password")):
            return True
        return False

        if re.search(r"[0-9]",input("password")):
            return True
        return False

        if re.search(r"[@!#$%^&*()_+=|?/\-~}{;:.<>,]",
                     input("password")):
            return True
        return False
