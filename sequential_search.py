import numpy as np

def sequential_search(db, queries):

     results = [(0, 0)]
     for i in range(len(queries)):
          xmin, xmax, ymin, ymax = queries[i][0], queries[i][1], queries[i][2], queries[i][3]
          print("Query: (", xmin, ",", xmax, ",", ymin, ",", ymax, ")")

          # print("Records:")
          for record in db:
               x, y = record[0], record[1]

               if (xmin <= x and x <= xmax and ymin <= y and y <= ymax):
                    # print("(", x, ", ", y, ")")
                    results.append(record)

     results = results[1:]
     return results