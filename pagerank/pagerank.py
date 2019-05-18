#graph = [[0,1,1,0],[0,0,0,1],[1,1,0,1],[0,0,1,0]]
graph = [[0,1,1,1],[0,0,1,1],[1,0,0,0],[1,0,1,0]]
n = len(graph)
#Damping factor
#If you increase the damping factor, the iterations will increase
d = 0.85
#Page rank of A = (1-d)/N + d( PR(All nodes incoming to A) / No.of Outgoing links from those nodes)
#Stopping condition is that sum(abs change of prev - curr) < 0.0001
previter = [1/n,]*n
curriter = [0,]*n

def prevcheck(graph, n):
    for i in range(n):
        temp = graph[i]
        if 1 not in temp:
            return False
    return True

def incomingnodes(k,n):
    temp = []
    for i in range(n):
        if graph[i][k] == 1:
            temp.append(i)
    return temp

def outgoingCount(k,n):
    c=0
    for i in range(n):
        if graph[k][i] == 1:
            c+=1
    return c

def PR(k,n,d):
    nodes = incomingnodes(k,n)
    tempsum = 0
    for index in nodes:
        pr_prev = previter[index]
        count = outgoingCount(index,n)
        tempsum += pr_prev/count
    pr = (1-d)/n + d*tempsum
    return pr

def check():
    temp = 0
    for i in range(n):
        prev = previter[i]
        curr = curriter[i]
        abschange = abs(prev-curr)
        temp += abschange
    if temp<0.0001:
        return True
    return False

def PRalgorithm(previter, curriter):
    iter = 0
    if prevcheck(graph, n):
        while True:
            for i in range(n):
                curriter[i] = PR(i,n,d)
            if not check():
                previter,curriter = curriter,previter
                iter+=1
            else :
                break

        print("Page ranks for the given network is as follows :\n")
        print(curriter)
        print("\nNumber of iterations required : ", end="")
        print(iter)
    else:
        print("Graph has a node with no outgoing edge!")


PRalgorithm(previter, curriter)

#graph = [[0,1,1,0],[0,0,0,1],[1,1,0,1],[0,0,1,0]]
graph = [[0,1,1,1],[0,0,1,1],[1,0,0,0],[1,0,1,0]]
n = len(graph)
d = 0.95
#Page rank of A = (1-d)/N + d( PR(All nodes incoming to A) / No.of Outgoing links from those nodes)
#Stopping condition is that sum(abs change of prev - curr) < 0.0001
previter = [1/n,]*n
curriter = [0,]*n
PRalgorithm(previter, curriter)


# In[12]:


graph = [[0,1,1,0],[0,0,0,1],[1,1,0,1],[0,0,1,0]]
n = len(graph)
d = 0.85
previter = [1/n,]*n
curriter = [0,]*n
PRalgorithm(previter, curriter)


# In[13]:


graph = [[0,1,1,0],[0,0,0,1],[1,1,0,1],[0,0,1,0]]
n = len(graph)
d = 0.95
previter = [1/n,]*n
curriter = [0,]*n
PRalgorithm(previter, curriter)







