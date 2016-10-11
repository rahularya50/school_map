"""
corridors, staircases, edges
"""

from graph import *
from elements import *
from graph_operations import *

# Initialization

location_dict = {}
staircase_dict = {}
corridors = []

# Make the Link Block!

link_block = [["L02", "AC1", "AC2", "AS1", "AS2"],
              ["ICT4", "ICT3", "ICT2", "ICT1", "AS4", "AS5"],
              ["EN201", "EN202", "EN203", "English Office", "EN204", "EN205", "EN206"],
              ["EN301", "EN302", "EN303", "EN304", "EN305", "EN306", "EN307", "EN308"],
              ["MA401", "MA402", "MA403", "MA404", "MA405", "MA406", "MA407"],
              ["MA501", "MA502", "MA503", "Maths Office", "MA504", "MA505", "MA506"]]

for i in range(6):
    corridors.append(Corridor(link_block[i], 10, location_dict, 1))

location_dict["Link Block Intersection"] = Node("the intersection", [])
corridors[1].nodes.insert(5, location_dict["Link Block Intersection"])

s1 = Staircase("Link Block Staircase", 7, 0)
s2 = Staircase("Link Block Staircase", 7, 0)  # TODO: Add AS3 + Terrace

staircase_dict["Link Block 1"] = s1
staircase_dict["Link Block 2"] = s2

for i in range(6):
    make_edge(s1.nodes[i], s2.nodes[i], corridors[i])

# Make the Science Block!

corridors = []

science_block = [["GLT"],
                 ["SC101", "Prep Room", "SC102", "SC103"],
                 ["Sci-New Block Passthrough", "SC201", "SC202", "SC203"],
                 ["ME2", "SC301", "Prep Room", "SC302", "SC303"],
                 ["Science Office", "SC401", "SC402", "SC403", "SC404"],
                 ["ME1", "SC501", "Prep Room", "SC502", "SC503"],
                 ["Science Block Garden"]]  # TODO: Add new block access and ME1/2 + Science Office routing

for i in range(1, 7):
    corridors.append(Corridor(science_block[i], 10, location_dict, 1))

s1 = Staircase("Science Block Staircase", 7, 3)
s2 = Staircase("Science Block Staircase", 7, 1)

location_dict["GLT"] = Node("GLT", [])
make_edge(location_dict["GLT"], s2.nodes[0], Edge([], "open space", 10, 1))

staircase_dict["Science Block 1"] = s1
staircase_dict["Science Block 2"] = s2

for i in range(6):
    make_edge(s1.nodes[i], s2.nodes[i], corridors[i])

make_edge(None, s2.nodes[0], corridors[0])

# Make the Language Block! TODO: Add Language Block extension + second staircase

corridors = []

language_block = [["the ICT Helpdesk", "W1", "W2"],
                  ["G1", "G2", "F1"],
                  ["the Language Office", "LA201", "LA202", "LA203", "LA204"],
                  ["LA301", "LA302", "LA303", "LA304", "LA305", "LA306"]]

for i in range(4):
    corridors.append(Corridor(language_block[i], 10, location_dict, 0))

s1 = Staircase("Language Block Staircase", 4, 3)
staircase_dict["Language Block 1"] = s1

for i in range(4):
    make_edge(s1.nodes[i], None, corridors[i])

# Link the Language Block with the Link Block and Science Blocks!

for i in range(4):
    make_edge(None, InvisibleNode("Language Block Link Node", []), corridors[i])
    make_edge(corridors[i].nodes[-1], staircase_dict["Link Block 1"].nodes[i], Edge(None, "bridge", 10, 1))

make_edge(location_dict["Sci-New Block Passthrough"], None, corridors[3])

# Make the Peel Block!

corridors_1, corridors_2, corridors_3 = [], [], []

peel_block = [[["LPS", "Middle School Office", "Reprographics"], ["Staffroom", "Foyer", "Offices + SLT", "Board Room"],
               ["Careers Office", "SSC 5", "SSC 4", "SSC 3"]],
              [["Media Center", "Reading Center"],
               ["LRC (middle school section)", "LRC Canteen", "LRC (senior school section)"],
               ["Senior School Office", "SSC 2", "SSC 1"]]]

corridors_1.append(Corridor(peel_block[0][0], 10, location_dict, 2))
corridors_1.append(Corridor(peel_block[1][0], 10, location_dict, 2))

corridors_2.append(Corridor(peel_block[0][1], 10, location_dict, 1))
corridors_2.append(Corridor(peel_block[1][1], 10, location_dict, 1))

corridors_3.append(Corridor(peel_block[0][2], 10, location_dict, 0))
corridors_3.append(Corridor(peel_block[1][2], 10, location_dict, 0))

s1_0 = StairJunction(0, [corridors_2[0]])
s1_1 = StairJunction(1, [corridors_1[1]])

s2_0 = StairJunction(0, [corridors_2[0]])
s2_1 = StairJunction(1, [corridors_3[1]])

s1 = Edge([s1_0, s1_1], "Peel Block Staircase", 6, 3)
s2 = Edge([location_dict["Foyer"], location_dict["LRC Canteen"]], "Foyer Staircase", 6, 1) # TODO: Make Staircase?
s3 = Edge([s2_0, s2_1], "Peel Block Staircase", 6, 1)

s1_0.add_edge(s1)
s1_1.add_edge(s1)

location_dict["Foyer"].add_edge(s2)
location_dict["LRC Canteen"].add_edge(s2)

s2_0.add_edge(s3)
s2_1.add_edge(s3)

c1_0 = InvisibleNode("Peel Block Corner Node 10", [corridors_1[0], corridors_2[0]])
c1_1 = InvisibleNode("Peel Block Corner Node 11", [corridors_1[1], corridors_2[1]])
c2_0 = InvisibleNode("Peel Block Corner Node 20", [corridors_2[0], corridors_3[0]])
c2_1 = InvisibleNode("Peel Block Corner Node 21", [corridors_2[1], corridors_3[1]])

corridors_1[0].add_nodes(c1_0)
corridors_1[1].add_nodes([s1_1, c1_1])

make_edge(s1_0, s2_0, corridors_2[0])
make_edge(c1_0, c2_0, corridors_2[0])
make_edge(c1_1, c2_1, corridors_2[1])

make_edge(c2_0, None, corridors_3[0])
make_edge(s2_1, None, corridors_3[1])
make_edge(c2_1, None, corridors_3[1])

peel_end_node_1 = InvisibleNode("Peel Block Link Node 1", [])
make_edge(peel_end_node_1, None, corridors_1[1])
make_edge(location_dict["Link Block Intersection"], peel_end_node_1, Edge([], "bridge", 5, 2))

# Testing :(

print("\n".join(
    str(i) for i in gen_desc(path_finder(location_dict["GLT"], location_dict["SSC 3"]))))
