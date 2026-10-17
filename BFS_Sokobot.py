from collections import deque

# test mazes, these are given
#_ = valid space and # is wall
maze = [
    list("########"),
    list("#S_____#"),
    list("#__B___#"),
    list("#______#"),
    list("#______#"),
    list("#____G_#"),
    list("########")
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
    start_pos = None
    crate_map = set()
    goal_map = set()

    height = len(maze)      
    width = len(maze[0])   

    for i in range(height):
        for j in range(width):
            if (maze[i][j] == 'S'):    #stores start coordinates
                start_pos = (i, j)

            if (maze[i][j] == 'B'):    #stores crate coordinates
                crate_map.add((i, j))

            if (maze[i][j] == 'G'):    #stores goal coordinates
                goal_map.add((i, j))

    start_goal = ((start_pos, frozenset(crate_map)), goal_map)
    return start_goal    #returns a state, which is player pos and crate map, along with goal map

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
         player_pos, crate_map = current_state

         if (crate_map == goal_map): return path_dict, current_state

         for direction, (row, col) in directions.items():     #iterate for every neighbor of current state
             shifted_row = player_pos[0] + row             #shifted row and column correspond to the coordinates of
             shifted_col = player_pos[1] + col             #neighboring space for the iteration (in first iteration it checks upward (-1, 0)
                                                              
             if 0 <= shifted_row < height and 0 <= shifted_col < width:   #validity check if it is within bounds of the map

                 if (shifted_row, shifted_col) in crate_map: # if neighbor is a crate 
                    next_row = shifted_row + row
                    next_col = shifted_col + col

                    if maze[next_row][next_col] != '#' and (next_row, next_col) not in crate_map: # and the space after the crate is not a wall and not another crate
                         new_crate_map = set(crate_map)
                         new_crate_map.remove((shifted_row, shifted_col))
                         new_crate_map.add((next_row, next_col))
                         new_crate_map = frozenset(new_crate_map)
                         new_player_pos = (shifted_row, shifted_col)
                         new_state = (new_player_pos, new_crate_map)

                         if new_state not in visited:
                             frontier.append(new_state)
                             visited.add(new_state)  
                             path_dict[new_state] = ((current_state), direction)  #store valid neighbor, the node from where it was reached (parent), and the direction of movement it took to reach it
                     
                 elif maze[shifted_row][shifted_col] != '#':   #if the neighbor is not a crate or wall
                     new_player_pos = (shifted_row, shifted_col)
                     new_state = (new_player_pos, crate_map)

                     if new_state not in visited:
                         frontier.append(new_state)
                         visited.add(new_state)     
                         path_dict[new_state] = ((current_state), direction)  #store valid neighbor, the node from where it was reached (parent), and the direction of movement it took to reach it

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

start_state, goal_map = find_start_goal(maze)
path_map, solved_state = bfs(maze)
move_sequence_solution = deconstruct(path_map, start_state, solved_state)

print(move_sequence_solution)