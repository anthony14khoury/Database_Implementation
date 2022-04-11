# Boolean return: checks if node's values are in the range provided
def in_range(node, range):
     return all(range[:,0] <= node) and all(node <= range[:, 1])

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
     
     def rangesearch(self, range):
          
          # Initialize Node
          node = self.node

          # Range mins and maxes
          xmin, xmax, ymin, ymax = range[0][0], range[0][1], range[1][0], range[1][1]

          # Check if point(s) are in the range
          if in_range(node, range):
               yield node
          
          # Finding the interval we care about (x or y)
          min, max = range[self.level]

          # Grabbing x or y based on the level
          split = node[self.level]

          # Checking if left child exists and node is in the range
          if self.left is not None and split >= min:
               
               # Left child is an array (leaf): yield all values
               if isinstance(self.left, list):
                    for point in self.left:
                         if point[0] >= xmin and point[0] <= xmax and point[1] >= ymin and point[1] <= ymax:
                              yield point
               
               # Recursively Search Left
               else:
                    yield from self.left.rangesearch(range)
          
          # Checking if right child exists and node is in the range
          if self.right is not None and split <= max:

               # Right child is an array (leaf): yield all values
               if isinstance(self.right, list):
                    for point in self.right:
                         if point[0] >= xmin and point[0] <= xmax and point[1] >= ymin and point[1] <= ymax:
                              yield point
               
               # Recursively Search Right
               else:
                    yield from self.right.rangesearch(range)