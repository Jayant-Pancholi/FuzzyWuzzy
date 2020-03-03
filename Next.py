import csv
from fuzzywuzzy import fuzz

id = input("Enter ID : ")
title = input("Enter title : ")
author = input("Enter author : ")
format = input("Enter format : ")
price = input("Enter price : ")

with open('data3.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    mylist = []
    # templist = []
    for row in readCSV:
        row = str(row)
        mylist.append(row)
    templist = [id, title, author, format, price]
    while mylist:
        for match in mylist:
            matchli=list(match.split(","))
            matchstr = "".join(map(str, matchli))
            matchstr = (str(matchstr)).replace("'", "")
            matchstr = (str(matchstr)).replace(" ", "")
            matchstr = (str(matchstr)).replace("[", "")
            matchstr = (str(matchstr)).replace("]", "")

            inputstring = "".join(templist)

            count = fuzz.partial_ratio(inputstring, matchstr)
            print(count)
            if count > 90:
                print(match)
                print("Matched")
                # break
            else:
                print(templist)
        del templist[-1]


        del mylist[-1]
        break
