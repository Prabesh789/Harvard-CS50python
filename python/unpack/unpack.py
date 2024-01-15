# unpacking the list
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
'''
Here, in line 7 * unpack the list of coins
'''


# unpack the dict
def total1(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts1")
'''
Here, in line 20 dict of coins is unpacked by ** 
'''
