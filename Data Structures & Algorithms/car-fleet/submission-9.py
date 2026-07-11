class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        for pos, spd in pair:
            time = (target-pos)/spd
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
    