age=18
print(age==18)

answer=17
if answer != 42:
    print("That is not the correct answer. Please try again!")

print(age<21)
print(age<=21)
print(age>21)
print(age>=21)

age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
age_1=22
print((age_0>=21) and (age_1>=21))

age_1=22
age_0=18
print(age_0>=21 or age_1>=21)
age_1=18
print(age_1>=21 or age_0>=21)