from modals import comments
from services import user_service
from dao import comments_dao
def get_comments(taskname):
    comments_list=[]
    r=comments_dao.get_comments(taskname)
    res=r.fetch_row(maxrows=0)
    return res

def add_comment(comment_detail):
    print comment_detail['commentText']
    comment=comments.Comments
    comment.text=comment_detail['commentText']
    comment.username=comment_detail['username']
    comments_dao.add_comment(comment)


