# File: pa3.py
# Author: Daniel Daugbjerg and Evan Scott
# Date: April 12, 2024
# Description: 
import math
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
        stone_grid = [[0]*1000 for _ in range(1000)]
        i_offset = nr - 1
        j_offset = -2
        #read in stone locations and store on grid
        for _ in range(n):
            stone_loc = f.readline().strip().split()
            i = int(stone_loc[0]) - int(stone_loc[1])
            j = int(stone_loc[0]) + int(stone_loc[1])
            stone_grid[i+i_offset][j+j_offset] = 1

        #create memoization count table
        memo = [[0 for _ in range((nc-1)+i_offset)] for _ in range((nc + nr) + j_offset)]
       
        for i in range(nc-1+i_offset):
            for j in range((nc + nr) + j_offset):
                #base case: check if stone is in bottom left corner
                if i == 0 and j == 0:
                    memo[i][j] = stone_grid[i][j]
                elif i == 0:
                    memo[i][j] = stone_grid[i][j] + memo[i][j - 1]
                elif j == 0:
                    memo[i][j] = stone_grid[i][j] + memo[i - 1][j]
                #compute larger square with rectangles and getting rid of duplicates + plus top right corner
                else:
                    memo[i][j] = stone_grid[i][j] + memo[i - 1][j] + memo[i][j - 1] - memo[i - 1][j - 1]

        #for i in memo:
            #print(i)
        # Handle queries
        for _ in range(q):

            query = int(f.readline().strip())
            best_count = 0
            best_loc = (0,0)
            #look through each square in count table grid
            #figure out what the length sides of the square are
            for r in range(len(memo)):
                for c in range(len(memo[r])):
                    #compute desired square
                    total_square = memo[r][c]
                    if r >= query*2:
                        left_rect = memo[r-query*2][c]
                    else:
                        left_rect = 0
                    if c >= query*2:
                        right_rect = memo[r][c-query*2]
                    else:
                        right_rect = 0
                    if r >= query*2 and c >= query*2:
                        smaller_square = memo[r-query*2][c-query*2]
                    else:
                        smaller_square = 0
                    #print(str(total_square)+" "+str(left_rect)+" "+str(right_rect)+" "+str(smaller_square))
                    #replace values if larger count found
                    if best_count <= (total_square-right_rect-left_rect+smaller_square):
                        best_count = (total_square-right_rect-left_rect+smaller_square)
                        #need to translate back to (r,c)
                        r_translated = r-i_offset-query
                        c_translated = c-j_offset-query
                        y = (r_translated+c_translated)//2
                        x = (r_translated-c_translated)//-2
                        best_loc = (x,y)


                    
            print(f"{best_count} ({best_loc[0]},{best_loc[1]})")

            
if __name__ == "__main__":
    solve("test1.in")

