def heihua_translate(heihua_dict:dict,heihua:str)->str:
    str_list = heihua.split(',')
    if str_list[1] in heihua_dict:
        result = str_list[0].replace(str_list[1],heihua_dict[str_list[1]])
    return result
heihua_dict = {'xswl':'笑死我了','dbq':'对不起','cxk':'蔡徐坤'}
heihua_sentence = input("请输入包含黑话的字符串,黑话，并用英文逗号分隔")
print(heihua_translate(heihua_dict,heihua_sentence))