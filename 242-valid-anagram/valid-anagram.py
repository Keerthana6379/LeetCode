class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dict={}
        for ch in s:
            dict[ch]=dict.get(ch,0)+1
        for ch in t:
            if ch not in dict or dict[ch]==0:
                return False
            dict[ch]-=1
        return True