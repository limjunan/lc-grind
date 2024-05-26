class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = {}

        for i in magazine:
            if i in note: note[i] += 1
            else: note[i] = 1
        
        for i in ransomNote:
            if i not in note or not note[i]: return False
            note[i] -= 1

        return True
        