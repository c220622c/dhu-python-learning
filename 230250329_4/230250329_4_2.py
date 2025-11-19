def find_narcissus(n:int) -> list:
    result = []
    for i in range(10**(n-1),10**n):
        str_i = str(i)
        add_up = 0
        for j in range(len(str_i)):
            add_up = add_up+int(str_i[j])**n
        if add_up == i:
            result.append(i)
    return result
def is_odd(input_number:list)->list:
    odd_numbers = []
    for num in input_number:
        if num % 2 == 1:
            odd_numbers.append(num)
    return odd_numbers
def main():
    digits = 3
    odd_narcissus_list = is_odd(find_narcissus(digits))
    print(f"所有为奇数的{digits}位水仙花数为:")
    for odd_narcissus in odd_narcissus_list:
        print(odd_narcissus)
main()
