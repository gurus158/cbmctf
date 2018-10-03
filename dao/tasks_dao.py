import _mysql
import yaml
db_data = yaml.load(open('/home/root/flask_basic/static/db.yaml'))

db = _mysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'], passwd=db_data['password'],db=db_data['db'])


def getTaskId_By_task_name(task_name):
    query="select id from tasks where name='"+task_name+"'"
    db.query(query)
    return db.store_result()

def get_flag_points(taskname):
    query = "select flag,points from tasks where name='" + taskname + "'"
    db.query(query)
    r = (db.store_result()).fetch_row()
    return r

def get_task_details(taskname):
    query="select points,description,catagory from tasks where name='"+taskname+"'"
    db.query(query)
    return (db.store_result()).fetch_row()
