'''Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults
using Least Recently Used (LRU) Algorithm. 
geeksforgeeks.org/problems/page-faults-in-lru5603/1'''

class Solution:
    def pageFaults(self, N, C, pages):
        lru = []
        cnt = 0
        for i in range(N):
            if len(lru) < C and pages[i] not in lru:
                lru.append(pages[i])
                cnt += 1
            elif pages[i] in lru:
                lru.remove(pages[i])
                lru.append(pages[i])
            else:
                lru.pop(0)
                lru.append(pages[i])
                cnt += 1
        return cnt