# https://atcoder.jp/contests/dp/tasks/dp_a

import sys
import numpy as np
sys.stdin = open('input.txt','r')  ##INPUT FILE NAME HERE
sys.stdout = open('output.txt','w')  ##OUTPUT FILE NAME HERE

def Solve():
    n  = int(input())
    arr = list(map(int, input().split()))
    dp = [0 for i in range(n)]
    dp[0] = arr[0]

    if n > 1:
        dp[1] = abs(arr[0]-arr[1])

    if n > 2:
        dp[2] = min(dp[1]+ abs(arr[0]-arr[1]), abs(arr[0]-arr[2]))
    
    if n > 3:
        for i in range(3, n):
            dp[i] = min(abs(arr[i]-arr[i-1])+dp[i-1], abs(arr[i]-arr[i-2])+dp[i-2])

    print(dp[-1])
Solve()