class Rectangle():

    def __init__(self , l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width
    
newractangle = Rectangle(20, 40)

print("Dimension of rectangle - Lenght : %d, Width : %d" %(newractangle.length,newractangle.width))

print("Area of Rectangle :", newractangle.rectangle_area())