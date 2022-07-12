import os
import numpy as np


def give_last_palet_barcode(big_files_PATH):
    last_palet_barcodes = []

    with open(big_files_PATH) as f:
        i = 0
        # flag = True
        while True:
            data = f.read(1)
            # print(data)
            # print('here', data)
            if data == '\n':
                break
            else:
                i += 1
    with open(big_files_PATH) as f:

        last_palet_barcodes.append(f.read(i+1))
        while last_palet_barcodes[-1] != '':
            last_palet_barcodes.append(f.read(i+1))
    last_palet_barcodes = [item.replace('\n', '')
                           for item in last_palet_barcodes]

    return last_palet_barcodes
