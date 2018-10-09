# osm-gps 
[![HitCount](http://hits.dwyl.io/jupcan/osm-gps.svg)](http://hits.dwyl.io/jupcan/osm-gps) ![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square) ![Pending Pull-Requests](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/pulls.svg?style=flat-square)  
**a3 group** intelligent systems lab project
> designment and developement of an agent program to find the optimal route for a vehicle that circulates through a set of places of a town using data from open street map - [uclm](https://www.uclm.es/) computer science | [osm](https://www.openstreetmap.org) grahml data

## [task1](/reqs/task1.pdf) 
given a file in format grahml, the students must write a class ”graph” containing:
- a constructor, that receives as parameter the name of the file graphml
- methods: belongNode, positionNode and adjacentNode  

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
...
