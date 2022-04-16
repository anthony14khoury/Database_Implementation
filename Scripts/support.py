

# Reading the Database
def readDB(dbName):
     database = []
     with open(dbName) as file:
          for line in file:
               entry = line[:-1]
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