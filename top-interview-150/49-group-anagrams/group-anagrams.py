class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for val in strs:
            key = "".join(sorted(val))
            if key in d:
                d[key].append(val)
            else:
                d[key] = [val]

        return list(d.values())