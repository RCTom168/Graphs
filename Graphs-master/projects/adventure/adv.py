from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# We will use this class to help us keep track of the rooms that we have visited and the rooms that still need to be visited.
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)


# Load a world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = r"C:\Users\robtom\Desktop\Graphs-master\projects\adventure\maps\test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = r"C:\Users\robtom\Desktop\Graphs-master\projects\adventure\maps\test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = r"C:\Users\robtom\Desktop\Graphs-master\projects\adventure\maps\test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = r"C:\Users\robtom\Desktop\Graphs-master\projects\adventure\maps\test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
map_file = r"C:\Users\robtom\Desktop\Graphs-master\projects\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

def traverse_maze(player):
    
    # Dictionary that holds the Reverse directions
    reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    # List that keeps track of the Path traveled to visit rooms
    traversal_path = []

    # The Set that keeps track of the rooms that we have visited
    visited_rooms = set() 

    # The variable that holds the Class Stack
    s = Stack()

    # The variable that holds the player's current room
    cur_room = player.current_room

    # While the number of rooms visited is less than total number of rooms
    while len(visited_rooms) < len(room_graph):

        # If the current room is not in the visited rooms set
        if cur_room.id not in visited_rooms:

            # Add the current room id to the visited rooms set
            visited_rooms.add(cur_room.id)

        # The previous room is now the current room
        prev_room = cur_room

        # Choose a direction to travel in

        # For a direction that is available to travel in in our current room, given the exits that are available
        for direction in cur_room.get_exits():
            
            # If a given direction of the current room is not in our visited room set
            if cur_room.get_room_in_direction(direction).id not in visited_rooms: 
                
                # Use stack to push the reverse direction of the direction we want to travel in.
                s.push(reverse_direction[direction])

                # Have the player travel in the selected direction
                player.travel(direction)

                # Append the selectd direction to the traversal path List
                traversal_path.append(direction)

                # Add the Player's current room ID to the visited rooms set
                visited_rooms.add(player.current_room.id)

                # The room that is traveled to becomes the player's new current room
                cur_room = player.current_room

                break # In order to avoid looping over other exits, we break the loop here, that way we only travel through the first unexplored exit.
        
        # This is what makes us traverse. Means it wasn't updated in loop above.
        if cur_room == prev_room:
            
            # Use Stack to pop the selected direction traveled out
            direction = s.pop()

            # The player travels in the selected direction
            player.travel(direction)

            # Append the slected direction to the traversal path
            traversal_path.append(direction)

            # The room that is traveled to becomes the player's new current room
            cur_room = player.current_room

    # Returns a list that has the traversal path results
    return list(traversal_path)

# The traversal path equals all of the work of the traverse maze function
traversal_path = traverse_maze(player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
