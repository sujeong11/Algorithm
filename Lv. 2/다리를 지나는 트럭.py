from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    trunk_weights = deque(truck_weights)
    cur_weight = 0

    while trunk_weights:
        cur_weight -= bridge.popleft()
        time += 1

        if cur_weight + trunk_weights[0] <= weight:
            new_trunk = trunk_weights.popleft()
            cur_weight += new_trunk
            bridge.append(new_trunk)
        else:
            bridge.append(0)

    return time + bridge_length
