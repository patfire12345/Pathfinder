def dijkstra(queue,wallList,finish):

    while True:
    # queue = filterDuplicate(queue)
        #queue = sortQueue(queue)
        print(queue)

        nearest = findNearest(queue,wallList,queue[0][1],queue[0][0])

        for i in range(len(nearest)):
            if finish in nearest[i]:
                print(nearest[i][0])
                return True
                
        queue.extend(nearest)
        queue.remove(queue[0])


    #if dijkstra(queue,finish):
        #return True

    #return False

def findNearest(queue,walls,point,value):
     
    x = point[0]
    y = point[1]
    
    if y == 0:
        up = None
    else:
        up = (x,y-1)
        
    if x == 0:
        left = None
    else:
        left = (x-1,y)

    down = (x,y+1)
    right = (x+1,y)

    nearest = [[value+1,up],[value+1,down],[value+1,left],[value+1,right]]
    indicies = []
    newNearest = []

    for i in range(len(nearest)):
        if nearest[i][1] == None or nearest[i][1] in walls:
            indicies.append(i)

    
    for j in range(len(nearest)):
        if j not in indicies:
            newNearest.append(nearest[j])

    indicies = []

    

    for k in range(len(queue)):
        for m in range(len(newNearest)):
            if (newNearest[m][1] == queue[k][1] and newNearest[m][0] >= queue[k][0]):
                indicies.append(m)

    nearest = newNearest
    newNearest = []

    for n in range(len(nearest)):
        if n not in indicies:
            newNearest.append(nearest[n])

    return newNearest
            
            
"""
def filterDuplicate(queue):

    newQueue = []
    match = []
    highestLength = 0
    i = 0

    while i < len(queue)-1:

        for j in range(i+1,len(queue)):
            if queue[i][1] == queue[j][1]:

                if queue[i][0] > highestLength:
                    highestLength = queue[i][0]

                if queue[j][0] > highestLength:
                    highestLength = queue[j][0]

        
            if queue[i][1] != queue[j][1] or (queue[i][1] == queue[j][1] and queue[j][0] == highestLength):
                newQueue.append(queue[j])

        

        queue = newQueue
        i = i+1

    return queue


def sortQueue(queue):

    for i in range(len(queue)-1):
        for j in range(len(queue)-i-1):
            if queue[j][0] > queue[j+1][0]:
                queue[j][0],queue[j+1][0] = queue[j+1][0],queue[j][0]

    return queue
"""
    
while True:
    startx = int(input("Start x: "))
    starty = int(input("Start y: "))
    finishx = int(input("Finish x: "))
    finishy = int(input("Finish y: "))

    wallList = []
    
    ans = ''

    while ans != 'yes':
        wallx = int(input("Wall x: "))
        wally = int(input("Wall y: "))

        wallList.append((wallx,wally))
        ans = input("More walls? ")

    start = (startx,starty)
    finish = (finishx,finishy)
    wall = (wallx,wally)

    queue = [[0,start]]

    print(dijkstra(queue,wallList,finish))
    print('\n')
