class LFSR:
    # constructor
    def __init__(self, seed: str, tap):
        self.seed = seed
        self.tap = tap

    # return the number of bits in the LFSR
    def length(self):
        return len(self.seed)

    # return the bit at index ‘i’
    def bit(self, i: int):
        return self.seed[i]

    # execute one LFSR iteration and return new (rightmost) bit as an int
    def step(self):
        # save the calculated bit before shift -- bit[0] XOR with bit[tap]
        xor_bit = int(self.bit(0)) ^ int(self.bit(-self.tap))
        # shift the binary value by one by removing the first character of the string: self.seed
        # and concatenating the calculated rightmost bit to the end of self.seed
        self.seed = self.seed[1:] + str(xor_bit)

        # The assignment says to return rightmost bit
        # return int(rightmost_bit)

        # I am going to return the new seed value as an integer
        return int(self.seed, 2)

    # return string representation of the LFSR separated by |’s and spaces
    # ex: 01001010
    def __str__(self):
        return self.seed


if __name__ == "__main__":
    # create an instance of LFSR called seed_1
    seed_1 = LFSR('10011010', 5)
    # print the values for assignment submission
    print(f'initial seed value in binary: {seed_1}')
    print(f'seed value 1 in binary: {seed_1.step()}')
    print(f'seed value 1 as integer {seed_1}')
    print(f'seed value 2 in binary: {seed_1.step()}')
    print(f'seed value 2 as integer {seed_1}')
    print(f'seed value 3 in binary: {seed_1.step()}')
    print(f'seed value 3 as integer {seed_1}')
    print(f'seed value 4 in binary: {seed_1.step()}')
    print(f'seed value 4 as integer {seed_1}')
    print(f'seed value 5 in binary: {seed_1.step()}')
    print(f'seed value 5 as integer {seed_1}')

