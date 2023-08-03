cars=['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car='bmw'
print(car=='BMW')
print(car.upper()=='BMW')
#upper method does not effect to variable
print(car)
