class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            pattern = [0] * 26
            for char in string:
                pattern[ord(char) - ord('a')] += 1

            result[tuple(pattern)].append(string)
        return list(result.values())