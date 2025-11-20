def Cid_Verify(cid:str)->str:
    factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last_dict = {0: "1", 1: "0", 2: "X", 3: "9", 4: "8", 5: "7", 6: "6", 7: "5", 8: "4", 9: "3", 10: "2"}
    Cid_Sum = 0
    for n in range(len(str(cid))-1):
        Cid_Sum += int(str(cid)[n])*int(factor[n])
    quotient = Cid_Sum%11
    if last_dict[quotient] == str(cid)[-1]:
        return "身份证号通过验证"
    else:
        return "身份证号非法"
print(Cid_Verify(input("请输入十八位身份证号：")))

