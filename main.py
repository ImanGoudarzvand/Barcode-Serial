from last_palet_barcode import give_last_palet_barcode
from give_serial_for_palets import give_Serials_for_palet
import pandas as pd
from give_barcode_forpalet import give_barcode_forpalet
import sys
import os
import numpy as np
import re
# big_file = 'Pocket_14001114_Letter_3966575_Part1_236Milion.txt'


def main(big_file_folder, output_folder_name, output_file_name, packing_list_file_name, packing_list_folder_name, tarh, num_in_palet):

    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):

        return [atoi(c) for c in re.split(r'(\d+)', text)]

    big_file_names = os.listdir(big_file_folder)
    big_file_names.sort(key=natural_keys)

    
    ### For barcodes:
    ### Last pallet has 2 extra \n
    ### Others barcodes file have 1 extra \n
    if len(big_file_names) != 1:
        path = os.path.join(big_file_folder, big_file_names[-1])
        last_palet_barcodes = give_last_palet_barcode(path)
        # print(len(last_palet_barcodes))
        num_last_palet = len(last_palet_barcodes)-2
        # print(num_last_palet)
        total_barcodes = ((len(big_file_names)-1)*num_in_palet) + num_last_palet
        # print(total_barcodes)
        STARTERS = np.arange(1, total_barcodes, num_in_palet)
        # print(STARTERS)
        os.makedirs(output_folder_name, exist_ok=True)
        os.makedirs(packing_list_folder_name, exist_ok=True)
    else:
        path = os.path.join(big_file_folder, big_file_names[0]) # only one file exist
        last_palet_barcodes = give_last_palet_barcode(path)
        num_last_palet = len(last_palet_barcodes)-1
        # print(num_last_palet)
        # print(last_palet_barcodes[-2])
        last_palet_barcodes = last_palet_barcodes[:-1]
        # print(last_palet_barcodes[-1])
        total_barcodes = num_last_palet
        STARTERS = np.arange(1, total_barcodes, num_in_palet)
        os.makedirs(output_folder_name, exist_ok=True)
        os.makedirs(packing_list_folder_name, exist_ok=True)

    for fileNumber, Starter in enumerate(STARTERS):
        if fileNumber == 0 and len(big_file_names) != 1 :

            # produce serial
            serial_for1palet = give_Serials_for_palet(num_in_palet=num_in_palet, total_barcodes=total_barcodes, tarh=tarh, starter=Starter,
                                                      fileNumber=fileNumber+1, add_zeros=True)
            print(serial_for1palet)
            serial_for1palet = np.array(serial_for1palet).reshape(-1, tarh)

            # get the barcodes
            path = os.path.join(big_file_folder, big_file_names[fileNumber])
            barcodes_for1palet = give_barcode_forpalet(path, num_in_palet)
            barcodes_for1palet = barcodes_for1palet.reshape(-1, tarh)

            # combine barcodes and serials

            output = np.dstack(
                (barcodes_for1palet, serial_for1palet)).flatten()
            output = output.reshape(-1, tarh*2)
            df = pd.DataFrame(output)

            np.savetxt(
                f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', df, delimiter=',', fmt='%s')

            packing_list_output = output.reshape(num_in_palet, 2)
            packing_list_df = pd.DataFrame(
                packing_list_output, columns=['barcode', 'serial'])
            packing_list_palet = packing_list_df.sort_values(by=['serial'])
            np.savetxt(f'{packing_list_folder_name}/{packing_list_file_name}_{fileNumber+1}.txt',
                       packing_list_palet, delimiter=',', fmt='%s')

        if (fileNumber != STARTERS.shape[0]-1) & (fileNumber != 0):
            serial_for1palet = give_Serials_for_palet(num_in_palet=num_in_palet, total_barcodes=total_barcodes, tarh=tarh, starter=Starter,
                                                      fileNumber=fileNumber+1)
            serial_for1palet = np.array(serial_for1palet).reshape(-1, tarh)

            # get the barcodes
            path = os.path.join(big_file_folder, big_file_names[fileNumber])
            barcodes_for1palet = give_barcode_forpalet(path, num_in_palet)
            barcodes_for1palet = barcodes_for1palet.reshape(-1, tarh)

            # combine barcodes and serials

            output = np.dstack(
                (barcodes_for1palet, serial_for1palet)).flatten()
            output = output.reshape(-1, tarh*2)
            df = pd.DataFrame(output)

            np.savetxt(
                f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', df, delimiter=',', fmt='%s')

            packing_list_output = output.reshape(num_in_palet, 2)
            packing_list_df = pd.DataFrame(
                packing_list_output, columns=['barcode', 'serial'])
            packing_list_palet = packing_list_df.sort_values(by=['serial'])
            np.savetxt(f'{packing_list_folder_name}/{packing_list_file_name}_{fileNumber+1}.txt',
                       packing_list_palet, delimiter=',', fmt='%s')

        if fileNumber == STARTERS.shape[0]-1 or len(big_file_names) == 1:

            serial_for1palet = give_Serials_for_palet(num_in_palet=num_last_palet, total_barcodes=total_barcodes, tarh=tarh,
                                                      starter=Starter, fileNumber=fileNumber, last_file=True, add_zeros=True)
            
            # np.savetxt(
                    # f'serials.csv', serial_for1palet, fmt='%s')

            # print(serial_for1palet[-100:])
            # print(serial_for1palet.shape)
            
            # get the barcodes
            if len(big_file_names) != 1:
                path = os.path.join(big_file_folder, big_file_names[fileNumber])
                barcodes_for1palet = give_last_palet_barcode(path)
                barcodes_for1palet = barcodes_for1palet[:-2]
#             barcodes_for1palet = barcodes_for1palet.reshape(-1,tarh)
            else:
                barcodes_for1palet = last_palet_barcodes
                # print(len(barcodes_for1palet))
            # combine barcodes and serials

            # * 2  for barcode + serial
            o = num_last_palet * 2
            print(o)
            n_rows_last_file = o //  (tarh * 2)
            print(n_rows_last_file)
            n_last_row_last_file = o - (n_rows_last_file * tarh * 2)
            print(n_last_row_last_file)



            p = num_last_palet // tarh  # Calculate if all num_last_palet fits in tarh or not
            j = num_last_palet - p * tarh
            output = np.dstack(
                (barcodes_for1palet, serial_for1palet)).flatten()
            # np.savetxt("foo.csv", output, delimiter=",",fmt='%s')
            # print(j)
            print(output.shape)


            if j != 0:

                t = output[:-n_last_row_last_file].reshape(-1, tarh*2)
                t2 = output[-n_last_row_last_file:]
                t2 = t2.tolist()

                # np.savetxt(
                #     f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', t, delimiter=',', fmt='%s')
                
                np.savetxt(
                    f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', t, delimiter=',', fmt='%s')

                # with open(f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', 'a') as f:
                #     for item in t2:
                #         f.write('%s,' % item)
                
                with open(f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', 'a') as f:
                    for item in t2:
                        f.write('%s,' % item)

            else:
                np.savetxt(
                    f'{output_folder_name}/{output_file_name}_{fileNumber+1}.txt', output.reshape(-1, tarh*2), delimiter=',', fmt='%s')

            packing_list_output = output.reshape(-1, 2)
            packing_list_df = pd.DataFrame(
                packing_list_output, columns=['barcode', 'serial'])
            
            packing_list_palet = packing_list_df.sort_values(by=['serial'])
            np.savetxt(f'{packing_list_folder_name}/{packing_list_file_name}_{fileNumber+1}.txt',
                       packing_list_palet, delimiter=',', fmt='%s')


if __name__ == '__main__':
    # give_barcode(big_file, 6120000)
    big_file = 'Pocket_14001114_Letter_3966575_Part1_236Milion.txt'

    big_file_folder = input('big_file_folder: ')
    num_in_palet = int(input('num_in_palet: '))
    tarh = int(input('tarh: '))
    output_folder_name = input('output_folder_name: ')
    output_file_name = input('output_file_name: ')
    packing_list_folder_name = input('packing_list_folder_name: ')
    packing_list_file_name = input('packing_list_file_name: ')

#     big_file_folder = "big_folder"
#     num_in_palet = 2750000
#     tarh = 32
#     output_folder_name = "o"
#     output_file_name = "oo"
#     packing_list_folder_name = "p"
#     packing_list_file_name = "pp"

    main(big_file_folder=big_file_folder, output_folder_name=output_folder_name, output_file_name=output_file_name,
         packing_list_file_name=packing_list_file_name, packing_list_folder_name=packing_list_folder_name, tarh=tarh, num_in_palet=num_in_palet)
