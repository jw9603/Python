# import networkx as nx
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]



    # def find_star_center(edges):
    #     G = nx.Graph()
    #     G.add_edges_from(edges)
        
    #     # In a star graph, the center node is the one with the maximum degree
    #     degrees = dict(G.degree())
    #     center = max(degrees, key=degrees.get)
        
    #     return center
    
if __name__ == '__main__':
    a = Solution()
    
    res1 = a.findCenter([[1,2],[2,3],[4,2]])
    res2 = a.findCenter([[1,2],[5,1],[1,3],[1,4]])
    
    print('res1',res1)
    print('res2',res2)
