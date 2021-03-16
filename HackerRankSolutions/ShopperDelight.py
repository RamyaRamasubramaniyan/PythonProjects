# HackerRank - Shopper's Delight
# A Shopaholic wants to buy a pair of jeans, a pair of shoes, a skirt, and a top but has a limited budget in dollars. Given different pricing options for each product, determine how many options our customer has to buy 1 of each product. You cannot spend more money than the budgeted amount.
# 
# Example
# priceOfJeans = [2, 3]
# priceOfShoes = [4]
# priceOfSkirts = [2, 3]
# priceOfTops = [1, 2]
# budgeted = 10
# 
# The customer must buy shoes for 4 dollars since there is only one option. This leaves 6 dollars to spend on the other 3 items. Combinations of prices paid for jeans, skirts, and tops respectively that add up to 6 dollars or less are [2, 2, 2], [2, 2, 1], [3, 2, 1], [2, 3, 1]. There are 4 ways the customer can purchase all 4 items.
# 
# Function Description
# 
# Complete the getNumberOfOptions function in the editor below. The function must return an integer which represents the number of options present to buy the four items.
# 
# getNumberOfOptions has 5 parameters:
# int[] priceOfJeans: An integer array, which contains the prices of the pairs of jeans available.
# int[] priceOfShoes: An integer array, which contains the prices of the pairs of shoes available.
# int[] priceOfSkirts: An integer array, which contains the prices of the skirts available.
# int[] priceOfTops: An integer array, which contains the prices of the tops available.
# int dollars: the total number of dollars available to shop with.
# 
# Constraints
# 
# 1 ≤ a, b, c, d ≤ 103
# 1 ≤ dollars ≤ 109
# 1 ≤ price of each item ≤ 109
# Note: a, b, c and d are the sizes of the four price arrays

import itertools, bisect

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    # Write your code here
    priceOfJeansAndSkirts = [i + j for i, j in itertools.product(priceOfJeans, priceOfSkirts)]
    priceOfShoesAndTops = [i + j for i, j in itertools.product(priceOfTops, priceOfShoes)]

    result = 0
    cost_limit = 0
    priceOfJeansAndSkirts.sort()
    priceOfShoesAndTops.sort()

    
    for price in priceOfJeansAndSkirts:
        remaningDollar = budgeted - price
        if price >= budgeted:
            break
        trial_count = bisect.bisect_right(priceOfShoesAndTops, remaningDollar)
        result += trial_count
 
    return result 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    priceOfJeans_count = int(input().strip())

    priceOfJeans = []

    for _ in range(priceOfJeans_count):
        priceOfJeans_item = int(input().strip())
        priceOfJeans.append(priceOfJeans_item)

    priceOfShoes_count = int(input().strip())

    priceOfShoes = []

    for _ in range(priceOfShoes_count):
        priceOfShoes_item = int(input().strip())
        priceOfShoes.append(priceOfShoes_item)

    priceOfSkirts_count = int(input().strip())

    priceOfSkirts = []

    for _ in range(priceOfSkirts_count):
        priceOfSkirts_item = int(input().strip())
        priceOfSkirts.append(priceOfSkirts_item)

    priceOfTops_count = int(input().strip())

    priceOfTops = []

    for _ in range(priceOfTops_count):
        priceOfTops_item = int(input().strip())
        priceOfTops.append(priceOfTops_item)

    budgeted = int(input().strip())

    result = getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted)

    fptr.write(str(result) + '\n')

    fptr.close()
    
# SAMPLE INPUT1 : 2 2 3 1 4 1 2 3 1 2 3 10
# SAMPLE OUTPUT1 : 3
# SAMPLE INPUT2 : 1 4 3 3 4 1 2 3 2 1 4 12
# SAMPLE OUTPUT 2: 2
# SAMPLE INPUT 3 : 1 1 1 4 1 3 1 1 3
# SAMPLE OUTPUT 3 : 0
