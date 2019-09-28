from bitstring import BitArray, BitStream


with open('teste.bin', "rb") as file:
    a2 = BitArray(file)
    print(a2.bin)










#my_str = '00100111'
#binary_file = open('file.bin', 'wb')
#b = BitArray(bin=my_str)
#b.tofile(binary_file)
#binary_file.close()










#print(hex(int("100101011", 2)))
