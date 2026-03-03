from collections import Counter
import heapq

class Solution:
    """Solution for scheduling tasks with cooling intervals.

    Given a list of characters `tasks` representing different tasks and a
    non‑negative integer `n` representing the minimum cooling interval between
    two same tasks, return the least number of time units needed to finish all
    tasks. Each time unit, the CPU can either execute a task or be idle.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Calculates the least number of time units to finish all tasks with cooling.

        Args:
            tasks (List[str]): A list of uppercase characters representing tasks.
            n (int): The minimum number of intervals that must pass before the same task can run again.

        Returns:
            int: The minimum time units required to complete all tasks.
        """
        
        # max_heap: freq, task_id
        avail: list[tuple[int, int]] = []
        # min_heap: avail_time, task_id, freq
        cooldown: list[tuple[int, int, int]] = []
        for task_id, freq in Counter(tasks).items():
            heapq.heappush(avail, (-freq, task_id))
            
        time = 0
        while avail or cooldown:
            # Fast-forward time
            if not avail:
                time = max(time, cooldown[0][0])

            # Add now-ready cooldown tasks
            while cooldown and cooldown[0][0] <= time:
                _, task_id, freq = heapq.heappop(cooldown)
                heapq.heappush(avail, (-freq, task_id))
                
            freq, task_id = heapq.heappop(avail)
            freq = abs(freq)
            
            if freq - 1 > 0:
                heapq.heappush(cooldown, (n + 1 + time, task_id, freq - 1))
            time += 1
                
        return time