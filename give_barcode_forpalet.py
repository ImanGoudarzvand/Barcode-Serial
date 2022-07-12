import os
import numpy as np

file_name = 'New Text Document.txt'
file_name2 = 'Pocket_14001114_Letter_3966575_Sample2_236Milion.txt'
big_file = 'Pocket_14001114_Letter_3966575_Part1_236Milion.txt'


def give_barcode_forpalet(big_file, palet_num):

    with open(big_file) as file:

        i = 0
        # flag = True
        while True:
            data = file.read(1)
            # print(data)
            # print('here', data)
            if data == '\n':
                break
            else:
                i += 1

    # print(i)
    with open(big_file) as file:
        barcodes = []
        # list.append(file.read(i))
        # total_num = 0
        for _ in range(palet_num):

            barcodes.append(file.read(i+1))
        barcodes = [item.replace('\n', '') for item in barcodes]

    return np.array(barcodes, dtype=object)


if __name__ == '__main__':
    a = give_barcode_forpalet(big_file, 6120000)
    print(a)
