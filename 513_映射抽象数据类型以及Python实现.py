# 实现hashtable,指定在key位置存入data


class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size  # hold the key items 
        self.data=[None]*self.size  # hold the data values

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:  # 如果slot内是empty，就存进去
            self.slots[hashvalue]=key
            self.data[hashvalue]=data

        else:  # slot内已有key
            if self.slots[hashvalue]==key: # 如果已有值等于key,更新data
                self.data[hashvalue]=data # replace
            else:  # 如果slot不等于key,找下一个为None的地方
                nextslot=self.rehash(hashvalue,len(self.slots)) 
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,len(self.slots))
                    print('while nextslot:',nextslot)
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    print('slots None')
                else:
                    self.data[nextslot]=data
                    print('slots not None')
            
    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        data=None
        stop=False
        found=False
        position=startslot

        while self.slots[position]!=None and not found and not stop:
            if self.slots[position]==key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position==startslot:
                    stop=True
        return data
    
    def __getitem__(self,key): # 魔法函数
        return self.get(key)
    def __setitem__(self,key,data): # 魔法函数
        print('key:',key)
        print('data:',data)
        self.put(key,data)


H=HashTable()
H[54]='cat'