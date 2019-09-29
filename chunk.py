from bitstring import BitArray, BitStream
from time import localtime, strftime


with open('file.bin', "rb") as file: # open binary file
    chunk = file.read(256) # define number of bytes to read
bin_hex = BitArray(chunk) # bin to hex
bin_ascii = bin_hex.bin #hex to ASCII
num_ones_array = bin_ascii.count('1')


with open('write_file.csv', "a+") as write_file: # open file and append number of ones
    write_file.write('{} {}\n'.format(strftime("%H:%M:%S", localtime()), num_ones_array))
#write_file.close()
