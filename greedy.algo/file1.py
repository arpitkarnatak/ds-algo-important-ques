import sys
import numpy as np
import math
sys.stdin = open('../input.txt','r')  ##INPUT FILE NAME HERE
sys.stdout = open('../output.txt','w')  ##OUTPUT FILE NAME HERE
def N_Meetings(start, end): 

    ## start = list, end = list
    ## https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/
    ## Arrange in ascending order of meeting end
    ## If it's equal, arrange in ascending order of start time

    
    meets = [tuple((end[i], start[i], i+1)) for i in range(len(start))]
    
    meets.sort()
    print(meets)

    ## First meeting will happen
    poss_meets = [meets[0]]

    for i in meets[1:]:
        ## Add the next meet if the start time of this meet is greater than equal to end of last meet
        if i[1] >= poss_meets[-1][0]:
            poss_meets.append(i)

    print([i[-1] for i in poss_meets]) ## Indexes of max meetings possible

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# N_Meetings(a,b)

def Stonks(arr):
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/'

    ### Calculate profit or loss between each day.
    ### Then add all days of profit and leave out the loss
    return sum([max(arr[i+1]-arr[i], 0) for i in range(len(arr)-1)])

# Stonks(list(map(int,input().split())))

def IslandSurvival(days_to_survive, max_food, req_food):
    ##https://www.geeksforgeeks.org/survival/
    ## Add max food for 6 days and subtract req food everyday to food left. 
    ## whenever there is negative food left, return false (as food got spent)
    food_left = 0
    day = 1

    for i in range(1,days_to_survive+1):
        if i%7 != 0:
            food_left = food_left + max_food - req_food
            if food_left < 0:
                return False
        else:
            food_left -= req_food
            if food_left < 0:
                return False
    return True

#a,b,c = map(int,input().split())
#print(IslandSurvival(a,b,c))

def MaxProduct(arr):
    #https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
    ze, po, neg = [], [], []
    for i in arr:
        if i<0:
            neg.append(i)
        elif i>0:
            po.append(i)
        else:
            ze.append(i)

    neg.sort()

    if neg != [] and len(neg)>1:
        ans = math.prod(neg[ :len(neg)//2+1 ])
    else:
        ans = -neg[0]

    if po != []:
        ans *= math.prod(po)

    if ze != [] and po == []:
        ans = min(0, ans)
    return ans

#print(MaxProduct([-1,0,6,-3,6,2]))
