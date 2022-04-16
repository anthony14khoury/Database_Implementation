import numpy as np

def sequential_search(db, queries):

     # Open Sequential Search Output File
     with open('../Output/Sequential_Search_Output.txt', 'w') as file:

          # Initial Array with Proper Output Structure
          results = [(0, 0)]
          for i in range(len(queries)):
               
               # Grab Parameters of the Query
               xmin, xmax, ymin, ymax = queries[i][0], queries[i][1], queries[i][2], queries[i][3]

               # Write the Query to the Output File
               query_output = 'Query: (', xmin, ',', xmax, ',', ymin, ',', ymax, ')'
               file.write(str(query_output))
               
               query_results = [[(0, 0)]]
               for record in db:

                    # Grab a record
                    x, y = record[0], record[1]

                    # Check if the record is in the query
                    if (xmin <= x and x <= xmax and ymin <= y and y <= ymax):
                         
                         query_results.append(record)


               query_results.sort()          # Sort List
               results = results[1:]         # Remove First Index (default structure)
               results.append(query_results) # Add record to results list

               for report_record in query_results:
                    # Write Record to Output File
                    file.write(str(report_record))


          # Remove First Index (default structure)
          # results = results[1:]

     return results