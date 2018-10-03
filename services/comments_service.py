from modals import comments
from services import tasks_service
from dao import comments_dao
def get_comments(taskname):
    comments_list=[]
    r=comments_dao.get_comments(taskname)
    res=r.fetch_row(maxrows=0)
    return res

def add_comment(comment_detail):

    comment = comments.Comments
    chars=set('/<>\\')
    if any((c in chars) for c in comment_detail['text']):
        return "False"

    if comment_detail['text'] != "":
        comment.text = str(comment_detail['text'])
    else:
        comment.text="cbm is cool"

    comment.username=str(comment_detail['username'])
    taskid=(tasks_service.get_taskid(taskname=comment_detail['taskname']))[0][0]
    comment.taskid=taskid
    comments_dao.add_comment(comment)
    return "True"


