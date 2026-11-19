class Solution(object):
    def findLongestWord(self, s, dictionary):
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            it = iter(s)
            if all(char in it for char in word):
                return word
        return ""        