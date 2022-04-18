'''
     Programming Assignment
     Author: Anthony Khoury

     Description:
          Implementation of a range query algorithm for high dimensional data using 3 strategies:
               1. Sequential Search
               2. KD-Tree
               3. MYkd-tree
'''

import time
from kd_tree import KD_Tree
from My_KD_tree import My_KD_Tree
from sequential_search import sequential_search
from support import readDB, readQueries

# Command Line Input
question = "\nInput: "
command_line_input = str(input(question))
command_line_input = command_line_input.split(" ")
input_length = len(command_line_input)

if input_length != 3 and input_length != 4:
     print("Incorrect number of parameters entered.")
     exit

else:
     search_algorithm = int(command_line_input[0])
     database_name = command_line_input[1]
     queries_name = command_line_input[2]

     if len(command_line_input) == 4:
          index_size = int(command_line_input[3])


print('\n' + '------- Initializations: -------')

# Database 
db = readDB('./Data/' + database_name)
print('\t' + "Database Read: Records: " + str(len(db)))

# Queries
queries = readQueries('./Queries/' + queries_name)
print('\t' + "Queries Read: Queries: " + str(len(queries)))



print('\n' + '------- Algoritm: -------')

if (search_algorithm == 0):
     print('\t' + "Sequential Search:")

     start_time = time.time()
     sequential_search(db, queries)
     end_time = time.time()
     print('\t' + "Total Duration (s): ", round(end_time - start_time, 4), " seconds")
     print('\t' + "Output file located: ./Output/Sequential_Search_Output.txt" + '\n')


elif (search_algorithm == 1):
     print('\t' + "Creating KD Tree")
     kd_tree = KD_Tree(data=db, index_size=index_size, level = 0)


     print('\t' + "Searching KD Tree")
     start_time = time.time()
     kd_tree.query_search(queries=queries)
     end_time = time.time()
     print('\t' + "Total Duration (s): ", round(end_time - start_time, 4), " seconds")
     print('\t' + "Output file located: ./Output/KD_Tree_Output.txt" + '\n')


elif (search_algorithm == 2):
     print('\t' + "Creating My KD Tree")
     my_kd_tree = My_KD_Tree(data=db, index_size=index_size, level=0)


     print('\t' + "MYkd-tree search")
     start_time = time.time()
     my_kd_tree.query_search(queries=queries)
     end_time = time.time()
     print('\t' + "Total Duration (s): ", round(end_time - start_time, 4), " seconds")
     print('\t' + "Output file located: ./Output/My_KD_Tree_Output.txt" + '\n')