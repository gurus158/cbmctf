class Task:
    catagory=''
    points=0
    flag=''
    name=''
    user_ids=[]
    def __init__(self,catagory,points,flag,name,user_ids):
        self.catagory=catagory
        self.points=points
        self.name=name
        self.flag=flag
        self.user_ids=user_ids

    @property
    def catagory(self):
        return self.catagory

    @property
    def points(self):
        return self.points

    @property
    def flag(self):
        return self.flag

    @property
    def name(self):
        return self.name

    @property
    def user_ids(self):
        return self.user_ids

    @catagory.setter
    def catagory(self,catagory):
        if catagory !='':
            self.catagory=catagory

    @points.setter
    def points(self,points):
        if points != None:
            self.points=points

    @flag.setter
    def flag(self,flag):
        if flag!='':
            self.flag=flag

    @name.setter
    def name(self,name):
        if name!='':
            self.name=name

    @user_ids.setter
    def user_ids(self,user_ids):
        if user_ids!=None:
            self.user_ids=user_ids


