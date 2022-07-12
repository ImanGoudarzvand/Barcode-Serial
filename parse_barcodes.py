import os
import numpy as np


def give_barcodes(big_file, palet_num, folderName, file_name):

    os.makedirs(folderName, exist_ok=True)
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
        # barcodes = []
        # list.append(file.read(i))
        total_num = 0
        file_num = 0
        flag = True
        delete_last_file = False

        # barcodes = []

        while flag:
            # if total_num % palet_num == 0:
            barcodes = []

            with open(f'{folderName}/{file_name}{file_num}.txt', 'w') as f:

                # if total_num == 0:
                barcodes.append(file.read(i+1))
                if barcodes[-1] == " ":
                    delete_last_file = True
                    break
                total_num += 1
                # else:
                #     total_num -= 1

                while total_num % palet_num != 0:
                    # if total_num == palet_num:
                    #     total_num -= 1

                    barcodes.append(file.read(i+1))
                    if barcodes[-1] == '':
                        flag = False
                        break
                    total_num += 1
                barcodes = [item.replace('\n', '') for item in barcodes]
                # total_num += 1
                # print('barcodes ;', barcodes)
                for item in barcodes:
                    # print('barcodes ;', barcodes)
                    f.write("%s\n" % item)

            file_num += 1
        if delete_last_file:
            os.remove(f'{folderName}/{file_name}{file_num}.txt')
        # barcodes = []
        # print(barcodes)
    # return barcodes
    #     barcodes.append(file.read(i+1))
    # barcodes = [item.replace('\n', '') for item in barcodes]

    # return np.array(barcodes, dtype=object)


if __name__ == '__main__':
    # give_barcode(big_file, 6120000)
    # big_file = 'Pocket_14001114_Letter_3966575_Part1_236Milion.txt'

    big_file = input('big file name: ') + '.txt'
    palet_num = int(input('number of each palet: '))
    folderName = input('Folder Name : ')
    file_name = input('file_name: ')

    give_barcodes(big_file=big_file, palet_num=palet_num,
                  folderName=folderName, file_name=file_name)

    # print(a)
