'''Geek is a software engineer. He is assigned with the task of calculating average waiting time of all the processes by 
following shortest job first policy. The shortest job first (SJF) or shortest job next, is a scheduling policy that selects 
the waiting process with the smallest execution time to execute next.
Given an array of integers bt of size n. Array bt denotes the burst time of each process. Calculate the average waiting time 
of all the processes and return the nearest integer which is smaller or equal to the output.
Note: Consider all process are available at time 0.
geeksforgeeks.org/problems/shortest-job-first/1'''


class Solution:
    def solve(self, bt):
        bt.sort()
        n = len(bt)
        totalWt = 0
        prevWt = 0
        for i in range(n-1):
            totalWt += prevWt + bt[i]
            prevWt += bt[i]
            
        avgWt = totalWt // n
        return avgWt