"""When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
def user_age (age):
    result = 220 - age
    return result

def max_rate (age):
    result = age * 0.85 
    return result

def min_rate (age):
    result = age * 0.65
    return result

user_input = int(input("Please enter your age: "))
result_one = user_age(user_input)
result_two = max_rate(result_one)
result_three = min_rate(result_one)

print()
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {result_three:.0f} and {result_two:.0f} beats per minute.')