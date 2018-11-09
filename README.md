# osm-gps
**a3 group** intelligent systems lab project  
> designment and developement of an agent program to find the optimal route for a vehicle that circulates through a set of places of a town using data from open street map - [uclm](https://www.uclm.es/) computer science | [osm](https://www.openstreetmap.org) grahml data

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

## [task1](/reqs/task1.pdf)
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
delivered [task1 documentation](/docs/task1.pdf)  

## [task2](/reqs/task2.pdf)
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

delivered [task2 documentation](/docs/task2.pdf)

## task3
basic version of the [search algorithms][i15]
- breath-first search
- depth-first search, depth-limited search and iterative deepening dearch
- uniform cost

we need all classes defined in **task2** and some input values asked to the user to generate a [txt file][i16] containing a sequence of states corresponding to the path solution if exists for each of the algorithms mentioned before. we have also implemented a [visited list][i17] to be able to tun all the algorithms with pruning whicch makes then much more efficient and fast.

here we have a possible inputs combination to our code and its output file

```python
json file: example
example.json
0: breath-first search
1: depth-first search
2: depth-limited search
3: iterative deepening search
4: uniform cost search
5: a* search
strategy: 0
pruning(y/n): y
breath-first search w/ pruning
depth: 999
data/anchuras.graphml.xml
cost: 690.552000, depth: 12, elapsed time: 0.012542s
check out.txt for more info
```

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
