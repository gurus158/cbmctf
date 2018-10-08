class Video:
    url=''
    name=''
    description=''

    def __init__(self,url,name,description):
        self.url = url
        self.name = name
        self.description = description

    @property
    def url(self):
        return self.url

    @property
    def name(self):
        return self.name

    @property
    def description(self):
        return self.description

    @url.setter
    def url(self,url):
        self.url = url

    @name.setter
    def name(self,name):
        self.name = name

    @description.setter
    def description(self,description):
        self.description = description
