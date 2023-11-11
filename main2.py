class Cell:
    def __init__(self, image='▢', Y=None, X=None):
        self.image = image
        self.Y = Y
        self.X = X

class Field:
    def __init__(self, rows=10, cols=25, cell=Cell):
        self.rows = rows
        self.cols = cols
        self.cell = [[cell(Y=y, X=x) for x in range(cols)] for y in range(rows)]

    def drawrows(self):
        for row in self.cell:
            row_images = [cell.image for cell in row]
            print(*row_images)

MyClass = Field()
MyClass.cell
MyClass.drawrows()
