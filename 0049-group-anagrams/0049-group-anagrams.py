class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for st in strs:
            charCount = [0] * 26

            for ch in st:
                charCount[ord(ch) - ord("a")] += 1 

            result[tuple(charCount)].append(st)

        return result.values()

