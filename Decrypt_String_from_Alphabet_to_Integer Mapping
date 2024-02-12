class Solution:
    def freqAlphabets(self, s: str) -> str:
        characters = []
        i = -1
        answers = []

        while i >= -len(s):
            if s[i] == "#":
                index = i + (-2)
                c = s[index:i]
                characters.append(c)
                i -= 2
            else:
                characters.append(s[i])
            i -= 1

        answers = list(map(int, characters))
        
        s = ""

        for i in range(-1, -len(answers) - 1, -1):
            s += chr(ord('a') + answers[i] - 1)

        return s
