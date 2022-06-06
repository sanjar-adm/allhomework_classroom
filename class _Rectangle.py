class  Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Площадь:{self.length * self.width}")

    def perimetr(self):
        print(f"Периметр:{2* (self.length + self.width)}")


    def set_x_y(self,new_x,new_y):
        self.length = new_x
        self.width = new_y

    def get_x_y(self,):
        print(self.length,self.width)

x_y = Rectangle(10,5)
x_y.get_x_y()
x_y.set_x_y(40,6)
x_y.get_x_y()
x_y.perimetr()
x_y.area()
