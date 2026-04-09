class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for val in strs:
            key = "".join(sorted(val))
            if key in d.keys():
                d[key].append(val)
            else:
                d[key] = [val]

        return list(d.values())