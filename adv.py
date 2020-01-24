from room import Room
from player import Player
from world import World
from util import Stack, Queue #Use this for storage

import random
from ast import literal_eval



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Shows where the player's start point
player = Player(world.starting_room)
# print("Starting room", world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# The graph should be a dictionary --> Graph room_id 's to?
mapDictionary = {}

# vertex = current_room
# edges = paths - directions?


# Try BFS/t --> searching paths to the maze?

# def bfs(starting_room_id):
#     # Create a queue
#     q = Queue()
#     # Enqueue starting point in a list to start path = starting_room_id
#     q.enqueue([starting_room_id])
#     visited = set() 

#     # While there is stuff in the queue
#     while q.size()> 0:
#         # pop/grab the first available path
#         path = q.dequeue()
#         # current_room = last item in the path
#         current_room = path[-1]
#         print("current room", current_room, "\n")
#         # visited.add(current_room)
#         # print('Add to visited', visited.add(current_room))
#         # If not visited
#         # if current_room not in visited:
#         #     visited[current_room] = path
        
#         # For each...edge?...direction in the map graph's current_room
#         # direction == iterator == i ==[]
#         for direction in mapDictionary[current_room]:
#             # search for a room with a "?"
#             print('MapGraph Directions', mapDictionary[current_room][direction], "\n")
#             if mapDictionary[current_room][direction] == '?':
#                 # return to the available paths
#                 return path
#             elif mapDictionary[current_room][direction] not in visited:
#                 # create a new path to append the edge/direction
#                 new_path = list(path)
#                 new_path.append(mapDictionary[current_room][direction])
#                 print("Appending direction", new_path, "\n")
#                 q.enqueue(new_path)

#     print("Visited", visited, "\n")
            
# DFS/t --> Generating Maze???
# need to connect/ compare to room_graph? --> ancestors?
# keep track of previously traveled rooms? counter?


"""
Need a dictionary = mapGraph
{
    room_id      dir : exit?, dir : r5, dir : exit? dir : exit?
room    0:      {'n' : '?',    's': 5,   'w': '?',   'e': '?'  },

move ->           dir : r0, dir : exit?, dir : exit?
        5:       {'n' : 0,  's' : '?',   'e': '?'   }
}
"""

# Three commands that may be useful: --> How?
# player.current_room.id --> find the id of th room the player is currently in
# player.current_room.get_exits() --> use to find possible exits
# player.travel(direction) --> Need to figure how to use this

def search(starting_room):
    # rooms players have been to
    visitedRoom = 0
    # opposing cardinal  directions
    opp_directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # What room we are currently in
    current_room = player.current_room
    # print("Players current room", player.current_room)
    # The id we are currently in
    # print("Players current room", player.current_room.id)
    room_id = player.current_room.id
    
    #prints out cardinal direction
    # print("Exits", player.current_room.get_exits() ) 

    # make a dictionary of rooms with [n,s,e,w] as key:pair = either room_id or '?'
    room_dict ={}
    # conditional or loop
    # while the length of mapDictionary ! = length of room graph
    while len(mapDictionary) != len(room_graph):
        # print("current room", current_room.id)
        # if room id is not in mapDictionary:
        if room_id not in mapDictionary:
            # Iterate to find the possible exits:
            for i in current_room.get_exits():
                # add the "?" in the room dictionary?
                # print("I", i) # prints n direction
                room_dict[i] = '?'
                print("room dictionary", room_dict[i]) 
            if traversal_path:
                prevRoom = opp_directions[traversal_path[-1]]
                room_dict[prevRoom] = prevRoom
            # add the unexplored "/" room to the room id
            mapDictionary[room_id] = room_dict

        else:
            break
            # print("Room dictionary",room_dict)
        # What next?
        # We see there is an unexplored '?'
        

print("Search Function", search(room_graph))
print("------------------")
print("Map Graph Dictionary", mapDictionary) #{0: {'n': '?'}}
print("------------------")
print("Traversal path", traversal_path)
print("------------------")


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# def maze(starting_room):
#     room = starting_room
#     # Create a stack/queue as appropriate
#     stack = Stack()
#     # Put the starting point in that
#     stack.push(room)
#     # Make a set to keep track of where we have been
#     visited = {}
#     # While there is stuff in the stacl/queue
#     while stack.size() < len(room_graph):
#         print("Fisrt Room call", room)
#         path = stack.pop()
#         print("Room path", path)
#         # room = path[-1]
#         break
#         # if room not in visited:
#         #     print("Room if statement", room)
#         #     # visited[room] = {}
#         #     # print(visited)