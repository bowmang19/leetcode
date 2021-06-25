class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Determine the shortest word in the list
        shortestWord = min(strs, key=len)
        # Iterate over that word because the prefix can't be longer than it
        for i, character in enumerate(shortestWord):
            # Compare each other word to it
            for word in strs:
                # If the current character is not equal between them
                if word[i] != character:
                    # Return the previous characters in the shortest word
                    return shortestWord[:i]
        # Otherwise, return the entire shortest word
        return shortestWord
