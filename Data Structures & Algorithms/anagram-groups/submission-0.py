class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for s in strs:
            order="".join(sorted(s))
            
            if order not in groups:
                groups[order] = []
            
            groups[order].append(s)

        return list(groups.values())