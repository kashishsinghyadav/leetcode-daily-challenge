class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        stack = ["JFK"]
        itinerary = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())
        
        return itinerary[::-1]
