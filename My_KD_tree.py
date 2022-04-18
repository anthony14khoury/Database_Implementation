import numpy as np

# Boolean return: checks if node's values are in the query provided
def in_query(node, query):
     return all(query[:,0] <= node) and all(node <= query[:, 1])



class My_KD_Tree:

     def __init__(self, data, index_size, level):
         
          # Length of the data
          length_of_data = len(data)

          # Calcualting Max Variance
          variance = []
          temp_data = np.array(data)
          variance.append(np.var(temp_data, 0))
          max_variance = np.argmax(variance)

          # Setting the level to the max variance
          level = max_variance

          # Sort the data to find the median
          data.sort(key = lambda x: x[level])
          
          # Middle point (on the right if length is even)
          middle = length_of_data // 2

          # Grabbing middle point
          self.node = data[middle]

          # Setting class attribute
          self.level = level
          # level = (level + 1) % len(data[0])

          # Initializing left and right nodes
          self.left = None
          self.right = None

          # Split data into left and right
          left_data = data[0 : middle]
          right_data = data[middle + 1 : length_of_data]

          # Recursively calling KD_Tree on left and right children
          if len(left_data) > index_size:
               self.left = My_KD_Tree(data=left_data, index_size=index_size, level=level)
          else:
               self.left = left_data

          if len(right_data) > index_size:
               self.right = My_KD_Tree(data=right_data, index_size=index_size, level=level)
          else:
               self.right = right_data
     
     def createTree(self):
          print("Tree Created!")

     def query_search(self, queries):
          # Open Sequential Search Output File
          with open('./Output/My_KD_Tree_Output.txt', 'w') as file:

               # Loop through all the queries
               for query in queries:
                    kd_results = []

                    # Write the Query to the Output File
                    query_output = 'Query: ' + str(tuple(query)) + '\n'
                    file.write(query_output)

                    
                    # Grab individual query
                    q = [[0,0]]
                    for i in range(0, len(query), 2):
                         q.append([query[i], query[i+1]])
                    q = np.array(q[1:])

                    # Search
                    kd_results = list(self.search(q))

                    kd_results.sort()
                    for report_record in kd_results:
                         # Write Record to Output File
                         temp_report = '\t' + str(list(report_record)) + '\n'
                         file.write(temp_report)
               

     def search(self, query):
          
          # Initialize Node
          node = self.node

          # Check if point(s) are in the query
          if in_query(node, query):
               yield node
          
          # Finding the interval we care about (x or y)
          min, max = query[self.level]

          # Grabbing x or y based on the level
          split = node[self.level]

          # Checking if left child exists and node is in the query
          if self.left is not None and split >= min:
               
               # Left child is an array (leaf): yield all values
               if isinstance(self.left, list):
                    record = self.left
                    check = False

                    for i in range(len(record)):
                         r = record[i]
                         
                         for j in range(len(r)):

                              if query[j][0] <= r[j] and r[j] <= query[j][1]:
                                   check = True
                              else:
                                   check = False
                                   break
               
                         if (check == True):
                              yield r
               
               # Recursively Search Left
               else:
                    yield from self.left.search(query)


          # Checking if right child exists and node is in the query
          if self.right is not None and split <= max:

               # Right child is an array (leaf): yield all values
               if isinstance(self.right, list):
                    record = self.right
                    check = False

                    for i in range(len(record)):
                         r = record[i]
                         
                         for j in range(len(r)):

                              if query[j][0] <= r[j] and r[j] <= query[j][1]:
                                   check = True
                              else:
                                   check = False
                                   break
                    
                         if (check == True):
                              yield r
               
               # Recursively Search Right
               else:
                    yield from self.right.search(query)