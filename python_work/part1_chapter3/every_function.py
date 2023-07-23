stocks=['apple', 'sk hynix', 'samsung electroics', 'nivida', 'amd', 'tesla', 'bitcion']
new_list=sorted(stocks)
print(stocks)
print(new_list)
new_list.reverse()
print(new_list)
print(stocks[0])
stocks.insert(0,'tqqq')
stocks.append('soxl')
print(stocks)
del stocks[4]
print(stocks)
last_one=stocks.pop()
print(last_one)
target='amd'
stocks.remove(target)
print(stocks)
length=len(stocks)
print(f"The number of list is {length}")