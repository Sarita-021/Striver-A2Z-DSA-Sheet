'''You are given three arrays: id, deadline, and profit, where each job is associated with an ID, a deadline, and a profit.
Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated 
with a job only if it is completed by its deadline.

Your task is to find:
The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1'''

# Greedy approach

class Jobs:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    # Function used for sorting jobs according to their deadlines
    def JobSequencing(self, id, deadline, profit):
        jobs = [Jobs(id[i], deadline[i], profit[i]) for i in range(len(id))]
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxd = max(deadline)
        slot = [-1]*(maxd+1)
        cntJobs = maxProfit = 0
        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    cntJobs += 1
                    maxProfit += jobs[i].profit
                    break
        return [cntJobs, maxProfit]
    

# Optimized Code (Using DSU)

class Jobs:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def JobSequencing(self, id, deadline, profit):
        jobs = [Jobs(id[i], deadline[i], profit[i]) for i in range(len(id))]

        # Step 1: Sort jobs in descending order of profit
        jobs.sort(key=lambda x: x.profit, reverse=True)

        maxd = max(deadline)
        parent = [i for i in range(maxd + 1)]  # DSU parent array

        cntJobs = maxProfit = 0

        for job in jobs:
            # Find the latest available slot before or on the job's deadline
            available_slot = self.find(parent, job.deadline)
            
            if available_slot > 0:
                # Assign job to the found slot
                parent[available_slot] = self.find(parent, available_slot - 1)  # Union operation
                cntJobs += 1
                maxProfit += job.profit

        return [cntJobs, maxProfit]
