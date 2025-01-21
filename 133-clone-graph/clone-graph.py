"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        relation = {}    #to keep track of old node to new node(HashMap)


        def clone(node):               #using dfs to solve
            if node in relation:       #checking if we have already cloned & visited a node
                return relation[node]  #if yes, then return the cloned node

            copyNode = Node(node.val)  #if we hvnt visited, then create a clone
            relation[node] = copyNode  #add the relation to our HashMap
            for neighbor in node.neighbors:
                #recursively check current node's neighbours, clone and add to the new clone's neighbours attribute
                copyNode.neighbors.append(clone(neighbor)) 
            return copyNode
        
        return clone(node) if node else None  #check base case: if node is null or not
    

        