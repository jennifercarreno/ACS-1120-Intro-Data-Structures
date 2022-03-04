#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket

        # makes empty list for keys
        all_keys = []

        # loops through buckets
        for bucket in self.buckets:
            # add key to list
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # empty values list
        values = []
        # loops through buckets
        for bucket in self.buckets:
            # ads value to list
            for key, value in bucket.items():
                values.append(value)
        return values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            # loops through buckets and adds key-values to a list
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        length = 0
        # counts number of key-values
        for bucket in self.buckets:
            for key, value in bucket.items():
                length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs

        # calculates bucket index
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # looks for the key 
        for k,value in bucket.items():
            if k is key:
                # checks if empty
                if k is not None:
                    return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs

        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # looks for key
        for k,value in bucket.items():
            if k == key:
                if k is not None:
                    # returns value of key
                    return k.value
            else:
                raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""

        # calculates bucket index
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # findes key value
        for k,v in bucket.items():
            if k is key:
                # deletes key value
                bucket.delete((k, v))
        
        # creates new key value
        bucket.append((key, value))
      

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for k,v in bucket.items():
            if k == key:
                k.delete()
            else:
                raise KeyError('Key not found: {}'.format(key))

if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))
