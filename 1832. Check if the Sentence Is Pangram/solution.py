class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        else:
            # The set of characters in the string does not allow repeated characters,
            # so if the length of it is equal to 26, the sentence has every letter
            boolean = len(set(sentence)) == 26
            return boolean
