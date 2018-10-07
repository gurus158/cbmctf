class Forgot_pass:
    token=''
    email=''
    used=0

    def __init__(self,token,email,used):
        self.token = token
        self.email = email
        self.used = used

    @property
    def token(self):
        return self.token

    @property
    def email(self):
        return self.email

    @property
    def used(self):
        return self.used

    @token.setter
    def token(self,token):
        if token != None:
            self.token = token

    @email.setter
    def email(self,email):
        if email != None:
            self.email = email

    @used.setter
    def used(self,used):
        if used != None:
            self.used = used

