# 1․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։

import math
from abc import ABC, abstractmethod
class Shape():
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


# 2․ Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։

class Circle(Shape):
    def __init__(self, r):
        if not self.validate_r(r):
            raise ValueError ('Radius should be a positive number')
        self.r = r
    
    @staticmethod
    def validate_r(radius: int|float) -> bool:
        return radius > 0
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r ** 2


# 3․ Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։

class Rectangle(Shape):
    def __init__(self, a, b):
        if not (self.validate_a(a) and self.validate_b(b)):
            raise ValueError ('The sides must be positive numbers')
        self.a = a
        self.b = b

    @staticmethod
    def validate_a(a_side: int|float) -> bool:
        return a_side > 0

    @staticmethod
    def validate_b(b_side: int|float) -> bool:
        return b_side > 0
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b
    

# 4․ Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի 
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։

class Triangle(Shape):
    def __init__(self, a=None, b=None, c=None, h=None, alpha=None):
        if a != None and b != None and c != None:
            if not (self.validate_a(a) and self.validate_b(b) and self.validate_c(c)):
                raise ValueError('Wrong parameter')
        elif a != None and h != None:
            if not (self.validate_a(a) and self.validate_h(h)):
                raise ValueError('Wrong parameter')
        elif not a != None and b != None and alpha != None:
                if not (self.validate_a(a) and self.validate_b(b) and self.validate_alpha(alpha)):
                    raise ValueError('Wrong parameter')
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.alpha = alpha

    @staticmethod
    def validate_a(a_side: int|float) -> bool:
        return a_side > 0

    @staticmethod
    def validate_b(b_side: int|float) -> bool:
        return b_side > 0

    @staticmethod
    def validate_c(c_side: int|float) -> bool:
        return c_side > 0

    @staticmethod
    def validate_h(height: int|float) -> bool:
        return height > 0

    @staticmethod
    def validate_alpha(angle_alpha: int|float) -> bool:
        return angle_alpha > 0

    def perimeter(self):
        if self.a != None and self.b != None and self.c != None:
            return self.a + self.b + self.c
        elif self.a != None and self.h != None:
            pass
        elif self.a != None and self.b != None and self.alpha != None:
            self.c = (self.a ** 2 + self.b ** 2 - 2 * self.a * self.b * math.cos(self.alpha)) ** 0.5
            return self.a + self.b + self.c
        else:
            raise Exception('Unknown')

    def area(self):
        if self.a != None and self.b != None and self.c != None:
            p = self.perimeter() / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        elif self.a != None and self.h != None:
            return self.a * self.h / 2
        elif self.a != None and self.b != None and self.alpha != None:
            return self.a * self.b * math.sin(self.alpha) / 2
        else:
            raise Exception('Unknown')


circle_1 = Circle(2)
circle_2 = Circle(3)
rectangle_1 = Rectangle(2, 3)
rectangle_2 = Rectangle(4, 5)
triangle_1 = Triangle(a=3, b=3, c=5)
triangle_2 = Triangle(a=4, b=5, alpha=0.785)
triangle_3 = Triangle(a=4, h=3)

calc = (circle_1, circle_2, rectangle_1, rectangle_2, triangle_1, triangle_2, triangle_3)

for i in calc:
    print(f'area = {i.area()}')
    print(f'perimeter = {i.perimeter()}')






