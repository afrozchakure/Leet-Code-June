class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        
        # finding the weighted sum (Cumulative)
        for weights in w:
            prefix_sum += weights
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # Generating a random number
        random_num = self.total_sum * random.random()
        
        # Applying binary search
        low, high = 0, len(self.prefix_sum) - 1
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
