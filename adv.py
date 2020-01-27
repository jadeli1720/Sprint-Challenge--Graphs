from room import Room
from player import Player
from world import World
from util import Stack, Queue #Use this for bfs/t ro dfs/t storage

import random #gives access to shuffle
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

# Three commands that may be useful: --> How?
# player.current_room.id --> find the id of th room the player is currently in
# player.current_room.get_exits() --> use to find possible exits
# player.travel(direction) --> Need to figure how to use this

def bfs(starting_room_id): #search for shortest path
    # Create a queue
    q = Queue()
    # Enqueue starting point in a list to start path = starting_room_id
    q.enqueue([starting_room_id])
    visited = set() 

    # While there is stuff in the queue
    while q.size() > 0:
        # pop/grab the first available path
        path = q.dequeue()
        # current_room = last item in the path
        current_room = path[-1]
        # print("current room", current_room, "\n")
        visited.add(current_room)
        # print("visited", visited)
            
        # For each direction in the map graph's current_room
        for direction in mapDictionary[current_room]:
            # print('MapGraph Directions in bfs', mapDictionary[current_room], "\n")
            if mapDictionary[current_room][direction] == '?':
#                 # return to the available paths
                return path
            elif mapDictionary[current_room][direction] not in visited:
                # create a new path to append the edge/direction
                new_path = list(path)
                new_path.append(mapDictionary[current_room][direction])
                q.enqueue(new_path)
                # print("Appending direction", new_path, "\n")


def search(starting_room): # --> dft ==> creating maze. Exploring all paths of maze until exit is path found.
    
    # opposing cardinal  directions
    opp_directions = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # Counter of rooms player has been to.
    visitedRoomId = 0

    # while the length of mapDictionary ! = length of room graph
    while len(mapDictionary) != len(room_graph):
        # What room we are currently in
        current_room = player.current_room
        # The room id we are currently in
        room_id = current_room.id
        # Building the graph
        # make a dictionary of rooms with [n,s,e,w] as key:pair = either room_id or '?' as the value
        room_dict = {}

        # if room id is not in mapDictionary:
        if room_id not in mapDictionary:
            # Iterate to find the possible exits:
            for i in current_room.get_exits():
                # add the "?" in the room dictionary
                # print("I", i) # prints n direction
                # add the key at [i] and the value that = '?'
                room_dict[i] = '?'
                # print("room dictionary", room_dict[i]) 
            # updating the room
            if traversal_path:
                # previous room = the opposite directions of the last travel path
                prevRoom = opp_directions[traversal_path[-1]]
                # add the prevRoom to the room_dic and add it to the counter
                room_dict[prevRoom] = visitedRoomId
            # add the unexplored "?" room to the room id
            mapDictionary[room_id] = room_dict
            # print('map dictionary:', mapDictionary[room_id])
            
        else:
            # Add the room id from mapDictionary to the inner room dictionary
            room_dict = mapDictionary[room_id]
            
        
        # We see there is an unexplored '?'
        # Need to see if a room is connected or not
        # Storing the '?'s
        possible_exits = list()

        # print("Room dictionary check", room_dict) # prints the direction and the '?'
        # iterate through our room dictionary 
        for direction in room_dict:
            # print("direction in room", room_dict[direction])
            # if '?' is at index direction
            if room_dict[direction] == '?':
                # Store them so that we can use them to travel through
                possible_exits.append(direction)
                # print(f"We have a possible exit {possible_exit}")
    
        # print(len(possible_exit)) #Gives us a length of 1
        # If there is an unknown direction....
        if len(possible_exits) != 0:
            random.shuffle(possible_exits)
            # print(f'{possible_exits[0]} is the next possible direction')
            # direction = the possible direction at index[0]
            direction = possible_exits[0]
            # print('We moved',f'{direction}')
            
            # append that direction to the traversal path
            traversal_path.append(direction)
            # print('traversal path in if', traversal_path)

            # move the player in the direction using the travel function
            player.travel(direction)

            # Replacing mapDictionary's '?' with next discovered rooms id
            #Grab players current room
            room_move = player.current_room
            # print("room dictionary", mapDictionary[current_room.id][direction] )
            mapDictionary[current_room.id][direction] = room_move.id
            # print("room_move:",room_move.id,)
            visitedRoomId = current_room.id
            # print('visited room id', visitedRoomId)
        else:
            # BFS to search for next exits/possible rooms using room_id
            next_room = bfs(room_id)
            # print("Next room", next_room) 
            # print("length of next_room", len(next_room)) # = length of 3 when using 2nd map
            # if the path of next_room has results from bfs
            if next_room is not None and len(next_room) > 0:
                # print("Yeah we have reached this if statement")
                # iterate the length of the room to gain access to room id's
                for i in range(len(next_room) -1):
                    # print("I in for loop", i) # i = room id
                    # print("map check at i", mapDictionary[next_room[i]])
                    # iterate the mapDictionary's next_room at this index to access it directiondirection 
                    for direction in mapDictionary[next_room[i]]:
                    # print("direction", direction) # direction = cardinal direction
                        # print("conditional", mapDictionary[next_room[i]][direction])
                        # print("checking next plus one", next_room[i + 1])
                        # If mapDictionary's next_room[i] and [direction] matches that of the following room[i] found through bfs
                        if mapDictionary[next_room[i]][direction]  == next_room[i + 1]:
                            # print("traversal_path", traversal_path.append(direction))
                            # append the direction to travel_path
                            traversal_path.append(direction)
                            # print("player travel", traversal_path.append(direction))
                            # move player to that room
                            player.travel(direction)
                            # print("player travel", current_room.id)
            else:
                break

            


search(room_graph)
print("Map Graph Dictionary", mapDictionary) 
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

