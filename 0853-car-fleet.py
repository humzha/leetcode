class Solution:
    """Solution for counting car fleets arriving at a target destination.

    Given a target distance, and two arrays position and speed for n cars,
    return the number of car fleets that will arrive at the destination.
    A car fleet is formed when a faster car catches up to a slower one
    and they travel together at the slower speed.
    """

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Your implementation here
        car_pos_speed = [(position[i], speed[i]) for i in range(len(speed))]
        car_pos_speed.sort(key=lambda x: x[0])
        # Want the highest/closest position first, because they will be the heads of the blocking fleets
        car_pos_speed.reverse()
        car_fleets = []
        for pos, speed in car_pos_speed:
            # Assuming not blocked
            time_taken = (target - pos) / speed
            if not car_fleets:
                car_fleets.append(time_taken)
                continue
            # 20h, curr_car = 19h, 21h
            if car_fleets and car_fleets[-1] < time_taken:
                car_fleets.append(time_taken)
        return len(car_fleets)