# [osm-gps](/doc/osm-gps.pdf)
[![uclm](https://img.shields.io/badge/uclm-project-red.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAC9UlEQVR42o3S3UtTYRwH8F//QhBE3WT0elGr6CZUCLzoRUQt6ibICrESS1MDi7pJwcSXgsCGlG+1LFFzzpzONqduTp3TqVO36V7OzubZ2TznbDvn7NW5nmlXWdADPzg8/D6c3/N9HohSDPCrDgg53bDJByERj0OEpCCEE8cjXlrJaBbOcys2iHpp1OOBgN4MaG/b/BXHfKxgkwuaNvkQE6X8WNDiTI16qP/AicTlMElPeeXTtdTY7G1Kpa/iLU5dnONvhHDyH9hBJGEGu2RV2t93PWaXrb2xAO/kTJgMb5EUM9MGWZQJ5PrnTH9gMwYx2n865PLOrr5uK+XXcLV/YfUD3t5fFFgwN0Y89JzlTUcxb3PNc2YsjVHrdzAKBX1gh+KhsIXokgtJqbopxvIvEa7y600i38xSnXd4qpwa1zcTvcqGqNdHMBPzpzijHSDGcic2WV4Xj0QTGwptBd4meejTGb+gKcS+acMD1mj7Ro3OfcWE3fddnbJnKMRExMuYglbXWUCjjCTQitEBu2dQU05rFp6gsOrJftXzqI9d8gxpajzDk9XUqK6MVs+Xx9igLtnPmewz4GiRnEFprmxtbSXWO4crUCgVrs7hfDTyeLIpiBG29a6fBTxGlPkX116grQBrwnBHq+QCOD9LwflpQIDSNVAjM8IQSVWQfWN1lgZRQRLjH8WF7h5FJW9brww63I2c2WG0N/WkOUVSAHJADZ6BCXAIu/eiP9ehs79Do97xzxrbk5hdsYo9UlVejAnU0lOGFnvT932ubsW2A01WMUxml8Bo2l3QZD7ai+6wnLc5XyGnSuyslTC5UYOOUTJz/enBifR80GaXgjanDGAoJRMGU67Cj/0ZMJZ+DyzVrYdplT4PocXf2B4wWIrwVslJzcUCkB+4AiNHc1HlAMgFN7dr6EgWqC8VgrVeBI7mPkBPUZuUYfeGlehR7HGhbKYzi0F57BqMn7uVrN3Y9rYD0HMEontE4NMuK7yyyVS3WAmujqFd+Bcdh3NlWlsAggAAAABJRU5ErkJggg==&longCache=true&colorA=b30135&colorB=555555&style=for-the-badge)](https://www.uclm.es)

**a3 group** intelligent systems lab project  
> designment and developement of an agent program to find the optimal route for a vehicle that circulates through a set of places of a town using data from openstreetmap - [uclm](https://www.uclm.es/) computer science | [osm](https://www.openstreetmap.org) grahml data

## installation
whole project developed using **python3**
```
sudo apt-get install python3.6
```

using **lxml library** to represent the xml files data in a tree an then generate our own internal representation of it
```
sudo apt-get install python3-lxml
```

and also **sorted containers** one to use some of the data structures it offers such as ordered dictionaries
```
python3 -m pip install sortedcontainers
```

## [task1](https://github.com/jupcan/osm-gps/tree/task1)
generation of a internal representation of a graph with geographical data from osm
given a file in format grahml
- a **[constructor][i5]**, that receives as parameter the name of the file graphml
- methods: **[belongNode][i6]**, **[positionNode][i7]** and **[adjacentNode][i8]**

below we are showing a command line output example for the 3 aforementioned methods:

```python
file: ciudad real
ciudad real.graphml.xml
nodes: 796725819,765309509,827212358
True
[('38.9845189', '-3.9145536')]
{('796725819', '764039286'): ('Avenida de Europa', '4.148'),
 ('796725819', '797147422'): ('Calle Santa María de Alarcos', '9.129')}
0.0005040168762207031 seconds
True
[('38.9849254', '-3.9246998')]
{('765309509', '803292210'): ('Calle de la Mata', '38.067')}
0.0003075599670410156 seconds
True
[('38.9828974', '-3.9395137')]
{('827212358', '827212360'): ('Calle Goya', '47.442'),
 ('827212358', '827212476'): ('Calle Atalaya', '42.912')}
0.0003237724304199219 seconds
```

## [task2](https://github.com/jupcan/osm-gps/tree/task2)
definition of the problem and implementation of the frontier
- creation and organization of the code in more detailed classes: **[state][i10]**, **[state space][i11]**, **[frontier][i14]**, **[treeNode][i13]** and **[problem][i12]**
- use of new technologies such as .json and .md5 for some inputs/outputs of certain classes  

given an json file used as input to initialize our problem class:
```json
{
	"graphlmfile": "Ciudad Real/data/anchuras.graphml",
	"IntSt":{
			"node": "4331489739",
			"listNodes":["4331489528","4331489668","4331489711","4762868815","4928063625"],
			"id": "f4b616551965fb586e608397c308bf0f"
	}
}
```
we create a *stateSpace class* instance with the given path and read all the information stored in the graphml file so as to be able to compute all the operations we already were able to do in **[task1](/reqs/task1.pdf)**. we also create a *state class* instance with all the other information (node, listNodes, id) to have a start point and be able to make some other new operations:
- **successors(*state*)**: [(acc1,NewState1,costAct1), ... ,(accM,NewStateM,costActM)]; accM = string like 'I am in id origin and I go to id destionation'. NewStateM = adjacent node. costActM = street length
- **belongNode(*state*)**: true or false if it belongs or not to state space
- **creation of frontier** as well as insertion of *treeNodes objects*, elimination and checking emptiness on it

below we are showing a command line output example for the 3 aforementioned methods:
```python
json file: example
example.json
data/anchuras.graphml.xml
[(127.1360111900787, <treeNode.treeNode object at 0x7f33cc1c8fd0>), (591.7378136374725, <treeNode.treeNode object at 0x7f33cc1d9e80>), (612.2393770939552, <treeNode.treeNode object at 0x7f33cc1d9e10>)]
[(591.7378136374725, <treeNode.treeNode object at 0x7f33cc1d9e80>), (612.2393770939552, <treeNode.treeNode object at 0x7f33cc1d9e10>)]
True
4331489738 state md5: 331b41c249f9d392954ce4a36df65ca7
4331489740 state md5: 229da16d1c640e1e81747a47bdd716fa
4331489763 state md5: 6d7014c2db65e030d3ae0af84286edfe
[("I'm in 4331489739 and I go to 4331489738", "(4331489738, ['4331489528', '4331489668', '4331489711', '4762868815', '4928063625'])", '48.137'), ("I'm in 4331489739 and I go to 4331489740", "(4331489740, ['4331489528', '4331489668', '4331489711', '4762868815', '4928063625'])", '108.841'), ("I'm in 4331489739 and I go to 4331489763", "(4331489763, ['4331489528', '4331489668', '4331489711', '4762868815', '4928063625'])", '63.11')]
```
that is, for the initial state we look for its succesors updating each time the state by checking if the node im at the moment is in the state space and removing it from the list if so. also generating the new md5 representation of each state and printing the frontier of the problem once inserting three treeNode object examples and removing one of them.

## [task3](https://github.com/jupcan/osm-gps/tree/task3)
basic version of the [search algorithms][i15]
- breath-first search
- depth-first search, depth-limited search and iterative deepening dearch
- uniform cost

we need all classes defined in **task2** and some input values asked to the user to generate a [txt file][i16] containing a sequence of states corresponding to the path solution if exists for each of the algorithms mentioned before. we have also implemented a [visited list][i17] to be able to run all the algorithms with pruning which makes them much more efficient and fast.

here we have a possible inputs combination to our code and its corresponding output file

```python
json file: example
example.json
0: breath-first search
1: depth-first search
2: depth-limited search
3: iterative deepening search
4: uniform cost search
strategy: 0
pruning(y/n): y
breath-first search w/ pruning
depth: 999
data/anchuras.graphml.xml
cost: 690.552, depth: 13, spatialcxty: 183, temporalcxty: 0.016545s
check out.txt for more info
```

```txt
output.txt
cost: 690.552, depth: 13, spatialcxty: 183, temporalcxty: 0.016545s
goal node: <treeNode.treeNode object at 0x7fc831f3bd68> - 4331489668
time and date: 19:39:02-19/11/2018

["I'm in 4331489739 and I go to 4331489738 c/Barrio Nuevo",
 "I'm in 4331489738 and I go to 4331489532 c/Barrio Nuevo",
 "I'm in 4331489532 and I go to 0946409139 c/sinNombre",
 "I'm in 0946409139 and I go to 4331489528 c/sinNombre",
 "I'm in 4331489528 and I go to 4331489718 c/Calle Arroyo",
 "I'm in 4331489718 and I go to 4331489716 c/Calle Arroyo",
 "I'm in 4331489716 and I go to 4331489709 c/Plaza España",
 "I'm in 4331489709 and I go to 4331489549 c/Calle Amirola",
 "I'm in 4331489549 and I go to 4331489550 c/Calle José María del Moral",
 "I'm in 4331489550 and I go to 4331489692 c/Calle José María del Moral",
 "I'm in 4331489692 and I go to 4331489662 c/Calle Periodista Antonio Herrero",
 "I'm in 4331489662 and I go to 4331489668 c/Calle Periodista Antonio Herrero"]
```
the generated file includes the cost of the solution, the depth where it is found and the time spent to reach it alongside all the actions path printed in order; i go from node1 to node2 and so on until we have passed throught all the desired nodes and reached the goal applying the given algorithm, if no solution is found an error is printed instead both on console and file.

## [task4](https://github.com/jupcan/osm-gps/tree/task4)

addition of **greedy** and __a*__ searches using as heuristic for a concrete state: _h(state) = minimum distance_ between the osm node of current state and any node in the list of nodes to be traveled (computed by means of straight line distance in meters).

as an added feature, we have also generated a sequence of images representing the solution, that is, for a given algorithm solution we are creating a **[gpx][i18]** file, representing it as a track and adding as waypoints the nodes we have to go through, that can be shown graphically in multiple [track drawing websites][i19], different [software][i20] or uploaded directly to [openstreetmap][i22] as stated in osm wiki. finally we are also generating a locally stored [svg image](solu/out.svg) as a way to see a _more human friendly_ representation of the solution, it is computed converting the previous gps file with [gpx2svg][i21] os script, shoutout to its creator.

>![sol on gpx visualizer](solu/out.gif)
a* search algorithm output as gpx for [problema.json](json/problema.json) file shown in [gpx visualizer][i23] website

## task5

as a final task, we have implemented the use of a new heuristic(h0) better than the one we have had until now(h1)

given a state **(x, [a, b, c])**:
- h1 = [min_distance][i24]((x, a),(x, b),(x, c))
- h0 = h1 + [min_distance][i24]((a, b), (a, c))

by adding another minimum distance with current node the first one to be visited, we obtain  a bigger heuristic closer to the real cost of the path thus a better one to consider, we can appreciate a spacial complexity smaller when running the program.

delivered [final documentation](/doc/osm-gps.pdf)

[i5]: https://github.com/jupcan/osm-gps/issues/5
[i6]: https://github.com/jupcan/osm-gps/issues/6
[i7]: https://github.com/jupcan/osm-gps/issues/7
[i8]: https://github.com/jupcan/osm-gps/issues/8
[i10]: https://github.com/jupcan/osm-gps/issues/10
[i11]: https://github.com/jupcan/osm-gps/issues/11
[i12]: https://github.com/jupcan/osm-gps/issues/12
[i13]: https://github.com/jupcan/osm-gps/issues/13
[i14]: https://github.com/jupcan/osm-gps/issues/14
[i15]: https://github.com/jupcan/osm-gps/issues/19
[i16]: https://github.com/jupcan/osm-gps/issues/20
[i17]: https://github.com/jupcan/osm-gps/issues/22
[i18]: https://wiki.openstreetmap.org/wiki/GPX
[i19]: https://wiki.openstreetmap.org/wiki/Track_drawing_websites
[i20]: https://wiki.openstreetmap.org/wiki/Software
[i21]: https://nasauber.de/opensource/gpx2svg/
[i22]: https://www.openstreetmap.org
[i23]: http://www.gpsvisualizer.com
[i24]: https://github.com/jupcan/osm-gps/issues/26
