class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        people = list(range(1, n+1))
        direction = 1
        current_index = 0

        while time > 0:
            current_index = (current_index + direction) % len(people)
            time -= 1

            if time == 0:
                return people[current_index]

            if current_index == 0 or current_index == len(people) - 1:
                direction *= -1
        