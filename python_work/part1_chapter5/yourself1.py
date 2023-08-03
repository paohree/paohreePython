coins=['bitcoin', 'ethereum','solana','doge']
print("Let's check True or False")
input="doge"
for coin in coins:
    print(f"Is it {coin}?")
    if coin == input:
        print(f"Yes, this is {coin}")
    else:
        print(f"No, this is not {coin}")
print("wowdoge!")