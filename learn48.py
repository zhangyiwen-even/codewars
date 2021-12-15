'''
Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. 
For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:
1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:
1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.
Your function should take an amount to change and an array of unique denominations for the coins:
  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0
编写一个函数，计算在给定硬币面额的情况下，可以用多少种不同的方式进行金额改变。 例如，如果您有面额为1和2的硬币，可以通过3种方式为4找零：
硬币的顺序无关紧要：
另外，假设您有无限数量的硬币。
您的功能应进行大量更改，并为硬币设置一系列独特的面额：
'''
def count_change(money, coins):
  if (money < 0) or (len(coins) == 0):
    return 0
  elif money == 0:
    return 1
  else:
    return count_change(money - coins[0],coins) + count_change(money,coins[1:])
print(count_change(11, [5,7]))

# def count_change(money, coins):
#   if money < 0:
#     return 0
#   if money == 0:
#     return 1
#   if money > 0 and not coins:
#     return 0
#   return count_change(money - coins[-1],coins) + count_change(money,coins[:-1])
# print(count_change(13, [1,5,7]))

# def count_change(money, coins):
#   dp = [1] + [0]*money
#   for coin in coins:
#     for x in range(coins,money+1):
#       dp[x] += dp[x-coin]
#   return dp[money]
# print(count_change(13, [1,5,7]))

def count_change(money, coins):
  A = [1] + [0]*money
  for c in coins:
    A = [sum(A[:k+1][::-c]) for k in range(money+1)] 
  return A[-1]
print(count_change(13, [1,5,7]))