from misc import digits,xor_all

def self_shrinking_lfsr(tap, fill):
    """
    Each call to this generator clocks the lfsr twice, generating a pair of bits.
    If the first bit generated is 1, the second bit is returned.
    If the first bit generated is 0, the lfsr is clocked again twice for a new pair of bits.
    """
    # get length of lfsr from the supplied tap
    l = digits(tap, 2) - 1
    # don't consider least significant bit of the tap polynomial, it represents the 1
    # at the end of the polynomial and is not an actual tap location
    tap = tap >> 1
    # get the bitmasks to access the highest and second highest bits
    high = 1 << (l-1)
    second = 1 << (l-2)
    # generate the bitmask to truncate lfsr to l bits
    mask = 0
    for i in range(0, l):
        mask = (mask<<1)^1
    
    def clock():
        # clock the lfsr
        return ((fill<<1)&mask) ^ xor_all(tap & fill)
    out = 0
    while(True):
        # if high bit is 0:
        while(not fill&high):
            # clock twice
            fill = clock()
            fill = clock()
        # when high bit becomes 1, return second highest bit
        yield 1 if fill&second else 0
        out += 1
        # clock twice
        fill = clock()
        fill = clock()