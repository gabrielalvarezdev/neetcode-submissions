
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str in strs:
            word = "".join(sorted(str))
            if word not in seen:
                seen[word] = [str]
            else:
                seen[word].append(str)
        return list(seen.values())
            
        