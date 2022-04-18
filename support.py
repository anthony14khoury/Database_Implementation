# Read Database
def readDB(dbName):
     database = []
     with open(dbName) as file:
          for line in file:
               entry = line[:-1]
               entry = entry.split(',')
               coordinates = tuple(map(int, entry))
               database.append(coordinates)

     return database


# Read Queries
def readQueries(queries_name):
     queries = []
     with open(queries_name) as file:
          for line in file:
               query = line
               if (query[-1] == '\n'):
                    query = line[:-1]
               query = query.split(' ')
               query = tuple(map(int, query))
               queries.append(query)
     
     return queries