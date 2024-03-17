

last_name='seo'
first_name='yongwon'
comment='bitcoin nasdaq fighting!'

print(f"{last_name.upper()} {first_name.lower()} {comment.title()} wowdoge")

test=' wowdoge '
print(test)
print(test.rstrip())
print(test.lstrip())
print(test.strip())
print(test.removeprefix(' wow'))
print(test.removesuffix('doge '))

test=3**3
print(f'"on python, we use power like this." + "3**3=" + {test}')

paduck=['tqqq','bulz','soxl','bitcoin']
print(f"I love {paduck[3].upper()}")
paduck.append('ethereum')
paduck.insert(0,'qld')
print(paduck)
paduck.remove("qld")
print(paduck.pop())
print(paduck)
print(sorted(paduck))
print(paduck)
paduck.sort()
print(paduck)
paduck.sort(reverse=True)
print(paduck)
paduck.reverse()
print(paduck)
print(len(paduck))

empty_list=[]

for asset in paduck:
    print(f"{asset} is good")
for value in range(1,5):
    print(value)
for value in range(1,10,2):
    empty_list.append(value)
    print(value)

print(f"{min(empty_list)}, {max(empty_list)}, {sum(empty_list)}")
print(empty_list[:3])
print(empty_list[2:])

friend_list=[]
good_friend_list=[]

friend_list=empty_list
good_friend_list=empty_list[:]

print(friend_list)
print(good_friend_list)
empty_list.append(100)
print(friend_list)
print(good_friend_list)

dimension=(1,2,3)
print(dimension)
demension=(4,5,6)
print(dimension)

paduck.insert(0,'nasdaq')

for asset in paduck:
    if asset=='bitcoin':
        print(asset.upper())
    elif asset=="nasdaq":
        print(asset.title())
    else:
        print(asset.lower())


print("complete chapter 1 from 5")
print("2023 10 22 Sunday")
print("in circle room, with discrete mathematics duo, hanmin, yeeun")