'''
     Programming Assignment
     Author: Anthony Khoury

     Description:
          You will implement a range query algorithm for high dimensional data using 3 strategies:
               1. Sequential Search
               2. KD-Tree
               3. MYkd-tree
'''
#%%
# Imports
import numpy as np
import time
from kd_tree import KD_Tree
from MYkd_tree import MY_KD_Tree
from sequential_search import sequential_search
from support import readDB, readQueries, compare_results



# Command Line Input
# command_line_input = str(input())
# command_line_input = command_line_input.split(" ")
# if (len(command_line_input) == 3):
#      search_algorithm = int(command_line_input[0])
#      database_name = command_line_input[1]
#      queries_Name = command_line_input[2]
# elif (len(command_line_input) == 4):
#      search_algorithm = int(command_line_input[0])
#      database_name = command_line_input[1]
#      queries = command_line_input[2]
#      index_size = int(command_line_input[3])


database_name = "../projDB.txt"
queries_name = '../projquery.txt'
index_size = 50

# Database 
db = readDB(database_name)
print("Database Read")

# Queries
queries = readQueries(queries_name)
print("Queries Read")

# KD Tree Created
tree = KD_Tree(data=db, level=0, index_size=index_size)
print("KD Tree Created")

# MY KD Tree Created
# my_kd_tree = MY_KD_Tree(db, 0, index_size)
# print("MY KD Tree Created")



#%%
# Running Code

search_algorithm = 1     # Search Algorithm Choice: 0, 1, 2

sequential_results = []  # Sequential Search Results
kd_results = []          # KD Tree Search Results
my_kd_results = []       # MY KD Tree Search Results


# Sequential Search
if (search_algorithm == 0):
     print("Sequential Search:")

     # Start Stopwatch
     start_time = time.time()

     sequential_results.append(sequential_search(db, queries))
     
     # Stop Stopwatch
     end_time = time.time()
          
     print("Total Duration (s): ", end_time - start_time)


# KD Tree Search
elif (search_algorithm == 1):
     print("KD Tree Search")

     # Start Stopwatch
     start_time = time.time()
     
     kd_results.append(list(tree.query_search(queries=queries)))

     # Stop Stopwatch
     end_time = time.time()

     print("Total Duration (s): ", end_time - start_time)




elif (search_algorithm == 2):
     print("MYkd-tree search")


#%%
# Compare Results
# compare_results(sequential_results, kd_results)


#%%