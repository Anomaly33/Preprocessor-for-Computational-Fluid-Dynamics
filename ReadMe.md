# Description of the Code

The main aim of a preprocessor is to extract the following information from the given grid data:

1. The number of edges in the domain.
2. Left and right neighbors of each edge in the domain.
3. Edges situated at the boundary of the domain.
4. Neighbors of each node in the domain.
5. Neighboring triangles of each triangular element in the domain.
6. Number of triangles sharing a common node in the domain.
7. Area of each triangular element in the domain.
8. The outward normal of each edge in the domain.

Each of the data mentioned above is used by the CFD solver to solve the given equation numerically.
