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

# Sequential Search
def sequential_search(db, queries):

     for i in range(queries.shape[0]):
          xmin, xmax, ymin, ymax = queries[i][0], queries[i][1], queries[i][2], queries[i][3]
          print("Query: (", xmin, ",", xmax, ",", ymin, ",", ymax, ")")

          print("Records:")
          for record in range(int(db.shape[0])):
               x, y = db[record][0], db[record][1]

               if (xmin <= x and x <= xmax and ymin <= y and y <= ymax):
                    print( "\t", "(", x, ",", y, ")")


def split_array(arr, cond):
  return [arr[cond], arr[~cond]]


class Node:

     x: int
     y: int
     block_left: np.array([])
     block_right: np.array([])


# Command Line Input
# command_line_input = str(sys.argv)
# search_algorithm = int(command_line_input[1])
# database_name = command_line_input[2]
# queries = command_line_input[3]

search_algorithm = 0
database_name = "projDB.gz"
queries_name = 'projquery.txt'

# Initial Database Object
db = readDB(database_name)

# Read Queries
queries = readQueries(queries_name)




# %%
# KD Tree Implementation

def inbox(p, box):
     return all(box[:,0] <= p) and all(p <= box[:, 1])

class KD_Tree:

     def __init__(self, data, level = 0):
          # Length of the data
          length_of_data = len(data)
          
          # Middle point (on the right if length is even)
          middle = length_of_data // 2

          # Sort the data to find the median
          data.sort(key = lambda x: x[level])

          # Grabbing middle point
          self.point = data[middle]

          # Setting class attribute
          self.level = level
          level = (level + 1) % len(data[0])

          # Initializing left and right nodes
          self.left = None
          self.right = None

          # Split data into left and right
          left_data = data[0 : middle]
          right_data = data[middle + 1 : length_of_data]

          # Recursively calling KD_Tree on left and right children
          if middle > 0:
               self.left = KD_Tree(left_data, level)
          if length_of_data - (middle + 1) > 0:
               self.right = KD_Tree(right_data, level)
     
     def rangesearch(self, box):
          p = self.point
          if inbox(p, box):
               yield p
          min, max = box[self.level]
          split = p[self.level]
          if self.left is not None and split >= min:
               yield from self.left.rangesearch(box)
          if self.right is not None and split <= max:
               yield from self.right.rangesearch(box)

     

data = [(14, 16), (9, 18), (15, 13), (8, 3), (4, 7)]
tree = KD_Tree(data)
query = np.array([[0, 4], [0, 9]])
print(list(tree.rangesearch(query)))



#%%

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



#%%