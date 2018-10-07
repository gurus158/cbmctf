import _mysql
import yaml
db_data = yaml.load(open('/home/root/flask_basic/static/db.yaml'))

db = _mysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'], passwd=db_data['password'],db=db_data['db'])

def is_token_used(token):
    query = "select used from forgot_pass where token = '" + token + "'"
    db.query(query)
    return (db.store_result()).fetch_row()

def add_token_mail(token,email):
    if token is not None and email is not None:
        query = "insert into forgot_pass(token,email) values('" + token + "','" + email + "')"
        db.query(query)

def set_token_used(token):
    if token is not  None:
        query = "update forgot_pass set used = 1 where token = '" + token + "'"
        db.query(query)

def get_email(token):
    if token is not  None:
        query = "select email from forgot_pass where token='" + token + "'"
        db.query(query)
        return (db.store_result()).fetch_row()

def delete_row(email):
    if email is not  None:
        query = "delete from forgot_pass where email = '" + email + "'"
        db.query(query)
