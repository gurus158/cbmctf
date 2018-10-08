import _mysql
import yaml
db_data = yaml.load(open('/home/root/flask_basic/static/db.yaml'))

db = _mysql.connect(host=db_data['host'], port=db_data['port'], user=db_data['user'], passwd=db_data['password'],db=db_data['db'])

def get_video_details(video_name):
    if video_name is not  None:
        query = "select url,name,description from videos where name='" + video_name + "'"
        db.query(query)
        r = (db.store_result()).fetch_row()
        return r
    return None

def get_video_list():
    query = "select name from videos"
    db.query(query)
    r = (db.store_result()).fetch_row(maxrows=0)
    return r

