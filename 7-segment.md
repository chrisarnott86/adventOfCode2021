0: 6
1: 2 *
2: 5
3: 5
4: 4 *
5: 5
6: 6
7: 3 *
8: 7 *
9: 6

[1,4,7,8]
6: has 6 bits not contain 1 [1,4,7,8,6]
3: has 5 bits and contains 7 [1,4,7,8,6,3]
5: has 5 bits and contains (3+4)-1 [1,4,7,8,6,3,5]
2: has 5 bits and contains 8-(3+5) [1,4,7,8,6,3,5,2]
0: has 6 bits and contains 1+(8-3) [1,4,7,8,6,3,5,2,0]
9: has 6 bits and contains 4 [1,4,7,8,6,3,5,2,0]
