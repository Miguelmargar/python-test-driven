from byotest import * #star means import everthing we could have put the name of the function only

eur_coins = [200, 100, 50, 20, 10, 5, 2, 1]
usd_coins = [25, 10, 5, 1]

def get_change(amount, coins=eur_coins):
    change = []
    for coin in coins:    
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change
    
test_are_equal(get_change(0), [])  
test_are_equal(get_change(1), [1])  
test_are_equal(get_change(2), [2])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(4), [2, 2])

test_are_equal(get_change(80, usd_coins), [25, 25, 25, 5])


print("All tests pass")

# Change the function so that instead of a list of coins, the function works with a dictionary that contains the coin denominations, and the quantity of each coin available. By default assume there are 20 of each coin, but this can be overridden by passing a dictionary to the function as with the previous example.
# If a coin that would normally be used to make change isn't available the program should attempt to use smaller coins to make up the change.
# If it is not possible to make the change with the coins available, the function should raise an error.

# to get the above change the list into a dictionary and give each list item a value of 20:
#     eur_coins = {200:20, 100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}
    
# then change the dictionary into a list with the .list() then arrange with the sort():
#     denominations = list(coins.keys())
#     denominations.sort(reverse=True)
    
# coins will have to be changed to denominations to make sure that the new list is taken into account