class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        lyst = []
        for i in words:
            morseConv = ''
            for j in i:
                morseConv += morse[ord(j) - 97]
            lyst.append(morseConv)
        return len(set(lyst))
