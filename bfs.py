#-------------BFS ALGORITHM----------------
#-----ABRAR UL HASSAN SPJ--------
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=[] #List for visited node
queue=[]  #initialization of queue
def bfs(visited,graph,node): #function for bfs
    visited.append(node)
    #print("visisted ",visited)
    queue.append(node)
    #print("Queue ",queue)
    while queue:  #creating while loop for visiting each node
        m=queue.pop(0)
        for i in graph[m]:
            #print("loop grpah [m ] ",graph[m])
            if i not in visited:
                print(i)
                visited.append(i)
                print("visisted ",visited)
                queue.append(i)
                #print("Queue ",queue)
                
bfs(visited,graph,'5')#function calling