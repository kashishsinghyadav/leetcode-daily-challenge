class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        bob=0
        alice=0
        n=len(colors)
        for i in range(1,n-1):
            curr=colors[i]
            prev=colors[i-1]
            nxt=colors[i+1]
            if curr=='A':
                if prev=='A' and nxt=='A':
                    alice+=1
            elif curr=='B':
                if prev=='B' and nxt=='B':
                    bob+=1

        if alice>bob:return True
        return False
