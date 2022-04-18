'''
     Programming Assignment
     Author: Anthony Khoury

     Description:
          Implementation of a range query algorithm for high dimensional data using 3 strategies:
               1. Sequential Search
               2. KD-Tree
               3. MYkd-tree
'''
#%%
''' ------- Imports & Functions -------'''
import time
from kd_tree import KD_Tree
from MY_KD_tree import MY_KD_Tree
from sequential_search import sequential_search
from support import readDB, readQueries


database_name = "../projDB.txt"
queries_name = '../test2.txt'
index_size = 50


# Database 
db = readDB(database_name)
print("Database Read: Records: " + len(db))

# Queries
queries = readQueries(queries_name)
print("Queries Read: Queries: " + len(queries))


# KD Tree Created
tree = KD_Tree(data=db, index_size=index_size, level = 0)
print("KD Tree Created")


# MY KD Tree Created
# my_kd_tree = MY_KD_Tree(data=db, index_size=index_size)
# print("MY KD Tree Created")



#%%
''' ------- Running Code -------'''

# Search Algorithm Choice: 0, 1, 2
search_algorithm   = 0
sequential_results = []
kd_results         = []
my_kd_results      = []


if (search_algorithm == 0):
     print("Sequential Search:")

     start_time = time.time()
     sequential_search(db, queries)
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)


elif (search_algorithm == 1):
     print("KD Tree Search")
     
     start_time = time.time()
     tree.query_search(queries=queries)
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)


elif (search_algorithm == 2):
     print("MYkd-tree search")
















#%%

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