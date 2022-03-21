import math
from datetime import date

def tireVolume (w,a,d):
    calculation = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
    return calculation

user_width = int(input("Enter the width of the tire in mm (ex 205): "))
user_radio = int(input("Enter the aspect ratio of the tire (ex 60): "))
user_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

result = tireVolume(user_width,user_radio,user_diameter)

print(f'The aproximate volume is {result:.2f} liters ')

datetime_obj = date.today()


with open("volumes.txt", "at") as f:
    print(f'{datetime_obj},{user_width}, {user_radio}, {user_diameter}, {result:.2f}', file=f)




