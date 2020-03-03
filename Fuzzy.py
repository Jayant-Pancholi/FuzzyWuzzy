import pandas as pd

from fuzzywuzzy import fuzz

import time as time

Guid = input("Enter GUID : ")
CompanyName = input("Enter Company Name : ")
Address1 = input("Enter Address : ")
City = input("Enter City : ")
State = input("Enter State : ")
Country = input("Enter Country : ")
Zip = input("Enter Zip : ")

cols = ['KUNNR', 'LAND1', 'NAME1', 'ORT01', 'PSTLZ', 'REGIO', 'ZADDRESS_LINE1']

sourcePath = 'data67.csv'

fields_to_list = []

counter = -1

df = pd.read_csv(sourcePath, skipinitialspace=True, usecols=cols)
df["KUNNR"] = df["KUNNR"].astype(str)


def getFuzzySearchOutput(inputString, concateStringId, counter):
    start_time = time.time()

    outputList = []

    matchper = []

    try:
        fields = concateStringId.values.tolist()
        if counter == -1:
            counter = 0
            # matchper = [fuzz.token_set_ratio(inputString, match.partition('--')[2]) for match in fields]
        for match in fields:
            matchper = fuzz.token_set_ratio(inputString, match.partition('--')[2])
            if matchper >= 90:
                outputList.append([(matchper, int(match.partition('--')[0]))])
                counter = counter + 1
        if counter >= 1:
            outputList = max(outputList)
            print("===============Output==============")
            print("GUID : " + Guid)
            print("Match Percentage : " + str(outputList[0][0]))
            print("Input String : " + inputString)
            print("Matched Id : " + str(outputList[0][1]))
            end_time = time.time()
            print("Time Taken(s) : " + str(end_time - start_time))
            exit(-1)
        else:
            counter = 0
            fields_to_list.clear()
    except Exception as e:
        raise Exception(e)


if CompanyName != "":
    if Address1 != "":
        if City != "":
            if State != "":
                if Country != "":
                    if Zip != "":
                        inputString = CompanyName + "," + Address1 + "," + City + "," + State + "," + Country + "," + Zip
                        # pass1
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["ORT01"], sep=",", na_rep="").str.cat(df["REGIO"], sep=",", na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="").str.cat(df["PSTLZ"], sep=",", na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        print("inside pass 1")
                        # break
                    elif Zip != "" or counter == 0:
                        print("inside pass 4")
                        inputString = CompanyName + "," + Address1 + "," + City + "," + State + "," + Country
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["ORT01"], sep=",", na_rep="").str.cat(df["REGIO"], sep=",", na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
            elif State == "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 2")
                        inputString = CompanyName + "," + Address1 + "," + City + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["ORT01"], sep=",", na_rep="").str.cat(df["LAND1"], sep=",", na_rep="").str.cat(
                            df["PSTLZ"], sep=",", na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                    elif Zip == "" or counter == 0:
                        print("inside pass 7")
                        inputString = CompanyName + "," + Address1 + "," + City + "," + Country
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["ORT01"], sep=",", na_rep="").str.cat(df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                elif Country == "":
                    if Zip != "" or counter == 0:
                        print("inside pass 3")
                        inputString = CompanyName + "," + Address1 + "," + State + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["REGIO"], sep=",", na_rep="").str.cat(df["LAND1"], sep=",", na_rep="").str.cat(
                            df["PSTLZ"], sep=",", na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
        elif City == "":
            if State != "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 5")
                        inputString = CompanyName + "," + Address1 + "," + State + "," + Country
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["ORT01"], sep=",", na_rep="").str.cat(df["REGIO"], sep=",", na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                    elif Zip == "" or counter == 0:
                        print("inside pass 12")
                        inputString = CompanyName + "," + Address1 + "," + Country
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
            elif State == "":
                if Country != "":
                    if Zip == "" or counter == 0:
                        print("inside pass 6")
                        inputString = CompanyName + "," + Address1 + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["ZADDRESS_LINE1"], sep=",", na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="").str.cat(df["PSTLZ"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
    elif Address1 == "":
        if City != "":
            if State != "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 8")
                        inputString = CompanyName + "," + City + "," + State + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["ORT01"], sep=",", na_rep="").str.cat(df["REGIO"],
                                                                                                     sep=",",
                                                                                                     na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="").str.cat(df["PSTLZ"], sep=",", na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                    elif Zip == "" or counter == 0:
                        print("inside pass 10")
                        inputString = CompanyName + "," + City + "," + State + "," + Country
                        concateString = df["NAME1"].str.cat(df["ORT01"], sep=",", na_rep="").str.cat(df["REGIO"],
                                                                                                     sep=",",
                                                                                                     na_rep="").str.cat(
                            df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
            elif State == "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 9")
                        inputString = CompanyName + "," + City + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["ORT01"], sep=",", na_rep="").str.cat(df["LAND1"],
                                                                                                     sep=",",
                                                                                                     na_rep="").str.cat(
                            df["PSTLZ"], sep=",", na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                    elif Zip == "" or counter == 0:
                        print("inside pass 14")
                        inputString = CompanyName + "," + City + "," + Country
                        concateString = df["NAME1"].str.cat(df["ORT01"], sep=",", na_rep="").str.cat(df["LAND1"],
                                                                                                     sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
        elif City == "":
            if State != "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 11")
                        inputString = CompanyName + "," + State + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["REGIO"], sep=",", na_rep="").str.cat(df["LAND1"],
                                                                                                     sep=",",
                                                                                                     na_rep="").str.cat(
                            df["PSTLZ"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                    elif Zip == "" or counter == 0:
                        print("inside pass 13")
                        inputString = CompanyName + "," + State + "," + Country
                        concateString = df["NAME1"].str.cat(df["REGIO"], sep=",", na_rep="").str.cat(df["LAND1"],
                                                                                                     sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
            elif State == "":
                if Country != "":
                    if Zip != "" or counter == 0:
                        print("inside pass 15")
                        inputString = CompanyName + "," + Country + "," + Zip
                        concateString = df["NAME1"].str.cat(df["LAND1"], sep=",", na_rep="").str.cat(df["PSTLZ"],
                                                                                                     sep=",",
                                                                                                     na_rep=" ")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
                    elif Zip == "" or counter == 0:
                        print("inside pass 16")
                        inputString = CompanyName + "," + Country
                        concateString = df["NAME1"].str.cat(df["LAND1"], sep=",", na_rep="")
                        concateStringId = df["KUNNR"].str.cat(concateString, sep="--", na_rep="")
                        # break
else:
    print("No Matching Input Pass for GUID : " + Guid)
    exit(-1)

# call function for fuzzysearch
getFuzzySearchOutput(inputString, concateStringId, counter)
