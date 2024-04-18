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

        i_offset = nr - 1
        j_offset = -2
        stone_grid = [[0 for _ in range(2000)] for _ in range(2000)]
        #read in stone locations and store on grid
        for _ in range(n):
            stone_loc = f.readline().strip().split()
            i = int(stone_loc[0]) - int(stone_loc[1])
            j = int(stone_loc[0]) + int(stone_loc[1])
            stone_grid[i+i_offset][j+j_offset] = 1

        #create memoization count table
        memo = [[0 for _ in range((nc-1)+i_offset+1)] for _ in range((nc + nr) + j_offset+1)]
       
        for i in range(nc-1+i_offset+1):
            for j in range((nc + nr) + j_offset+1):
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

        # Handle queries
        for _ in range(q):

            query = int(f.readline().strip())
            best_count = 0
            best_loc = (2000,2000)
            #look through each square in count table grid
            #figure out what the length sides of the square are
            for j in range(len(memo)):
                for i in range(len(memo[j])):
                    #compute desired square
                    
                    #get max i and j value to use for square
                    max_j = min(len(memo)-1,j+query)
                    max_i = min(len(memo[j])-1, i+query)
                    
                    total_square = memo[max_i][max_j]
                   
                   #get min i and j value to use for cutting off square
                    min_j = max(j-query,0)
                    min_i = max(i-query, 0)
                    
                    if min_i == 0:
                        bottom_rect = 0
                    else:
                        bottom_rect = memo[min_i-1][max_j]
                    
                    if min_j == 0:
                        left_rect = 0
                    else:
                        left_rect = memo[max_i][min_j-1]
                    
                    if min_j == 0 or min_i == 0:
                        smaller_square = 0
                    else:
                        smaller_square = memo[min_i-1][min_j-1]
                    
                    #translate values
                    j_translated = j-j_offset
                    i_translated = i-i_offset
                    c = (j_translated+i_translated)//2
                    r = (j_translated-i_translated)//2

                    #check if count is larger and point is within parameters
                    if (j_translated+i_translated)%2 == 0 and (j_translated-i_translated)%2 == 0 and r <= nr and r >= 1 and c <= nc and c >= 1:
                        if best_count < (total_square-left_rect-bottom_rect+smaller_square):
                            #need to translate back to (c,r)
                            best_loc = (c,r)
                            best_count = (total_square-left_rect-bottom_rect+smaller_square)
                        
                        #prioritize smallest index
                        elif best_count == (total_square-left_rect-bottom_rect+smaller_square):
                            if r<best_loc[1]:
                                best_loc = (c,r)
                            elif r == best_loc[1] and c <best_loc[0]:
                                best_loc = (c,r)


                    
            print(f"{best_count} ({best_loc[0]},{best_loc[1]})")

            
if __name__ == "__main__":
    solve("test1.in")

