# Islands matrix

#Islands Matrix Problem
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# There are 4 islands

#  , 1,    1,
# 1, 1,    1, 1

# 1,     1,  ,
# 1,     1, 1,

# nodes: 1s
# edge: connected n/s/w/e

# islands: connected components

# Build our graph or just define getNeighbors()

# stepNrth == row>0
def get_neighbors(node, matrix):
    row, col = node

    stepNorth = stepSouth = stepWest = stepEast = False
    # take a step north
    if row >0:
        stepNorth = row - 1
    
    #take a step South
    if row < len(matrix -1):
        stepSouth = row + 1

    # Take a step East
    if col < len(matrix[row]) - 1:
        stepEast = col + 1

    # Take a step West
    if col > 0:
        stepWest = col - 1

    if stepNorth is not False and matrix[tepNorth][col]

def dft_recursive(node, visited, matrix):
    # If node not visited
    if node not in visited:

        # Add to visited
        visited.add(node)

        # Get neighbors
        neighbors = get_neighbors(node, matrix)

        # For each neighbor
        for neighbor in neighbors:

            #Recurse
            dft_recursive(neighbor, visited, matrix)

def islands_counter(isles):

    visited = set()
    number_islands = 0
    # Iterate throguh the matrix
    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)
    # When we see a 1, if it has not been visited
            if node not in visited and isles[row][col] == 1
    
            # Increment our islands counter
            number_islands += 1

            # Run a traversal
            dft_recursive(node)
    
    return number_islands