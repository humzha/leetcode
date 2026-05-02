from collections import defaultdict
import heapq

class Solution:
    """Solution for finding the cheapest flight within at most k stops.

    You are given:
    - n cities labeled 0 to n-1 flights where flights[i] = [from, to, price] src (start), dst (destination), k (max stops) Return the cheapest price from src to dst with at most k stops. If not possible, return -1. """

    def findCheapestPrice(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        """Finds the cheapest price with at most k stops.

        Args:
            n (int): Number of cities.
            flights (list[list[int]]): Directed edges with cost.
            src (int): Source city.
            dst (int): Destination city.
            k (int): Maximum stops allowed.

        Returns:
            int: Cheapest cost or -1.
        """
        adj = defaultdict(list)
        for source, dest, cost in flights:
            adj[source].append((dest, cost))
        
        # stops = 1 -> the string is 3 src -> stop-> dest
        max_path = k + 2
        # path_len
        # (cost, path, city)
        visited = set()
        min_heap = [(0, 1, src)]
        while min_heap:
            cost, path_len, city = heapq.heappop(min_heap)
            if (city, path_len) in visited or path_len > max_path:
                continue
            # cost is the lowest cost we can traverse to city for
            if city == dst:
                return cost
            visited.add((city, path_len))
            for dest, flight_cost in adj[city]:
                heapq.heappush(min_heap, (cost + flight_cost, path_len + 1, dest))
        return -1
            