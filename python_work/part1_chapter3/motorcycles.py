motorcycles=['honda','yamada','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles[0]='honda'
motorcycles.append("ducati")
print(motorcycles)

motorcycles.insert(0,'kawasaki')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

poped_motorcycles=motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned}")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)
too_expensive='honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me. ")
