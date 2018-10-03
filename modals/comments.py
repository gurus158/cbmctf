class Comments:
    username='kid0cool'
    taskid=0
    text='cbm is awesome'

    def __init__(self,username,taskid,text):
        self.username=username
        self.taskid=taskid
        self.text=text

    @property
    def username(self):
        return self.username

    @property
    def taskid(self):
        return self.taskid
    @property
    def text(self):
        return self.text

    @taskid.setter
    def taskid(self,taskid):
        if taskid != None:
            self.taskid = taskid

    @username.setter
    def username(self,username):
        if username != None:
            self.userid=username

    @text.setter
    def text(self,text):
        if text != None:
            self.text=text




