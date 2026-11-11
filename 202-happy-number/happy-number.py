class Solution(object):
    def isHappy(self, n):
        hs = set()
        while n != 1 and n not in hs:
            hs.add(n)
            s = 0
            while n > 0:
                r = n % 10
                s += r * r
                n //= 10
            n = s
        return n == 1