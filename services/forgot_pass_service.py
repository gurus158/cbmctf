from modals import forgot_pass
from dao import forgot_pass_dao

def isempty(any_structure):
    if any_structure:
        return False
    else:
        return True

def is_token_used(token):
    r = forgot_pass_dao.is_token_used(token)
    print r
    if isempty(r):
        return True
    elif  r[0][0] == 0:
         return True
    else:
        return False

def add_token_mail(token,email):
    if token is not None and email is not None:
        forgot_pass_dao.add_token_mail(token, email)

def set_token_used(token):
    if token is not None:
        forgot_pass_dao.set_token_used(token)

def get_email(token):
    if token is not None:
        r=forgot_pass_dao.get_email(token)
        return r[0][0]

def delete_row(email):
    if email is not  None:
        forgot_pass_dao.delete_row(email)
