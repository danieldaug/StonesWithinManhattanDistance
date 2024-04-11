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
        if j < len(memo) and memo[i-1][j] == 0:
                memo[i-1][j] = memo[i-1][j-1]
                for p in range(i-1):
                    memo[i-1][j] += stone_grid[i-1-p][j]
        if i < len(memo) and memo[i][j-1] == 0:
                    memo[i][j-1] = memo[i-1][j-1]
                    for p in range(j-1):
                        memo[i][j-1] += stone_grid[i][j-1-p]


        print(memo)
        # Handle queries
        for _ in range(q):

            query = int(f.readline().strip())
            best_count = 0
            best_loc = (0,0)
            #look through each square in count table grid
            #figure out what the length sides of the square are
            for r in range(query, len(memo)):
                for c in range(query, len(memo[r])):
                    #compute desired square
                    total_square = memo[r][c]
                    left_rect = memo[r-query][c]
                    right_rect = memo[r][c-query]
                    smaller_square = memo[r-query][c-query]
                    #replace values if larger count found
                    if best_count < (total_square-right_rect-left_rect+smaller_square):
                        best_count = (total_square-right_rect-left_rect+smaller_square)
                        #need to translate back to (r,c)
                        best_loc = (((r-query//2) + (c-query//2))*2, ((c-query//2) - (r-query//2))*2)


                    
            print(f"{best_count} ({best_loc[0]},{best_loc[1]})")

            
if __name__ == "__main__":
    solve("test1.in")

