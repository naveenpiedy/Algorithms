import math


class Hash_Simulation:
    def __init__(self):
        self.hashTable = []
        self.size = 1000
        self.hashTable = [None] * 1000

    def intoHash(self, key, value):
        hashing_key = math.floor(key % self.size)
        if self.hashTable[hashing_key] is None:
            self.hashTable[hashing_key] = [[key, value]]
        else:
            self.hashTable[hashing_key].append([key, value])

    def lookUp(self, key):
        hashing_key = math.floor(key % self.size)
        keys = self.hashTable[hashing_key]
        for i in keys:
            if i[0] == key:
                return key
            else:
                return None

# def main():
#     Hash = Hash_Simulation()
#     Hash.intoHash(5,"Five")
#     Hash.intoHash(55, "Die")
#     s = Hash.lookUp(5)
#     print(s)
# if __name__ == '__main__':
#     main()
