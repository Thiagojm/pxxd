from bitstring import BitArray, BitStream
import time
from time import localtime, strftime


is_true = 0
while is_true != 10:
    is_true += 1
    with open('/dev/random', "rb") as file: # open binary file
        chunk = file.read(256) # define number of bytes to read
    bin_hex = BitArray(chunk) # bin to hex
    bin_ascii = bin_hex.bin #hex to ASCII
    num_ones_array = bin_ascii.count('1')
    with open('write_file.csv', "a+") as write_file: # open file and append time and number of ones
        write_file.write('{} {}\n'.format(strftime("%H:%M:%S", localtime()), num_ones_array))
    time.sleep(1)
    print(is_true)



print("Finished")

