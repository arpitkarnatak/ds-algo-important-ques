import sys
import numpy as np
sys.stdin = open('input.txt','r')  ##INPUT FILE NAME HERE
sys.stdout = open('output.txt','w')  ##OUTPUT FILE NAME HERE

def Solve():
    ## https://atcoder.jp/contests/dp/tasks/dp_c

    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    dp = [[0 for i in range(3)] for x in range(n)]

    #print(np.matrix(dp))
    dp[0] = a[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + a[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + a[i][2]

    
    #print(np.matrix(dp))
    print(max(dp[-1]))

Solve()