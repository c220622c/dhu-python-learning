def issue2():
    plaintext = str(input("请输入四位数明文: "))
    if len(plaintext) != 4 or not plaintext.isdigit():
        print("输入错误,请输入四位数明文")
        return False
    else:
        plaintext = list(plaintext)
        for i in range(4):
            plaintext[i] = str((int(plaintext[i]) + 5) % 10)
        plaintext[0], plaintext[2] = plaintext[2], plaintext[0]
        plaintext[1], plaintext[3] = plaintext[3], plaintext[1]
        plaintext = "".join(plaintext)
        print(f"密码:{plaintext}")
        return True


issue2()
