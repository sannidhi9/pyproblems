#https://leetcode.com/problems/add-binary/
#visit the above link to view problem description
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        e,c,d=[],0,[]
        d=[0]*max(len(a),len(b))+d
        for i in range(max(len(a),len(b))-1,-1,-1):
            while(len(a)!=len(b)):
                if len(a)-len(b)>0:
                    b=(len(a)-len(b))*'0'+b
                elif len(a)-len(b)<0:
                    a=abs(len(a)-len(b))*'0'+a
            e=[(int(a[i])+int(b[i])+c)%2,(int(a[i])+int(b[i])+c)//2]
            d[i],c=e[0],e[1]
            if c==1 and i==0:
                d=[1]+d
        return "".join(map(str, d))
