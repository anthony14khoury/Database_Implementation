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
               query_output = 'Query: (' + str(xmin) + ',' + str(xmax) + ',' + str(ymin) + ',' + str(ymax) + ')' + '\n'
               file.write(query_output)
               
               query_results = [[(0, 0)]]
               for record in db:

                    # Grab a record
                    x, y = record[0], record[1]

                    # Check if the record is in the query
                    if (xmin <= x and x <= xmax and ymin <= y and y <= ymax):
                         
                         query_results.append(record)


               query_results = query_results[1:]         # Remove First Index (default structure)
               query_results.sort() # Sort List

               for report_record in query_results:
                    # Write Record to Output File
                    temp_report = '\t' + str(report_record) + '\n'
                    file.write(temp_report)