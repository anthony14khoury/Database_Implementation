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
import sys
import time
import math


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
     
     print("Database Read")
     return database

# Read Queries
def readQueries(queries):
     queries = []
     with open('projquery.txt') as file:
          lines = file.readlines()
     
     for i in range(len(lines)):
          query = lines[i]
          query = query[:-1]
          query = query.split(' ')
          xmin, xmax = int(query[0]), int(query[1])
          ymin, ymax = int(query[2]), int(query[3])
          queries.append((xmin, xmax, ymin, ymax))
     
     print("Queries Read")
     return queries

# Sequentia Search
def sequential_search(db, queries):

     for i in range(queries.shape[0]):
          xmin, xmax, ymin, ymax = queries[i][0], queries[i][1], queries[i][2], queries[i][3]
          print("Query: (", xmin, ",", xmax, ",", ymin, ",", ymax, ")")

          print("Records:")
          for record in range(int(db.shape[0])):
               x, y = db[record][0], db[record][1]

               if (xmin <= x and x <= xmax and ymin <= y and y <= ymax):
                    print( "\t", "(", x, ",", y, ")")
               




#%%
# Command Line Input
# command_line_input = str(sys.argv)
# search_algorithm = int(command_line_input[1])
# database_name = command_line_input[2]
# queries = command_line_input[3]

search_algorithm = 0
database_name = "projDB.gz"
queries_name = 'projquery.txt'

# Initial Database Object
db = np.array(readDB(database_name))

# Read Queries
queries = np.array(readQueries(queries_name))



if (search_algorithm == 0):
     print("Sequential Search:")
     print("__________________")
     start_time = time.time()
     sequential_search(db, queries)
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)

elif (search_algorithm == 1):
     print("kd-tree search")

elif (search_algorithm == 2):
     print("MYkd-tree search")



# %%
