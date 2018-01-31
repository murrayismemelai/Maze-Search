import random  
from random import randint
import numpy as np
import string
#warning: x and y confusing  
  
sx = 7
sy = 7
dfs = [[0 for col in range(sx)] for row in range(sy)]  
maze = [[' ' for col in range(2*sx+1)] for row in range(2*sy+1)]  
#1:up 2:down 3:left 4:right  
operation = {1:(0,-1),2:(0,1),3:(-1,0),4:(1,0)}  
direction = [1, 2, 3, 4]  
stack = []  
  
for i in range(2*sx+1):  
    if i%2 == 0:  
        for j in range(2*sx+1):  
            maze[i][j] = '1'  
for i in range(2*sy+1):  
    if i%2 == 0:  
        for j in range(2*sy+1):  
            maze[j][i] = '1'  

emp_maze = [[' ' for col in range(2*sx+1)] for row in range(2*sy+1)]      
        
def show(graph):  
    for i in graph:  
        for j in i:  
            print j,  
        print  
  
def showRouter(stack):  
    RGragh = [[0 for col in range(sx)] for row in range(sy)]  
    for (x, y) in stack:  
        RGragh[y][x] = 1  
    show(RGragh)  
    print  
  
def generateMaze(start,dfs,maze,operation,direction):  
    x, y = start  
    dfs[y][x] = 1  
    random.shuffle(direction)  
    for d in direction:  
        px, py = (x + y for x, y in zip(start, operation[d]))  
        if px < 0 or px >= sx or py < 0 or py >= sy:  
            pass  
        else:  
            if dfs[py][px] is not 1:  
                mx = 2*x + 1  
                my = 2*y + 1  
                if d == 1:  
                    maze[my-1][mx] = ' '  
                elif d == 2:  
                    maze[my+1][mx] = ' '  
                elif d == 3:  
                    maze[my][mx-1] = ' '  
                elif d == 4:  
                    maze[my][mx+1] = ' '  
                generateMaze((px,py),dfs,maze,operation,direction) 
    return dfs,maze
    
def random_maze(maze):
    for x in range(15):
        for y in range(15):
            temp=randint(0,2)
            if temp==0:
                maze[x][y]='1'
            if x==0 or x==14 or y==0 or y==14:
                maze[x][y]='1'
    #maze[1][1]=' '
    #maze[13][13]=' '
    return maze
    
def write_maze(maze,thefile,mode):
    for i,item in enumerate(maze):
        if item=='1':
            print>>thefile, 1
        else:
            print>>thefile, 0
        if i ==0:
            print>>thefile, mode

def mod_maze(maze):
    x=randint(1,13)
    y=randint(1,13)
    counter=0
    while counter<1:
        print counter
        if maze[x][y]=='1':
            counter = counter+1
            maze[x][y]=' '


"""
graph_maze={}

for x in range(1,14):
    for y in range(1,14):
        if new_maze[x][y]==' ':
            if new_maze[x-1][y]==' ':
                if (x,y) in graph_maze:
                    graph_maze[(x,y)]= graph_maze[(x,y)] | set([(x-1,y)])
                else:
                    graph_maze[(x,y)]= set([(x-1,y)])
            if new_maze[x][y-1]==' ':
                if (x,y) in graph_maze:
                    graph_maze[(x,y)]= graph_maze[(x,y)] | set([(x,y-1)])
                else:
                    graph_maze[(x,y)]= set([(x,y-1)])
            if new_maze[x+1][y]==' ':
                if (x,y) in graph_maze:
                    graph_maze[(x,y)]= graph_maze[(x,y)] | set([(x+1,y)])
                else:
                    graph_maze[(x,y)]= set([(x+1,y)])
            if new_maze[x][y+1]==' ':
                if (x,y) in graph_maze:
                    graph_maze[(x,y)]= graph_maze[(x,y)] | set([(x,y+1)])
                else:
                    graph_maze[(x,y)]= set([(x,y+1)])
"""

                 
#http://bryukh.com/labyrinth-algorithms/

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("B", (row + 1, col)))#S
            graph[(row + 1, col)].append(("D", (row, col)))#N
        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("A", (row, col + 1)))#E
            graph[(row, col + 1)].append(("C", (row, col)))#W
    return graph

    
from collections import deque
def find_path_bfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    if (1,1) not in graph:
        return "NO WAY!"
        
    for i in graph.keys():
        graph[i]=sorted(graph[i])
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        #print current
        #print graph[current]
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

def find_path_dfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    stack = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    if (1,1) not in graph:
        return "NO WAY!"
        
    for i in graph.keys():
        graph[i]=sorted(graph[i],reverse=True)
    while stack:
        path, current = stack.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            stack.append((path + direction, neighbour))
    return "NO WAY!"

def change_char(dir):
    #print len(dir)
    for i in range(len(dir)):
        if dir[i] == 'A':
            dir = string.replace(dir, 'A', 'E')
            #dir[i] = 'E'
        elif dir[i] == 'B':
            dir = string.replace(dir, 'B', 'S')
            #dir[i] = 'S'
        elif dir[i] == 'C':
            dir = string.replace(dir, 'C', 'W')
            #dir[i] = 'W'
        elif dir[i] == 'D':
            dir = string.replace(dir, 'D', 'N')
            #dir[i] = 'N'
    return dir

def dir2coordinate(dir,outtxt):
    dir = dir[::-1]
    end_point_x=13
    end_point_y=13
    print >> outtxt,end_point_x
    print >> outtxt,end_point_y
    for i in range(len(dir)):
        if dir[i] == 'E':
            end_point_x =end_point_x-1
        elif dir[i] == 'S':
            end_point_y =end_point_y-1
        elif dir[i] == 'W':
            end_point_x =end_point_x+1
        elif dir[i] == 'N':
            end_point_y =end_point_y+1
        if i==0:
            print >>outtxt, 0#valid
        print >> outtxt,end_point_x
        print >> outtxt,end_point_y

intxt = open('input.txt', 'w')
valtxt = open('valid.txt', 'w')
outtxt = open('output.txt', 'w')

num_maze_1= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
             [1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
             [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,0,0,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
             [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
             [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1],
             [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
             [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

bfs_ans_1='EEEEEEEESSSSSSSSEESSSSEE'
dfs_ans_1= 'EEEEEEEEEEEESSSSSSSSWWSSSSEE'

num_maze_2= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

bfs_ans_2 = 'EEEEEEEEEEEESSSSSSSSSSSS'
dfs_ans_2 = 'EEEEEEEEEEEESSSSSSSSSSSS'

for k in range(2):
    for i in range(15):
        for j in range(15):
            print >> intxt,num_maze_1[i][j]
            if i==0 and j==0:
                print >> intxt,k

print >> valtxt,dfs_ans_1
print >> valtxt,bfs_ans_1
dir2coordinate(dfs_ans_1,outtxt)
dir2coordinate(bfs_ans_1,outtxt)

for k in range(2):
    for i in range(15):
        for j in range(15):
            print >> intxt,num_maze_2[i][j]
            if i==0 and j==0:
                print >> intxt,k

print >> valtxt,dfs_ans_2
print >> valtxt,bfs_ans_2
dir2coordinate(dfs_ans_2,outtxt)
dir2coordinate(bfs_ans_2,outtxt)

                
for i in range(1):
    #make a maze
    method = randint(0,2)
    #method =0
    if method==0:
        new_dfs,new_maze=generateMaze((0,0),dfs,maze,operation,direction)
        #new_maze=mod_maze(new_maze)
    else:
        new_maze = random_maze(emp_maze)
    #show(new_dfs)  
    show(new_maze)  
    flat_maze = [item for sublist in new_maze for item in sublist]
    
    #path  
    char_maze = np.asarray(new_maze)
    num_maze = np.where(char_maze==' ',0,1)
    graph_maze = maze2graph(num_maze)
    
    mode = randint(0,1)
    write_maze(flat_maze,intxt,mode)
    if mode == 1:
        bfs_ans = find_path_bfs(num_maze)
        if bfs_ans!='NO WAY!':
            bfs_ans = change_char(bfs_ans)
            dir2coordinate(bfs_ans,outtxt)
        else:
            print>>outtxt,1#not valid
            print>>outtxt,0
            print>>outtxt,0
            
        print >> valtxt, bfs_ans
    else:
        dfs_ans = find_path_dfs(num_maze)
        if dfs_ans!='NO WAY!':
            dfs_ans = change_char(dfs_ans)
            dir2coordinate(dfs_ans,outtxt)
        else:
            print>>outtxt,1#not valid
            print>>outtxt,0
            print>>outtxt,0
        
        print >> valtxt, dfs_ans
"""
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
            
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def dfs1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
                
def dfs_paths(graph,start,goal):
    queue = [(start, [start])]
    #print queue
    while queue:
        (vertex, path) = queue.pop(0)
        #print (vertex, path)
        #print([graph[vertex] - set(path)])
        #print "=========================="
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
                
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None   
#aaa=list(dfs_paths(graph_maze,(1,1),(13,13)))
aaa=dfs1(graph_maze,(1,1))
bbb=bfs(graph_maze,(1,1))
"""