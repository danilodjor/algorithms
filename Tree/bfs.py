def bfs(root):
    if not root:
        return root
    
    queue = []
    queue.append[root]

    while queue:
        curr= queue.pop()
        for child in curr.children:
            queue.append(child)