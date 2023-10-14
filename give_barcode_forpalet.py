import numpy as np

def give_barcode_forpalet(big_file: str, palet_num: int) -> np.ndarray:
    """This function will extract barcodes from a sub-txt barcode file

    Args:
        big_file (str): the sub-txt big file within big folder
        palet_num (int): number of barcodes in each sub-txt file

    Returns:
        a numpy array consists of all barcodes of a sub-txt file
    """


    with open(big_file) as file:

        i = 0
        while True:
            data = file.read(1)
            if data == '\n':
                break
            else:
                i += 1

    with open(big_file) as file:
        barcodes = []
        for _ in range(palet_num):
            barcodes.append(file.read(i+1))
        barcodes = [item.replace('\n', '') for item in barcodes]

    return np.array(barcodes, dtype=object)


if __name__ == '__main__':
    file_name = 'New Text Document.txt'
    file_name2 = 'Pocket_14001114_Letter_3966575_Sample2_236Milion.txt'
    big_file = 'Pocket_14001114_Letter_3966575_Part1_236Milion.txt'
    a = give_barcode_forpalet(big_file, 6120000)
    print(a)
