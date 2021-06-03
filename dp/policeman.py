import sys
import numpy as np
sys.stdin = open('input.txt','r')  ##INPUT FILE NAME HERE
sys.stdout = open('output.txt','w')  ##OUTPUT FILE NAME HERE


def Policeman_catch_thief(arr, k):
    # https://www.geeksforgeeks.org/policemen-catch-thieves/

    ans = [0 for i in range(len(arr))]


    for i in range(len(arr)):
        if arr[i] != 'P':
            ans[i] = ans[i-1]
            print(arr,ans)


        else:
            #check for thieves from k positions left to k positions right
            print(f'Loop from {max(0,i-k)} and {min(i+k+1, len(arr))}')
            for j in range(max(0,i-k), min(i+k+1, len(arr))):
                if arr[j] == 'T' and j!=i:
                    ans[i] = 1 if i == 0 else 1+ans[i-1]
                    arr[j] = 'C'  # Don't count again
                    print(arr, ans)
                    break
    print(ans)


Policeman_catch_thief(['P', 'T', 'P', 'T', 'T', 'P'], 3)
