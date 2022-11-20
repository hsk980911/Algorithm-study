'''
bridge_length가 다리를 건너는데 걸리는 시간이므로 bridge_length를 중점으로 생각해야 한다.

다리를 건너는 트럭의 합이 weight가 넘어가지 않을때 대기트럭에서 pop를 이용해 다리를 건너는 트럭으로 이동시킨다. 

여기서 그냥 sum(being_truck)해줄수 있는데 그러면 걸리는 시간이 확 늘어난다. 

아마 sum()이 O(n)이라 시간을 많이 잡아먹어서 그런거 같다. 

그래서 그냥 뺄때 빼주고 더해줄때 더해주는 형식으로 시간을 줄였다.
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    being_truck = [0]*bridge_length
    sum_being=0
    while being_truck:
        answer+=1
        c=being_truck.pop(0)
        sum_being-=c
        if truck_weights:
            if sum_being+truck_weights[0]<=weight:
                a=truck_weights.pop(0)
                being_truck.append(a)
                sum_being+=a
            else:
                being_truck.append(0)
    
    return answer