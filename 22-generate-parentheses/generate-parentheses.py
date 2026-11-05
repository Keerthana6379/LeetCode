class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def par(op,cl,str):
            if len(str)==n*2:
                res.append(str)
                return
            if op<n:
                par(op+1,cl,str+"(")
            if cl<op:
                par(op,cl+1,str+")")
        par(0,0,"")
        return res
        