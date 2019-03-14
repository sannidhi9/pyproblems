#https://leetcode.com/problems/add-binary/
#visit the above link to view problem description
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        e,c,d,dic=[],0,[],{0:[0,0],1:[1,0],2:[0,1],3:[1,1]}
        x=len(a)-len(b)
        if x>0:
            for j in range(x):
                b="0"+b
        elif x<0:
            for k in range(abs(x)):
                a="0"+a
        for l in range(len(a)):
            d=[0]+d        
        for i in range(len(b)-1,-1,-1):
            e=dic[int(a[i])+int(b[i])+c]
            d[i],c=e[0],e[1]
            if c==1 and i==0:
                d=[1]+d
        res ="".join(map(str, d))         
        return res
