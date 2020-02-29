'''Add Two Numbers'''
class takesum:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sm(self):
        return self.a + self.b

def main():
    
    a = int(input())
    b = int(input())
    obj=takesum(a,b)
    print(obj.sm())

if __name__=='__main__':
    main()
