import os


def give_barcodes(big_file: str,
                palet_num: str,
                folderName: str,
                file_name: str) -> None:
    """This function will extract all barcodes from a big txt file and split them into
       smaller txt files which are more handable

    Args:
        big_file: big txt file path
        palet_num: number of barcodes in each sub txt files
        folderName: the name for folder in which sub txt files are
        file_name: the prefix name for each txt file 
    """
    
    os.makedirs(folderName, exist_ok=True)
    with open(big_file) as file:

        # read chars from the first line until reach \n (end of a line)
        i = 0
        while True:
            data = file.read(1)
            if data == '\n':
                break
            else:
                i += 1
    
    # i+1 -> len of each barcode 
    # data -> pointer on last char on first line till reach \n 

    with open(big_file) as file:
        total_num = 0
        file_num = 0
        end_of_file = False        # a flag to determine if we are done writing barcodes with a txt file
        empty_file = False         # a flag to delete a generated file if it is empty
        while not end_of_file:
            barcodes = []

            with open(f'{folderName}/{file_name}{file_num}.txt', 'w') as f:

                # analysing the first line
                barcodes.append(file.read(i+1))
                if barcodes[-1] == "":
                    empty_file = True 
                    break # break if no barcode remains
                total_num += 1

                # real lines until there are palent_num of barcodes within afile
                while total_num % palet_num != 0:
                    barcodes.append(file.read(i+1))
                    if barcodes[-1] == '':
                        end_of_file = True
                        break
                    total_num += 1

                barcodes = [item.replace('\n', '') for item in barcodes] 
                for item in barcodes:
                    f.write(f"{item}\n")

            file_num += 1
        if empty_file:
            os.remove(f'{folderName}/{file_name}{file_num}.txt')

if __name__ == '__main__':
    # big_file = "new_big_file_2_750_000.txt"
    # palet_num = 100_000
    # folderName = "barcodes_folder"
    # file_name = "barcode_file"
    big_file = input("big_file_name: ") 
    if big_file[-3:] != "txt":
         big_file += ".txt"
    assert os.path.exists(big_file), f"{big_file} does Not exists!"
    palet_num = int(input("palet_num: "))
    folderName = input("big files folder name: ")
    file_name = input("A name for each big file: ")

    give_barcodes(big_file=big_file,
                palet_num=palet_num,
                folderName=folderName,
                file_name=file_name)
