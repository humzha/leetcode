class Solution:
    """Solution for determining if you can complete a circular gas station circuit.

    There are `n` gas stations arranged in a circle. Each station `i` has an
    amount of gas `gas[i]`, and it costs `cost[i]` gas to travel from station
    `i` to station `i + 1` (the last station connects back to the first). Return
    the **starting gas station’s index** if you can travel around the circuit
    once in a clockwise direction; otherwise return `-1`. You may assume
    total gas is at least total cost if a solution exists.
    """

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """Determines if there exists a valid starting station index.

        Args:
            gas (list[int]): Amount of gas available at each station.
            cost (list[int]): Cost of gas to travel from station `i` to `i + 1`.

        Returns:
            int: The starting station index if the circuit can be completed;
                otherwise `-1`.
        """
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0 :
            return  -1
            
        res = curr_balance = 0
        for i in range(len(gas)):
            curr_balance += delta[i]
            if curr_balance < 0:
                res = i + 1
                curr_balance = 0

        return res