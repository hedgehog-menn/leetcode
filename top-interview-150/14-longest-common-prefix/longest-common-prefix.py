class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        i = 1
        
        while i < len(strs) and len(common_prefix) > 0:
            while not strs[i - 1].startswith(common_prefix) or not strs[i].startswith(common_prefix):
                common_prefix = common_prefix[:-1]
            i += 1

        return common_prefix