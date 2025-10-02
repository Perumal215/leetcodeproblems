class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None   

        clones = {}     
        clones[node] = Node(node.val)
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor) 
                clones[curr].neighbors.append(clones[neighbor])
        return clones[node]
