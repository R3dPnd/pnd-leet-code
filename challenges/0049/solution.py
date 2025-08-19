class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in anagrams.keys():
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(string)
        
        return list(anagrams.values())
            

