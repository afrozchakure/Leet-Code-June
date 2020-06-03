class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mid = int(len(costs)/2)
        sum_a = 0
        diff_list = []
        for i in range(len(costs)):
            diff = costs[i][0] - costs[i][1]
            diff_list.append([diff, i])
        diff_list.sort()  # diff_list contains the indexes of the list
        for i in range(len(diff_list)):
            if i < mid:
                sum_a += costs[diff_list[i][1]][0]
            else:
                sum_a += costs[diff_list[i][1]][1]
        return sum_a
