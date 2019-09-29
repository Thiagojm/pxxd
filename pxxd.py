from bitstring import BitArray, BitStream
from textwrap import wrap
import timeit

def code():
    with open('teste.bin', "rb") as file: # open binary file
        bin_hex = BitArray(file) # bin to hex
    bin_ascii = bin_hex.bin
    print("Here are the bits: " + str(bin_ascii))
    total_bits = len(bin_ascii)
    print("Total number of bits is: " + str(total_bits))
    num_ones_array = [] 
    split_bin_ascii = wrap(bin_ascii, 256) # split in 256 bits per line
    for i in split_bin_ascii: # calculate number of 'ones' in each of the 256bits lines
        num_ones_array.append(i.count('1'))

    print("Here are the bits splites: " + str(split_bin_ascii))
    print("Number of ones in each line: " + str(num_ones_array))

# elapsed_time = timeit.timeit(code, number=100)/100 # time function 100 times
# print(elapsed_time)
