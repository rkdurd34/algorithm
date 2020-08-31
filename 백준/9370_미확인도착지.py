import sys
import heapq

final = []
for _ in range(int(sys.stdin.readline())):
    dot_num, line_num, cand = list(map(int, sys.stdin.readline().split()))
    start_node, a, b = list(map(int, sys.stdin.readline().split()))
    all_dict = dict()
    cand_list = list()
    for i in range(dot_num):
        all_dict[i + 1] = dict()
    for _ in range(line_num):
        temp_start, temp_end, temp_weight = list(map(int, sys.stdin.readline().split()))
        if (temp_start == a and temp_end == b) or (temp_end == a and temp_start == b):
            all_dict[temp_start][temp_end] = float(temp_weight)
            all_dict[temp_end][temp_start] = float(temp_weight)
        else:
            all_dict[temp_start][temp_end] = temp_weight
            all_dict[temp_end][temp_start] = temp_weight
    for _ in range(cand):
        cand_list.append(int(sys.stdin.readline()))
    cand_list.sort()


    # print(all_dict,cand_list)
    def dijk(graph, start, a, b, cand_list):
        answer = []
        distances = {dot: float('inf') for dot in graph}
        distances[start] = 0
        queue = []
        heapq.heappush(queue, [distances[start], start])
        # print(graph)
        while queue:
            # print(distances,queue)
            current_distances, current_start = heapq.heappop(queue)
            if (current_distances > distances[current_start]) or (not graph[current_start]):
                continue
            for i in graph[current_start]:
                if distances[i] > distance[current_start] + current_distances:
                    distances[i] = distance[current_start] + current_distances
                    heapq.heappush(queue, [distances[i], i])
                elif distances[i] == distance[current_start] + current_distances:
                    if type(distance[current_start]+current_distances) == float:
                        distances[i] = distance[current_start] + current_distances

        for i in cand_list:
            if type(distances[i]) != int and distances[i] != float('inf'):
                answer.append(i)
        return answer


    final.append(dijk(all_dict, start_node, a, b, cand_list))
for i in final:
    print(*i)
import sys
import heapq
final = []
for _ in range(int(sys.stdin.readline())):
    dot_num, line_num, cand = list(map(int,sys.stdin.readline().split()))
    start_node, a,b = list(map(int,sys.stdin.readline().split()))
    all_dict = dict()
    cand_list = list()
    for i in range(dot_num):
        all_dict[i+1] = dict()
    for _ in range(line_num):
        temp_start,temp_end,temp_weight = list(map(int,sys.stdin.readline().split()))
        if (temp_start == a and temp_end ==  b ) or (temp_end == a and temp_start ==  b):
            all_dict[temp_start][temp_end] =temp_weight-0.001
            all_dict[temp_end][temp_start] = temp_weight-0.001
        else:
            all_dict[temp_start][temp_end] =temp_weight
            all_dict[temp_end][temp_start] = temp_weight
    for _ in range(cand):
        cand_list.append(int(sys.stdin.readline()))    
    cand_list.sort() 
    
    # print(all_dict,cand_list)
    def dijk(graph,start,a,b,cand_list):
        answer = []
        distances = {dot:float('inf') for dot in graph}
        distances[start] = 0
        queue = []
        heapq.heappush(queue,[distances[start],start])
        # print(graph)    
        while queue:
            # print(distances,queue)
            current_distances,current_start =  heapq.heappop(queue)
            for i in graph[current_start]:
                if distances[i] < graph[current_start][i]+current_distances:
                    continue
                if distances[i] >= graph[current_start][i]+current_distances:
                    distances[i] = graph[current_start][i]+current_distances
                    heapq.heappush(queue, [distances[i],i])
        for i in cand_list:
            if type(distances[i]) !=int and distances[i] != float('inf'):
                answer.append(i)
        return answer
    final.append( dijk(all_dict, start_node,a,b,cand_list))
for i in final:
    print(*i)








# import sys
# import heapq
# final = []
# for _ in range(int(sys.stdin.readline())):
#     dot_num, line_num, cand = list(map(int,sys.stdin.readline().split()))
#     start_node, a,b = list(map(int,sys.stdin.readline().split()))
#     all_dict = dict()
#     cand_list = list()
#     for i in range(dot_num):
#         all_dict[i+1] = dict()
#     for _ in range(line_num):
#         temp_start,temp_end,temp_weight = list(map(int,sys.stdin.readline().split()))
#         all_dict[temp_start][temp_end] =temp_weight
#         all_dict[temp_end][temp_start] = temp_weight
#     for _ in range(cand):
#         cand_list.append(int(sys.stdin.readline()))    
#     cand_list.sort() 
    
#     # print(all_dict,cand_list)
#     def dijk(graph,start,a,b,cand_list):
#         answer = []
#         distances = {dot:[9999999,0] for dot in graph}
#         distances[start][0] = 0
#         distances[start][1] = start
        
#         queue = []
#         heapq.heappush(queue,distances[start])
#         # print(graph)
        
#         while queue:
#             # print(distances,queue)
#             current_distances,current_start =  heapq.heappop(queue)
            
#             for i in graph[current_start]:
#                 if distances[i][0] < graph[current_start][i]+current_distances:
#                     continue
#                 if distances[i][0] >= graph[current_start][i]+current_distances:
#                     if i == a and current_start ==  b :
#                         distances[i][0] = graph[current_start][i]+current_distances-0.0001
#                         distances[i][1] = current_start
#                         heapq.heappush(queue, [distances[i][0],i])
#                     if i == b and current_start ==  a:
#                         distances[i][0] = graph[current_start][i]+current_distances-0.0001
#                         distances[i][1] = current_start
#                         heapq.heappush(queue, [distances[i][0],i])
#                     else:
#                         distances[i][0] = graph[current_start][i]+current_distances
#                         distances[i][1] = current_start
#                         heapq.heappush(queue, [distances[i][0],i])
#         for i in cand_list:
#             if type(distances[i][0]) !=int:
#                 answer.append(i)
#         return answer

        
#     result = dijk(all_dict, start_node,a,b,cand_list)
    
#     print(*result)



# for i in final:
#     print(*i)

    # result_list = []
    # # for i in cand_list:
    # #     if distances[i]
    
    # for i in range(len(cand_list)):
    #     if need_node_start  in result[cand_list[i]][2:] and need_node_end in result[cand_list[i]][2:]:
    #         check_list[i] = True
    #         result_list.append(cand_list[i])
        
    # final.append(result_list)
    







# import sys
# import heapq
# final = []
# for _ in range(int(sys.stdin.readline())):
#     dot_num, line_num, cand = list(map(int,sys.stdin.readline().split()))
#     start_node, need_node_start, need_node_end = list(map(int,sys.stdin.readline().split()))
#     all_dict = dict()
#     cand_list = list()
#     for i in range(dot_num):
#         all_dict[i+1] = dict()
#     for _ in range(line_num):
#         temp_start,temp_end,temp_weight = list(map(int,sys.stdin.readline().split()))
#         all_dict[temp_start][temp_end] =temp_weight
#         all_dict[temp_end][temp_start] = temp_weight
#     for _ in range(cand):
#         cand_list.append(int(sys.stdin.readline()))    
#     cand_list.sort() 
#     # print(all_dict,cand_list)
#     def dijk(graph,start,cand_list):
#         distances = {dot:[float('inf')] for dot in graph}
#         distances[start][0] = 0
#         distances[start].append(start)
#         queue = []
#         heapq.heappush(queue,[distances[start][0],start])
#         print(graph)
#         print(distances)
#         while queue:
#             current_distances,current_start =  heapq.heappop(queue)
#             distances[current_start].append(current_start)
#             for i in graph[current_start]:
#                 if distances[i][0] < graph[current_start][i]+current_distances:
#                     continue
#                 if distances[i][0] > graph[current_start][i]+current_distances:
#                     distances[i][0] = graph[current_start][i]+current_distances
#                     # distances[i].append(current_start)
#                     distances[i].extend(distances[current_start][1:]+[current_start])
#                     heapq.heappush(queue, [distances[i][0],i])
#             print(distances,queue)
#         return distances
                    

#     result = dijk(all_dict, start_node, cand_list)
#     result_list = []
#     # for i in cand_list:
#     #     if distances[i]
#     check_list= [False]*len(cand_list)
#     for i in range(len(cand_list)):
#         if need_node_start  in result[cand_list[i]][2:] and need_node_end in result[cand_list[i]][2:]:
#             check_list[i] = True
#             result_list.append(cand_list[i])
#         # if need_node_end in result[cand_list[i]][2:] :
#         #     check_list[i] = True
#     # for i in range(len(check_list)):
#     #     if check_list[i]==True:
#     #         result_list.append(cand_list[i])
#     final.append(result_list)
    


# for i in final:
#     print(*i)


# import sys
# import heapq
# sys.setrecursionlimit(100000000)
# test_case = int(sys.stdin.readline())
# final_list = []
# for _ in range(test_case):
#     dot_num, line_num, cand = list(map(int,sys.stdin.readline().split()))
#     start_node, need_node_start, need_node_end = list(map(int,sys.stdin.readline().split()))
#     all_dict = dict()
#     cand_list = list()
#     for i in range(dot_num):
#         all_dict[i+1] = dict()
#     for _ in range(line_num):
#         temp_start,temp_end,temp_weight = list(map(int,sys.stdin.readline().split()))
#         all_dict[temp_start][temp_end] =temp_weight
#         all_dict[temp_end][temp_start] = temp_weight
#     for _ in range(cand):
#         cand_list.append(int(sys.stdin.readline()))
    
#     def dijk(graph,start,cand_list):
#         distances = {dot:[float('inf'),0] for dot in graph}
#         distances[start][0],distances[start][1] = 0, start
#         queue = []
#         heapq.heappush(queue,[distances[start][0],start])
#         while queue:
#             current_distance, current_node = heapq.heappop(queue)
#             if distances[current_node][0] < current_distance:
#                 continue
#             for adjacent, weight in graph[current_node].items():
#                 temp_distance = current_distance + weight
#                 if temp_distance < distances[adjacent][0]:
#                     distances[adjacent][0] = temp_distance
#                     distances[adjacent][1] =current_node
#                     heapq.heappush(queue, [temp_distance, adjacent])
#         result_list = []
#         for i in cand_list:
#             check_list = [i]
#             check_start = start
#             check_end = i 
#             while check_end != check_start:
#                 check_end = distances[check_end][1]
#                 check_list.append(check_end)
#             if need_node_start in check_list and need_node_end in check_list:
#                 result_list.append(str(i))
#         final_list.append(result_list)
#     dijk(all_dict,start_node,cand_list)
# for nom in final_list:
#     print(" ".join(sorted(nom)))
    

    
    



    

