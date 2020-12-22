#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 카데인 알고리즘 : O(n)
import sys
def solution(prices : list[int]):
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)
    print(profit)

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution(prices)