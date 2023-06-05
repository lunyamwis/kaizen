"""
F. Random Walk
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a tree consisting of n
 vertices and n−1
 edges, and each vertex v
 has a counter c(v)
 assigned to it.

Initially, there is a chip placed at vertex s
 and all counters, except c(s)
, are set to 0
; c(s)
 is set to 1
.

Your goal is to place the chip at vertex t
. You can achieve it by a series of moves. Suppose right now the chip is placed at the vertex v
. In one move, you do the following:

choose one of neighbors to
 of vertex v
 uniformly at random (to
 is neighbor of v
 if and only if there is an edge {v,to}
 in the tree);
move the chip to vertex to
 and increase c(to)
 by 1
;
You'll repeat the move above until you reach the vertex t
.

For each vertex v
 calculate the expected value of c(v)
 modulo 998244353
.

Input
The first line contains three integers n
, s
 and t
 (2≤n≤2⋅105
; 1≤s,t≤n
; s≠t
) — number of vertices in the tree and the starting and finishing vertices.

Next n−1
 lines contain edges of the tree: one edge per line. The i
-th line contains two integers ui
 and vi
 (1≤ui,vi≤n
; ui≠vi
), denoting the edge between the nodes ui
 and vi
.

It's guaranteed that the given edges form a tree.

Output
Print n
 numbers: expected values of c(v)
 modulo 998244353
 for each v
 from 1
 to n
.

Formally, let M=998244353
. It can be shown that the answer can be expressed as an irreducible fraction pq
, where p
 and q
 are integers and q≢0(modM)
. Output the integer equal to p⋅q−1modM
. In other words, output such an integer x
 that 0≤x<M
 and x⋅q≡p(modM)
.

Examples
input
3 1 3
1 2
2 3
output
2 2 1
input
4 1 3
1 2
2 3
1 4
output
4 2 1 2
input
8 2 6
6 4
6 2
5 4
3 1
2 3
7 4
8 2
output
1 3 2 0 0 1 0 1
"""


def random_walk():
    pass
