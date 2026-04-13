class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        return len(pattern) == len(s_list) and len(set(pattern)) == len(set(s_list)) == len(set(zip(pattern, s_list)))