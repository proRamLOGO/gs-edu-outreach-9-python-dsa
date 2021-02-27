def dfs_helper( node, graph, vis ) :
    
    # Recursive case
    print(node)
    for neighbour in graph[node] :
        if not vis[neighbour]:
            vis[neighbour] = True
            dfs_helper( neighbour, graph, vis )
    
def dfs( graph, vis ) :
    for i in graph :
        if not vis[i] :
            vis[i] = True
            dfs_helper(i, graph, vis)

def main() :
    n = int(input())
    lab = input().split()
    m = int(input())
    graph = dict()
    vis = dict()
    for i in lab :
        graph[i] = []
        vis[i] = False
    for i in range(m) :
        u,v = input().split()
        graph[u].append(v)
        graph[v].append(u)
        
    dfs(graph, vis)
    
    print(vis)
    # print(graph)

main()

{'A': ['B', 'C'],
 'B': ['A', 'C'],
 'C': ['B', 'D', 'A'],
 'D': ['C'],
 'E': []
}

##g = {
##       A:  [ C, B ],
##       B:  [ C, A ],
##       C:  [ A, B, D ],
##       D:  [ C ],
##       E:  []
##    }

##
##def main2() :
##    n = int(input())
##    lab = input().split()
##    m = int(input())
##    graph = dict()
##    for i in range(m) :
##
##        u,v = input().split()
##        
##        if u in graph:
##            graph[u].append(v)
##        else :
##            graph[u] = [v]
##
##        if v in graph:
##            graph[v].append(u)
##        else :
##            graph[v] = [u]
##
##    print(graph)
##    
##
##main()


##{
## 'A': ['B', 'C'],
## 'B': ['A', 'C'],
## 'C': ['B', 'D', 'A'],
## 'D': ['C']
## }


##
##g = {
##       A:  [ C, B ],
##       B:  [ C, A ],
##       C:  [ A, B, D ],
##       D:  [ C ],
##       E:  []
##       ...
##       u: [ ..., v]       # g[u].append(v)
##       v: [ ..., u]       # g[v].append(u)
##       
##    }
