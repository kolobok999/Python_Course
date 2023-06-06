new_lst = []
    for idx, el in enumerate(lst):
        if el > lst[idx -1] and el > lst[idx - len(lst) + 1]:
            new_lst.append(el)