import numpy as np


def give_Serials_for_palet(num_in_palet,
                        total_barcodes,
                        tarh,
                        accumulator,
                        starter=1,
                        fileNumber=1,
                        last_file=False,
                        add_zeros=False,
                        start_index= 1):

    num_boxes = num_in_palet // (tarh*accumulator)

    if last_file:
        ch_ind = np.arange(starter, total_barcodes+ start_index, tarh*accumulator)

    else:
        # 2 added for adade mazrabe 32 or 34 to work ????????
        ch_ind = np.arange(
            starter, (num_in_palet * fileNumber) + start_index, tarh*accumulator)
    total = []
    num_left = num_in_palet - num_boxes * (tarh*accumulator)
    if num_left:
        for num in ch_ind[:-1]:
            a = []
            for i in np.arange(num, num+accumulator, 1):
                row = np.arange(i, accumulator*tarh+num, accumulator)

                for x in row:
                    a.append(x)

            total.append(a)
        total = np.array(total).flatten()
    else:
        for num in ch_ind:
            a = []
            for i in np.arange(num, num+accumulator, 1):
                row = np.arange(i, accumulator*tarh+num, accumulator)

                for x in row:
                    a.append(x)

            total.append(a)
        total = np.array(total).flatten()

    # for num in ch_ind:
    #     a = []
    #     for i in np.arange(num, num+accumulator, 1):
    #         row = np.arange(i, accumulator*tarh+num, accumulator)

    #         for x in row:
    #             a.append(x)

    #     total.append(a)
    # total = np.array(total).flatten()
#     print(total.shape)

    ############################
    # End of complet 500 boxes
    ############################

    

    # and the last not-complete box

    if num_left != 0:
        complete_row = num_left // tarh
        accumulator2 = complete_row
        n_last_row = num_left - complete_row * tarh
        new_starter = total[-1]+1

        ch_ind = np.arange(new_starter, num_left+new_starter,
                           tarh*accumulator2)  # Perform better

        ###
        # About ch_ind
        ###

        # it gives a 1-d array if we have no-completed row
        # it gives a 2-d array if we DON'T HAVE a no-completed row

        total2 = []
        if ch_ind.shape == (1,):
            a = []
            for i in np.arange(ch_ind[0], ch_ind[0]+accumulator2, 1):
                row = np.arange(i, accumulator2*tarh+ch_ind[0], accumulator2)

                for x in row:
                    a.append(x)

            total2.append(a)
        # Contains index shoro of not-completed-box + index shoro of row of not-completed
        if ch_ind.shape != (1,):
            for num in ch_ind[:-1]:
                a = []
                for i in np.arange(num, num+accumulator2, 1):
                    row = np.arange(i, accumulator2*tarh+num, accumulator2)

                    for x in row:
                        a.append(x)

                total2.append(a)

        total2 = np.array(total2).flatten()

        ##########################
        # End of completed rows
        ##########################

        if n_last_row != 0:
            last_items = np.arange(ch_ind[-1], ch_ind[-1] + n_last_row)

            total2 = np.concatenate((total2, last_items))
        total = np.concatenate((total, total2))
#         print(total.shape)
#         print(total[-1])

        #######################
        # End OF PROGRAMM
        #######################

        total = total.astype(dtype='str')
#     print(total.dtype)
        if add_zeros:

            total = [x.zfill(7) for x in total]
            total = np.array(total, dtype='str')
            return total
        else:
            return total

    else:
        if add_zeros:
            total = total.astype(dtype='str')
            total = [x.zfill(7) for x in total]
            total = np.array(total, dtype='str')
            return total

        else:  # NOT add zero for completed 500_box num_in_palets
            total = total.astype(dtype='str')
            return total