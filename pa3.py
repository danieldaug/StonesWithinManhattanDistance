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
        stone_locs = []
        for _ in range(n):
            stone_loc = f.readline().strip().split()
            i = int(stone_loc[0]) - int(stone_loc[1])
            j = int(stone_loc[0]) + int(stone_loc[1])
            stone_locs.append((i,j))

        # Handle queries
        for _ in range(q):
            query = int(f.readline().strip())
            best_count, best_loc = 0, (None, None) # TODO: change this
            
            # TODO: for each query, find the max count of points here
                    
            print(f"{best_count} ({best_loc[0]},{best_loc[1]})")

            
if __name__ == "__main__":
    solve("test1.in")

