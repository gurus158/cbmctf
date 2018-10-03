class User:
    firstname = ''
    email = ''
    username = ''
    password = ''
    def __init__(self, firstname , email , username , password):
        self.firstname = firstname
        self.username = username
        self.email = email
        self.password = password

    @property
    def firstname(self):
        return self.firstname

    @property
    def email(self):
        return self.email

    @property
    def username(self):
        return self.username

    @property
    def password(self):
        return self.password

    @firstname.setter
    def firstname(self,firstname):
        if firstname != '':
            self.firstname = firstname

    @email.setter
    def email(self,email):
        if email != '':
            self.email = email

    @username.setter
    def username(self,username):
        if username != '':
            self.username = username

    @password.setter
    def password(self,password):
        if password != '':
            self.password = password