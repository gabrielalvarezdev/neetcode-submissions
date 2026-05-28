# Not sure. my best guess would be to:
# 1. take each element of the list and sort the chars alphabetically
# 2. compare each of the sorted elements to one another
# 3. append elements to a new list as matches are found or not found


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
            
        