# File: pa3.py
# Author:    
# Date: 
# Description: 

def solve(filename):
    """
    TODO: Write your docstring here (and for any other helper functions!)
    """

    f = open (filename)
    case = 0

    while True:
        # Read in inputs
        nc, nr, n, q = (int(x) for x in f.readline().split())
        
        if nc == 0 and nr == 0 and n == 0 and q == 0:
            break

        case += 1
        print(f"Case {case}:")

        # TODO: do some preprocessing here
        stone_grid = [[0]*1000]*1000
        i_offset = nr - 1
        j_offset = -2
        #read in stone locations and store on grid
        for _ in range(n):
            stone_loc = f.readline().strip().split()
            i = int(stone_loc[0]) - int(stone_loc[1])
            j = int(stone_loc[0]) + int(stone_loc[1])
            stone_grid[i+i_offset][j+j_offset] = 1

        #create memoization count table
        memo = [[0]*((nc-1)+i_offset)] * ((nc + nr) + j_offset)
        i = 0
        j = 0

        while (i < nc-1+i_offset-1 or j < nc+nr+j_offset-1):
            #base case: check if stone is in bottom left corner
            if (i,j) == (0,0):
                if stone_grid[0][0] == 1:
                    memo[0][0] = 1
            else:
                #make upward rectangle (in graph view) by taking smaller square plus row of squares above
                if memo[i-1][j] == 0:
                    memo[i-1][j] = memo[i-1][j-1]
                    for p in range(i-1):
                        memo[i-1][j] += stone_grid[i-1-p][j]
                
                #make sideways rectangle (in graph view) by taking smaller square plus column of squares to the right
                if memo[i][j-1] == 0:
                    memo[i][j-1] = memo[i-1][j-1]
                    for p in range(j-1):
                        memo[i][j-1] += stone_grid[i][j-1-p]
                
                #compute larger square with rectangles and getting rid of duplicates + plus top right corner
                memo[i][j] = memo[i-1][j] + memo[i][j-1] - memo[i-1][j-1] + stone_grid[i][j]
            
            if i < nc-1+i_offset-1:
                i += 1
            if j < nc+nr+j_offset-1:
                j += 1
        
        # Handle queries
        for _ in range(q):
            query = int(f.readline().strip())
            best_count, best_loc = 0, (None, None) # TODO: change this
            
            # TODO: for each query, find the max count of points here
                    
            print(f"{best_count} ({best_loc[0]},{best_loc[1]})")

            
if __name__ == "__main__":
    solve("test1.in")

