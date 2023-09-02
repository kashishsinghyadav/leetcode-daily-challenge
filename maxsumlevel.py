        l=defaultdict(list)
        def dfs(root,h):
            if root is None:
                return
            l[h].append(root.val)
            dfs(root.left,h+1)
            dfs(root.right,h+1)
        dfs(root,1)
        res=[]
        for i in l.values():
            res.append(sum(i))
        return res.index(max(res))+1
