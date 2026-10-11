from collections import deque

# test mazes, these are given
#_ = valid space and # is wall
maze1 = [
    list("__##_G"),
    list("#_#__#"),
    list("____##"),
    list("S##__#")
]

maze2 = [
    list("S__#____"),
    list("##_#_##_"),
    list("___#____"),
    list("_###_##_"),
    list("_____#__"),
    list("###____G")
]

maze3 = [
    list("S___#_____"),
    list("##_##_###_"),
    list("___#___#__"),
    list("_#_###_#__"),
    list("_#_____#__"),
    list("_#####_#__"),
    list("_____#____"),
    list("###______G")
]

#self defined dict to supplement search algorithm
directions = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

# store map start and goal states as coordinate tuples
def find_start_goal(maze):
    start_state = None
    end_state = None
    height = len(maze)      
    width = len(maze[0])   

    for i in range(height):
        for j in range(width):
            if (maze[i][j] == 'S'):    #stores start coordinates
                start_state = (i, j)

            if (maze[i][j] == 'G'):    #stores goal coordinates
                end_state = (i, j)

    return (start_state, end_state)

#takes the maze layout and returns all paths and its corresponding information until the end state
def bfs(maze):
    frontier = deque()
    visited = set() #set to restrict repeating values
    path_dict = {} #store path for deconstruction

    height = len(maze)      
    width = len(maze[0]) 

    frontier.append(start_state)
    visited.add(start_state)

    while (frontier):
         current_state = frontier.popleft()

         if (current_state == end_state):
            break

         for direction, (row, col) in directions.items():     #iterate for every neighbor of current state
             shifted_row = current_state[0] + row             #shifted row and column correspond to the coordinates of
             shifted_col = current_state[1] + col             #neighboring space for the iteration (in first iteration it checks upward (-1, 0)
                                                              
             if 0 <= shifted_row < height and 0 <= shifted_col < width:   #validity check if it is within bounds of the map
                 if maze[shifted_row][shifted_col] != '#' and (shifted_row, shifted_col) not in visited:   #checks if the neighboring space is not a wall and if not visited
                     frontier.append((shifted_row, shifted_col)) #add to frontier the valid neighbor
                     visited.add((shifted_row, shifted_col))     #add to visited the valid neighbor
                     path_dict[(shifted_row, shifted_col)] = ((current_state), direction)  #store valid neighbor, the node from where it was reached (parent), and the direction of movement it took to reach it
    return path_dict

# takes the paths information and returns the appropriate moves to go from start to end
def deconstruct(path_dict, start_state, end_state):
     path = []
     node = end_state #start from end to backtrack
     while (node != start_state):                #for as long as we haven't reached the start state
          parent, direction = path_dict[node]    #store parent and direction it took to get to current node
          path.append(direction)                 #store the direction in the path list
          node = parent                          #make the new node of analysis the current's parents and repeat
     path.reverse() 
     return (path)

start_state, end_state = find_start_goal(maze3)
path_map = bfs(maze3)
move_sequence_solution = deconstruct(path_map, start_state, end_state)

print(move_sequence_solution)