import _mysql
import yaml
from dao import tasks_dao
from modals import comments
db_data = yaml.load(open('/home/root/flask_basic/static/db.yaml'))

db = _mysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'], passwd=db_data['password'],db=db_data['db'])


def get_comments(taskname):
    t=tasks_dao.getTaskId_By_task_name(taskname)
    tid=t.fetch_row()
    query="select username,taskid,text,created from comments where taskid="+tid[0][0]
    db.query(query)
    r=db.store_result()
    return r

def add_comment(comment):
    print comment.username
    if comment!=None:
        query = "insert into comments(username,text) values('" + comment.username + "','" + comment.text + "')"
        db.query(query)
