def issue1(ten_thousands: int):
    if ten_thousands < 10000 or ten_thousands > 99999:
        print("应输入五位整数")
        return 1
    else:
        ten_thousands = str(ten_thousands)
        return [ten_thousands[-1], ten_thousands[-4]]


test_data = [12345, 34980, 10000, 98765]
for i in range(len(test_data)):
    answer = issue1(test_data[i])
    print(f"{test_data[i]}的各位数是{answer[0]},千位数是{answer[1]}")
