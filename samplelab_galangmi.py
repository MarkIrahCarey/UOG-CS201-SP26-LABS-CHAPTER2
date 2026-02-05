"""
Author: Mark Ira
Date: 2/5/26
FileName: samplelab_galangmi.py
Purpose: What the program is about
"""

mass_coef = float(input("Coefficent of object mass: "))
mass_power = int(input("Power of mass: "))

mass = mass_coef * 10 ** mass_power
print ("Mass:", mass)

radius_coef = float(input("Coefficent of object radius: "))
radius_power = int(input("Power of radius: "))
radius = radius_coef * 10 ** radius_power
print ("Radius", radius)

GRAVITATIONAL_CONSTANT = 6.674 * 10 ** (-11)

# round(5.4) -> 5
# round(#, #), round (4.5691, 2) -> 4.57
gravity = round((GRAVITATIONAL_CONSTANT * mass) / (radius ** 2), 1)

print ("Gravity:", gravity, "m/s^2")

# Saturn's gravity, 11.2
# Sun's gravity: 274