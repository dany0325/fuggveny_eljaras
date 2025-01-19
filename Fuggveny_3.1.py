def harommal_oszthatok(lst):
    divby3count = 0
    for i in lst:
        if i % 3 == 0:
            divby3count += 1
    return divby3count


print(harommal_oszthatok([213,3,3,3,3,12,1,2]))