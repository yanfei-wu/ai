# Traveling Salesman

In this project,  simulated annealing algorithm is implemented to solve the Traveling Salesman Problem between US state capitals. Simulated annealing is a probablistic technique used for finding an approximate solution to an optimization problem. The Traveling Salesman Problem is an optimization problem that seeks to find the shortest path passing through every city exactly once. Here, the path is defined to start and end in the same city, i.e., a closed loop path. 

Also, four different cooling schedule functions are compared, including linear, exponential, quadratic, and logarithmical functions, in terms of the run time and final path length after simulated annealing. With the specific search space in this problem (maximum 30 capital cities), there is no significant difference in run time. Among the four functions compared, quadtratic function gives the least optimization in final path length. 

