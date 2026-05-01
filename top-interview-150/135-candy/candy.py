class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_list = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_list[i] = max(candy_list[i], candy_list[i + 1] + 1)

        return sum(candy_list)