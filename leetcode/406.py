class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people_list = []
        for idx, person in enumerate(people):
            people_list.append([person[1], person[0], idx])

        ans = []
        while people_list:
            people_list.sort(reverse=True)
            k, height, idx = people_list.pop()
            ans.append(people[idx])
            for next_person in people_list:
                if next_person[1] <= height:
                    next_person[0] -= 1

        return ans
