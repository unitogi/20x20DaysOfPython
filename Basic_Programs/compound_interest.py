'''Compund Interest'''

class ci:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r

    def cii(self):
        return p*((1+r/100)**t)

if __name__ == '__main__':
    p=float(input())
    t=float(input())
    r=float(input())

    obj_ci=ci(p,t,r)
    print(obj_ci.cii())
    
