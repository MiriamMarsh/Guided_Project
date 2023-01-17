class Family_Member:
    def __init__(self, fname, age, is_parent):
        self.first_name = fname
        self.age = age
        self.is_parent = is_parent

    @property
    def is_parent(self):
        return self. _is_parent

    @is_parent.setter
    def parent_age(self,value):
        if self.age > 20 and value == True:
            self.is_parent= True
        else:
            self._is_parent = False



