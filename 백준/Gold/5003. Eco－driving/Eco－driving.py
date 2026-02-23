import sys
import math
import heapq

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Parse N (vertices/junctions), M (edges/roads), C (max distance limit)
    N = int(input_data[0])
    M = int(input_data[1])
    C = float(input_data[2])
    
    # Parse vertex coordinates
    coords = []
    idx = 3
    for _ in range(N):
        coords.append((float(input_data[idx]), float(input_data[idx+1])))
        idx += 2
        
    # Build the adjacency list for the DIRECTED graph (One-way roads)
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)  # Only u -> v
        
    # Helper function: Calculate Euclidean distance
    def get_dist(u, v):
        x1, y1 = coords[u-1]
        x2, y2 = coords[v-1]
        return math.hypot(x2 - x1, y2 - y1)
        
    # Helper function: Calculate turning angle in degrees
    def get_angle(u, v, w):
        x1, y1 = coords[u-1]
        x2, y2 = coords[v-1]
        x3, y3 = coords[w-1]
        
        # Vectors v1 (u -> v) and v2 (v -> w)
        v1x, v1y = x2 - x1, y2 - y1
        v2x, v2y = x3 - x2, y3 - y2
        
        # Dot product and magnitudes
        dot = v1x * v2x + v1y * v2y
        mag1 = math.hypot(v1x, v1y)
        mag2 = math.hypot(v2x, v2y)
        
        if mag1 == 0 or mag2 == 0:
            return 0.0
            
        cos_theta = dot / (mag1 * mag2)
        
        # Clip cos_theta to [-1.0, 1.0] to prevent math domain errors
        if cos_theta >= 1.0: return 0.0
        if cos_theta <= -1.0: return 180.0
        
        return math.degrees(math.acos(cos_theta))

    # Priority queue stores: (max_angle_so_far, total_distance, current_node, previous_node)
    pq = []
    
    # Initialize the queue. Adding 1e-7 to C handles minor floating-point inaccuracies
    for nxt in adj[1]:
        d = get_dist(1, nxt)
        if d <= C + 1e-7:
            heapq.heappush(pq, (0.0, d, nxt, 1))
            
    # Dictionary to maintain the Pareto frontier for state pruning
    min_dist = {}
    ans = None
    
    while pq:
        max_ang, dist, curr, prev = heapq.heappop(pq)
        
        # State pruning: if we've been here before with a shorter or equal distance, skip it.
        # (Because we pop from the heap by angle, any revisited state inherently has a >= angle).
        state = (curr, prev)
        if state in min_dist and dist >= min_dist[state]:
            continue
        min_dist[state] = dist
        
        # If we reached the destination
        if curr == N:
            ans = max_ang
            break
            
        # Explore neighbors
        for nxt in adj[curr]:
            turn_ang = get_angle(prev, curr, nxt)
            
            # Key Fix: We minimize the MAXIMUM angle encountered on the route
            new_max_ang = max(max_ang, turn_ang) 
            new_dist = dist + get_dist(curr, nxt)
            
            if new_dist <= C + 1e-7:
                heapq.heappush(pq, (new_max_ang, new_dist, nxt, curr))
                
    if ans is not None:
        print(f"{ans:.8f}")
    else:
        # Key Fix: Correct failure string expected by the judge
        print("Impossible")

if __name__ == '__main__':
    solve()