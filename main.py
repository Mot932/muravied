class Cell:
    def __init__(self, image='☐', Y=None, X=None):
        self.image = image
        self.Y = Y
        self.X = X

class Field:
    def __init__(self, rows=10, cols=25, cell=Cell):
        self.rows = rows
        self.cols = cols
        self.cell = cell().image  
 
    def drawcowsarows(self):
        for i in range(self.rows):
            row = [self.cell] * self.cols  
            print(*row)

MyClass = Field()
MyClass.drawcowsarows()