numbers=list(range(1,21))
for number in numbers:
    print(number)

to_million=list(range(1,10001))
#print(to_million)
print(min(to_million))
print(max(to_million))
print(sum(to_million))

odd=list(range(1,20,2))
for number in odd:
    print(number)

threes=list(range(3,31,3))
for number in threes:
    print(number)

cubes=[]
for number in range(1,11):
    cubes.append(number**3)
for cube in cubes:
    print(cube)

cubes=[value**3 for value in range(1,11)]
print(cubes)