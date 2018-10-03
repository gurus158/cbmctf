from modals import tasks
from dao import tasks_dao

def create_task(task_detail):
    if task_detail!=None:
        task=tasks.Task
        task.catagory=task_detail['catagory']
        task.points=task_detail['points']
        task.name=task_detail['name']
        task.flag=task_detail['flag']
        task.user_ids=task_detail['user_ids']
        return task
    return None

def isempty(any_structure):
    if any_structure:
        return False
    else:
        return True

def get_task_details(taskname):
    r=tasks_dao.get_task_details(taskname)
    return r

