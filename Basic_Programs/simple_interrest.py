class si:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r

    def sii(self):
        return p*t*r//100

if __name__ == '__main__':
    p=int(input())
    t=int(input())
    r=int(input())

    obj_si=si(p,t,r)
    print(obj_si.sii())
    
