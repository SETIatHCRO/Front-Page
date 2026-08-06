import numpy as np

def main():
    args = np.arange(0,32,0.5) # 0 to 31.5 in steps of .5 is permitted input
    d = {}

    for n in args:
        # Input is inverted and reversed 6 bit going into the pam interface. We reverse, ignore first bit, and invert again to 5-bit binary
        # which allows 0-31db attenuation.

        # Ex. 2.5 -> 5 (out of 6 bits) -> 000101 -> 101000 -> 010111 -> 
        d[str(n).removesuffix(".0")] = int(f"{int(2*n):06b}"[::-1][1:].zfill(8),2)

    while True:
        print(d[str(input('Command: '))])


if __name__ == "__main__":
    main()