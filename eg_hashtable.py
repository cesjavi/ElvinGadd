import math


class HashTableOA:
    """
    A hash table storing ints.
    Collision resolution through Open Addressing
    No delete() support
    """

    def __init__(self, slots, h=None, probe='linear'):
        """
        :param slots: number of slots in the hash table
        :param h: the hash function, defaults to the multiplication method
        :param probe: type of probing method
        """
        self.table = [None for _ in range(slots)]
        self.slots = slots
        self.elements = 0

        self.h = h or self.hash_mult
        self.probe = self.linear_probe if probe == 'linear' else self.quad_probe


    def insert(self, k: int) -> None:
        # Insert key k into the table
        if self.elements == self.slots:
            raise Exception('Cannot insert into full hash table')

        for i in self.probe(k):
            if self.table[i] is None:
                self.table[i] = k
                self.elements += 1
                break


    def search(self, k: int) -> bool:
        # Return whether key k is in the table
        for i in self.probe(k):
            if self.table[i] == k:
                return True
            elif self.table[i] is None:
                return False
        return False


    def hash_mult(self, k):
        # Hashing using the multiplication method
        return math.floor(self.slots * ((k * 0.618) % 1))


    def linear_probe(self, k: int):
        # Map key k to a slot in table
        for i in range(self.slots):
            yield (self.h(k) + i) % self.slots


    def quad_probe(self, k: int):
        # Map key k to a slot in table
        for i in range(self.slots):
            yield (self.h(k) + i**2) % self.slots



"========= Testing Hash Table ========="

hashtable = HashTableOA(10, lambda x: x % 10, 'linear')

hashtable.insert(46)
hashtable.insert(34)
hashtable.insert(42)
hashtable.insert(23)
hashtable.insert(52)
hashtable.insert(33)

print(hashtable.table)
