elif (search_algorithm == 1):
     print("KD Tree Search")

     # Start Stopwatch
     start_time = time.time()

     for i in range(len(queries)):
          query = queries[i]
          tree_query = np.array([[query[0], query[1]], [query[2], query[3]]])
          kd_results.append(list(tree.rangesearch(tree_query)))
     
     # Stop Stopwatch
     end_time = time.time()
     print("Total Duration (s): ", end_time - start_time)

     for j in range(len(kd_results)):
          kd_results[j].sort()