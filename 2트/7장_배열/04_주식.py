#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def brute(prices : list[int]):
    money = 0
    for i, n in enumerate(prices):

        for j in range(i+1,len(prices)):
            money = max(money, prices[j]-prices[i])

    print(money)

# 카데인 알고리즘 : O(n)
import sys
def solution(prices : list[int]):
    profit = 0
    min_price = sys.maxsize

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
        print(min_price, profit)
    print(profit)
    return


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution(prices)