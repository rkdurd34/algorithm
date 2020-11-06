
def solution(bridge_length, weight, truck_weights):
    
    truck_index = 0
    on_bridge = [truck_weights[truck_index] ]
    truck_index+=1
    time = 1
    while truck_index < len(truck_weights):
        print(on_bridge, time)
        if sum(on_bridge) + truck_weights[truck_index] <= weight:
            time += 1
            on_bridge.append(truck_weights[truck_index])
            truck_index+=1
            print(f'time {time} on_brdige{on_bridge}, 위에꺼 ')
            pass
        else:
        # if sum(on_bridge) + truck_weights[truck_index] > weight:
            # print(f'time {time} on_brdige{on_bridge}, ')
            time+= bridge_length - len(on_bridge)
            on_bridge.pop(0)
            while sum(on_bridge) + truck_weights[truck_index] > weight:
                on_bridge.pop(0)
                time+=1111
            print(f'time {time} on_brdige{on_bridge},아래꺼 ')
                
            
    time += bridge_length 
    # print(time, on_bridge,truck_index, len(truck_weights))
        
    
    return time 