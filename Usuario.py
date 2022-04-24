class Usuario():
    def __init__(self, id_user, user_display_name, user_nickname,user_password,user_age,user_career,user_carnet):
        self.id_user= id_user
        self.user_display_name= user_display_name
        self.user_nickname= user_nickname
        self.user_password= user_password
        self.user_age= user_age
        self.user_career= user_career
        self.user_carnet= user_carnet

    def getid_user(self):
        return self.id_user

    def getuser_display_name(self):
        return self.user_display_name

    def getuser_nickname(self):
        return self.user_nickname

    def getuser_password(self):
        return self.user_password

    def getuser_age(self):
        return self.user_age

    def getuser_career(self):
        return self.user_career
    
    def getuser_carnet(self):
        return self.user_carnet

    def setid_user(self, id_user):
        self.id_user=id_user

    def setuser_display_name(self, user_display_name):
        self.user_display_name=user_display_name

    def setuser_nickname(self,user_nickname):
        self.user_nickname=user_nickname

    def setuser_password(self,user_password):
        self.user_password=user_password

    def  setuser_age(self,user_age):
        self.user_age=user_age

    def setuser_career(self,user_career):
        self.user_career=user_career

    def setgetuser_carnet(self, getuser_carnet):
        self.getuser_carnet=getuser_carnet