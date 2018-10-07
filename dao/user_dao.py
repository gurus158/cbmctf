import _mysql
import yaml
from dao import  tasks_dao
db_data = yaml.load(open('/home/root/flask_basic/static/db.yaml'))

db = _mysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'], passwd=db_data['password'],db=db_data['db'])


def isempty(any_structure):
    if any_structure:
        return False
    else:
        return True

def signup_user(user):
    if user != None:
        firstname = user.firstname
        email = user.email
        username = user.username
        password = user.password
        query="insert into users(firstname , email , username , password ) values('"+firstname+"','"+email+"','"+username+"','"+password+"')"
        db.query(query)


def get_user_by_username(username):
    query="select * from users where username = '"+ username+"'"
    db.query(str(query))
    r=db.store_result()
    return r
def get_userid_b_username(username):
    query="select id from users where username='"+username+"'"
    db.query(query)
    return db.store_result()

def get_user_by_email(email):
    query = "select * from users where email = '" + email+"'"
    db.query(str(query))
    r=db.store_result()
    return r

def get_user_by_username_password(username,password):
    query="select * from users where username = '"+username+"' and password= '"+password+"'"
    db.query(str(query))
    r=db.store_result()
    return r

def confirm_email(email):
    query = "update users set email_confirmed = 1 where email='"+email+"'"
    db.query(query)


def add_points(username,points):
    query="select points from users where username='"+username+"'"
    db.query(query)
    r=(db.store_result()).fetch_row()

    if r[0][0]==None:
        cp=0
    else:
        cp = int(r[0][0])

    if cp != 0:
        tp=points+cp

        query="update users set points="+str(tp)+" where username='"+username+"'"
        db.query(query)
    else:
        tp=points
        query = "update users set points=" + str(tp) + " where username='" + username + "'"
        db.query(query)


def submit_flag(username,user_flag,task_name):
    r=tasks_dao.get_flag_points(task_name)
    flag=r[0][0]

    if flag==user_flag:
        add_points(username,int(r[0][1]))
        r=(get_task_ids(username))
        tid=tasks_dao.getTaskId_By_task_name(task_name)
        t=tid.fetch_row()
        if isempty(r):
            new_task_ids=str(t[0][0])
        else:
            new_task_ids=str(r[0][0])+","+str(t[0][0])
        query = "update users set task_ids='" + new_task_ids + "'"+" where username='"+username+"'"
        db.query(query)
        update_rank(username)
        return True
    else:
        return False

def get_task_ids(username):
    query = "select task_ids from users where username='" + username + "'"
    db.query(query)
    return (db.store_result()).fetch_row()

def get_leaderboard():
    query = "select username,points from users order by points desc"
    db.query(query)
    return db.store_result()

def update_rank(username):
    r = get_leaderboard()
    lb = r.fetch_row(maxrows=0)
    i = 1
    a = False
    for u in lb:
        if u[0]==username:
            a = True
        if a:
            query = "update users set rank=" + str(i) + " where username='" + u[0] + "'"
            db.query(query)

        i = i+1


def set_passwd(passwd,username):
    if passwd is not  None:
        query = "update users set password='" + passwd + "' where username='" + username +"'"
        print  query
        db.query(query)

def get_username_by_email(email):
    if email is not  None:
        query = "select username from users where email = '" + email + "'"
        db.query(query)
        return (db.store_result()).fetch_row()
