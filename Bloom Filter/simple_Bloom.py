from bitarray import bitarray

#3rd party
import mmh3


class BloomFilter(set):

        def __init__(self, size, hash_count):
            super(BloomFilter, self).__init__()
            self.bit_array = bitarray(size)
            self.bit_array.setall(0)
            self.size = size
            self.hash_count = hash_count

        def __len__(self):
            return self.size

        def __iter__(self):
            return iter(self.bit_array)

        def add(self, item):
            for ii in range(self.hash_count):
                index = mmh3.hash(item, ii) % self.size
                self.bit_array[index] = 1

            return self

        def __contains__(self, item):
            out = True
            for ii in range(self.hash_count):
                index = mmh3.hash(item, ii) % self.size
                if self.bit_array[index] == 0:
                    out = False

            return out


def main():
        bloom = BloomFilter(100, 10)
        animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
                   'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
                   'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
        # First insertion of animals into the bloom filter
        for animal in animals:
            bloom.add(animal)

        # Membership existence for already inserted animals
        # There should not be any false negatives
        for animal in animals:
            if animal in bloom:
                print('{} is in bloom filter as expected'.format(animal))
            else:
                print('Something is terribly went wrong for {}'.format(animal))
                print('FALSE NEGATIVE!')

        # Membership existence for not inserted animals
        # There could be false positives
        other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                         'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                         'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                         'hawk' ]
        for other_animal in other_animals:
            if other_animal in bloom:
                print('{} is not in the bloom, but a false positive'.format(other_animal))
            else:
                print('{} is not in the bloom filter as expected'.format(other_animal))

if __name__ == '__main__':
    main()