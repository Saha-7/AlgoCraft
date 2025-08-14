class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stak=[]
        for char in tokens:
            if char=="+":
                b=stak.pop()
                a=stak.pop()

                stak.append(a+b)
            elif char=="-":
                b=stak.pop()
                a=stak.pop()

                stak.append(a-b)
            elif char=="*":
                b=stak.pop()
                a=stak.pop()

                stak.append(a*b)
                
            elif char=="/":
                b=stak.pop()
                a=stak.pop()
                
                stak.append(int(float(a)/float(b)))
            else:
                stak.append(int(char))
        return stak[0]
               

