from bitstring import BitArray, BitStream
from textwrap import wrap
#import timeit
import pandas as pd


global num_ones_array


inputFile = input("Name of the file: ")


def fileBinToAscii():
    global inputFile
    global num_ones_array
    num_ones_array = []
    with open(inputFile, "rb") as file: # open binary file
        bin_hex = BitArray(file) # bin to hex
    bin_ascii = bin_hex.bin
    #print("Here are the bits: " + str(bin_ascii))
    total_bits = len(bin_ascii)
    #print("Total number of bits is: " + str(total_bits)) 
    split_bin_ascii = wrap(bin_ascii, 2048) # split in 2048 bits per line - 1 second
    for i in split_bin_ascii: # calculate number of 'ones' in each of the 2048 bits lines
        num_ones_array.append(i.count('1'))
    #print("Here are the bits splites: " + str(split_bin_ascii))
    #print("Number of ones in each line: " + str(num_ones_array))


fileBinToAscii()

binSheet = pd.DataFrame()                       # Array to Pandas Column
binSheet['Ones'] = num_ones_array
binSheet.dropna(inplace = True)
binSheet = binSheet.reset_index()
binSheet['index'] = binSheet['index'] + 1
binSheet = binSheet.rename(columns = {'index': 'Time'})
binSheet['Sum'] = binSheet['Ones'].cumsum()
binSheet['Average'] = binSheet['Sum']/(binSheet['Time'])
binSheet['Zscore'] = (binSheet['Average']-1024)/(22.62741699796/(binSheet['Time']**0.5))

file_to_save = inputFile.replace(".bin", ".xlsx")
#data_file2 = os.path.basename(data_file)
#data_file2 = data_file2.replace(".csv", "")
number_rows = len(binSheet.Time)
writer = pd.ExcelWriter(file_to_save, engine='xlsxwriter')
binSheet.to_excel(writer,sheet_name='Z-Test',index=False)
workbook = writer.book
worksheet = writer.sheets['Z-Test']
chart = workbook.add_chart({'type': 'line'})
chart.set_title({
'name': 'Z-Score: ',
'name_font': {
    'name': 'Calibri',
    'color': 'black',
    },
})

chart.set_x_axis({
'name': 'Time',
'name_font': {
    'name': 'Calibri',
    'color': 'black'
    },
'num_font': {
    'name': 'Calibri',
    'color': 'black',
    },
})

chart.set_y_axis({
'name': 'Z-Score',
'name_font': {
    'name': 'Calibri',
    'color': 'black'
    },
'num_font': {
    'color': 'black',
    },
})

chart.set_legend({'position': 'none'})
chart.add_series({'values': ['Z-Test', 1, 4, number_rows, 4],
                  'categories': ['Z-Test', 1, 0, number_rows, 0]})
worksheet.insert_chart('G2', chart)
writer.save()
print(binSheet)






#elapsed_time = timeit.timeit(fileBinToAscii, number=1)/1 # time function 100 times
#print(elapsed_time)
