
def give_last_palet_barcode(big_files_PATH) -> list:
    """This function will read barcodes from the last sub-txt barcode files

    Args:
        big_files_PATH (_type_): the path to last sub-txt barcode files
 
    Returns:
        a list contains last file barcodes
    """
    last_palet_barcodes = []

    with open(big_files_PATH) as f:
        i = 0
        while True:
            data = f.read(1)
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