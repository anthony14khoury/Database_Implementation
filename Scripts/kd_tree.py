import numpy as np

# Boolean return: checks if node's values are in the query provided
def in_query(node, query):
     return all(query[:,0] <= node) and all(node <= query[:, 1])

class KD_Tree:

     def __init__(self, data, level = 0, index_size = 50):
          # Length of the data
          length_of_data = len(data)
          
          # Middle point (on the right if length is even)
          middle = length_of_data // 2

          # Sort the data to find the median
          data.sort(key = lambda x: x[level])

          # Grabbing middle point
          self.node = data[middle]

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
          if len(left_data) > index_size:
               self.left = KD_Tree(left_data, level)
          else:
               self.left = left_data

          if len(right_data) > index_size:
               self.right = KD_Tree(right_data, level)
          else:
               self.right = right_data
     
     def createTree(self):
          print("Tree Created!")

     def query_search(self, queries):
          # Open Sequential Search Output File
          with open('../Output/KD_Tree_Output.txt', 'w') as file:
               
               kd_results = []

               # Loop through all the queries
               for i in range(len(queries)):
                    
                    # Grab individual query
                    query = np.array([[queries[i][0], queries[i][1]], [queries[i][2], queries[i][3]]])

                    # Query mins and maxes
                    xmin, xmax, ymin, ymax = query[0][0], query[0][1], query[1][0], query[1][1]

                    # Write the Query to the Output File
                    query_output = 'Query: (' + str(xmin) + ',' + str(xmax) + ',' + str(ymin) + ',' + str(ymax) + ')' + '\n'
                    file.write(query_output)

                    kd_results.append(list(self.search(query)))
                    kd_results[i].sort()
                    for report_record in kd_results[i]:
                         # Write Record to Output File
                         temp_report = '\t' + str(report_record) + '\n'
                         file.write(temp_report)
               
               return kd_results


     def search(self, query):
          
          # Initialize Node
          node = self.node

          # Query mins and maxes
          xmin, xmax, ymin, ymax = query[0][0], query[0][1], query[1][0], query[1][1]

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
                    for record in self.left:
                         if record[0] >= xmin and record[0] <= xmax and record[1] >= ymin and record[1] <= ymax:
                              yield record
               
               # Recursively Search Left
               else:
                    yield from self.left.search(query)
          
          # Checking if right child exists and node is in the query
          if self.right is not None and split <= max:

               # Right child is an array (leaf): yield all values
               if isinstance(self.right, list):
                    for record in self.right:
                         if record[0] >= xmin and record[0] <= xmax and record[1] >= ymin and record[1] <= ymax:
                              yield record
               
               # Recursively Search Right
               else:
                    yield from self.right.search(query)