import numpy as np

def sequential_search(db, queries):

     # Open Sequential Search Output File
     with open('./Output/Sequential_Search_Output.txt', 'w') as file:

          # Initial Array with Proper Output Structure
          dimension = int(len(queries[0]) / 2)

          # Looping through the queries
          for query in queries:   
               query_results = [[tuple([0] * (dimension))]]                 

               # Write the Query to the Output File
               query_output = 'Query: ' + str(tuple(query)) + '\n'
               file.write(query_output)
               
               for record in db:

                    record = list(record)    # Record from DB
                    check = False            # Boolean check if record is in query
                    q = 0                    # Query Index

                    # Looping through the record
                    for i in range(len(record)):
                         q = i * 2 # Update Query Index

                         # Is each dimension of the record in the corresponding dimension of the query?
                         if (query[q] <= record[i] and record[i] <= query[q+1]):
                              check = True
                         else:
                              check = False
                              break
                    
                    # If true, record is in query
                    if (check == True):
                         query_results.append(record)


               query_results = query_results[1:] # Remove First Index (default structure)
               query_results.sort() # Sort List
               
               # Write Record to Output File
               for report_record in query_results:
                    temp_report = '\t' + str(report_record) + '\n'
                    file.write(temp_report)