from modals import  users
from dao import user_dao
from dao import tasks_dao
def create_user(signup_detail):
    if signup_detail != None:
        user = users.User
        user.firstname = signup_detail['firstname']
        user.email = signup_detail['email']
        user.username = signup_detail['username']
        user.password = signup_detail['password']

        return user
    return None

def isempty(any_structure):
    if any_structure:
        return False
    else:
        return True

def get_userid(username):
    return (user_dao.get_userid_b_username(username)).fetch_row()

def signup_user(user):
    if user != None:
        return user_dao.signup_user(user)
    return None

def check_username(username):
    r=user_dao.get_user_by_username(username)
    return isempty(r.fetch_row())

def check_email(email):
    r=user_dao.get_user_by_email(email)
    return isempty(r.fetch_row())

def login_check(login_details):
    r=user_dao.get_user_by_username_password(login_details['username'],login_details['password'])
    return isempty(r.fetch_row())

def confirm_email(email):
    user_dao.confirm_email(email)

def check_task_name(task_name):
    r=(tasks_dao.getTaskId_By_task_name(task_name)).fetch_row()
    return isempty(r)

def submit_flag(username,user_flag,task_name):
    return user_dao.submit_flag(username,user_flag,task_name)

def already_solved(username,task_name):
    r=(tasks_dao.getTaskId_By_task_name(task_name)).fetch_row()
    task_ids=user_dao.get_task_ids(username)
    if task_ids[0][0]!= None:
        tl = task_ids[0][0].split(",")
        for t in tl:
            if t == r[0][0]:
                return True

    return False

def get_leaderboard():
    r=user_dao.get_leaderboard()
    return r.fetch_row(maxrows=0,how=1)
