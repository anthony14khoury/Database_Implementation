'''
     Programming Assignment
     Author: Anthony Khoury

     Description:
          You will implement a range query algorithm for high dimensional data using 3 strategies:
               1. Sequential Search
               2. KD-Tree
               3. MYkd-tree

     How to run the code:
          - 4 Inputs:
               1. Search Algorithm
               2. Database
               3. Queries
'''
#%%
# Imports
import gzip
import numpy as np
import time
from kd_tree import KD_Tree
from MYkd_tree import MY_KD_Tree
from sequential_search import sequential_search


# Reading the Database
def readDB(dbName):
     database = []
     with gzip.open(dbName, 'r') as file:
          for line in file:
               entry = line.decode("utf-8")
               entry = entry[:-1]
               entry = entry.split(',')
               coordinates = (int(entry[0]), int(entry[1]))
               database.append(coordinates)

     return database

# Read Queries
def readQueries(queries_name):
     queries = []
     with open(queries_name) as file:
          lines = file.readlines()
     
     for i in range(len(lines)):
          query = lines[i]
          query = query[:-1]
          query = query.split(' ')
          xmin, xmax = int(query[0]), int(query[1])
          ymin, ymax = int(query[2]), int(query[3])
          queries.append((xmin, xmax, ymin, ymax))
     
     return queries

# Compare the results of the searches
def compare_results(array1, array2):
     x_diff, y_diff = 0, 0
     for i in range(len(array1)):
          for j in range(len(array1[i])):
               x_diff += array1[i][j][0] - array2[i][j][0]
               y_diff += array1[i][j][1] - array2[i][j][1]
     print("X differences: ", x_diff)
     print("Y differences: ", y_diff)


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


database_name = "projDB.gz"
queries_name = 'test2.txt'
index_size = 50

# Database 
db = readDB(database_name)
print("Database Read")

# Queries
queries = readQueries(queries_name)
print("Queries Read")

# KD Tree Created
tree = KD_Tree(db, 0, index_size)
print("KD Tree Created")

# MY KD Tree Created
my_kd_tree = MY_KD_Tree(db, 0, index_size)
print("MY KD Tree Created")



#%%
# Running Code
search_algorithm = 1

sequential_results = []
kd_results = []

if (search_algorithm == 0):
     print("Sequential Search:")
     start_time = time.time()
     
     for i in range(len(queries)):
          query = queries[i]
          print(query)
          sequential_results.append(sequential_search(db, [query]))
     
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)

     for j in range(len(sequential_results)):
          sequential_results[j].sort()


elif (search_algorithm == 1):
     print("KD Tree Search")
     start_time = time.time()

     for i in range(len(queries)):
          query = queries[i]
          print(query)
          tree_query = np.array([[query[0], query[1]], [query[2], query[3]]])
          kd_results.append(list(tree.rangesearch(tree_query)))
     
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)

     for j in range(len(kd_results)):
          kd_results[j].sort()


elif (search_algorithm == 2):
     print("MYkd-tree search")


#%%
# Compare Results
compare_results(sequential_results, kd_results)


#%%