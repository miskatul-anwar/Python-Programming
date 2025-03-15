class vector:
    def __init__(self,size:int)->None:
        self.size=size;
        self.list=[]
        for _ in range(self.size):
            self.list.append(0)

    def set_element(self,index:int,element:int)->None:
        self.list[index]=element

    def get_element(self,index:int)->int:
        if self.list[index]!= 0:
            return self.list[index]
        return -1

    def show_all(self)->None:
        for i in range(self.size):
            if self.list[i] != 0:
                print(f"{self.list[i]}",end=" ")
        print()

def main()->None:
    v = vector(10)
    v.set_element(0,3)
    v.set_element(1,4)
    v.show_all()

if __name__=="__main__":
    main()
