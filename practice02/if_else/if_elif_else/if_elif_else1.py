marks = 95
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


day = "Monday"
if day == "Sunday":
    print("Holiday")
elif day == "Saturday":
    print("Weekend")
else:
    print("Working day")


speed = 120
if speed <= 60:
    print("Slow")
elif speed <= 100:
    print("Normal")
else:
    print("Fast")


number = 15
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by 3 and 5")
elif number % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3 or 5")


score = 10
if score >= 15:
    print("Level 3")
elif score >= 10:
    print("Level 2")
else:
    print("Level 1")


month = 12
if month == 12:
    print("December")
elif month == 1:
    print("January")
else:
    print("Another month")


time = 19
if time < 12:
    print("Morning")
elif time < 17:
    print("Evening")
else:
    print("Night")


# 3
score = 49
if score >= 30:
    print("Pass")
elif score <= 10:
    print("Fail")
else:
    print("Retake")


age = 15
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
