class fact:
    def __init__(self,num):
        self.num=num

    def fac(self):
        k=1
        for i in range(1,self.num+1):
            k=k*i
        return k

def main():
    num = int(input())
    objfact = fact(num)
    print(objfact.fac())

if __name__ == '__main__':
    main()
