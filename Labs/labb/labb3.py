from geometry_shapes import Circle
from geometry_shapes import Rectangle
cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)
rektangel = Rectangle(x=0,y=0,width=1, height=1)
print(cirkel1==cirkel2) # True
print(cirkel2==rektangel) # False
print(cirkel1.is_inside(0.5, 0.5)) # True
cirkel1.translate(5,5)
print(cirkel1.is_inside(0.5, 0.5)) # False
cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar