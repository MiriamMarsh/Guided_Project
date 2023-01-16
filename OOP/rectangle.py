class Rectangle:

    def __init__ (self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self,value):
        self.length = value
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self,value):
        self.width=value
