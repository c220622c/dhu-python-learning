
fruits_data = []
total_sales = 0
f = open("exam_4/fruit.txt", 'r', encoding='utf-8')
lines = f.readlines()

# 跳过标题行，从第二行开始读取
for i in range(1, len(lines)):
    line = lines[i].strip()
    if line:  # 跳过空行
            parts = line.split(',')
            if len(parts) >= 3:
                fruit_name = parts[0]
                quantity = int(parts[1])
                price = float(parts[2])
                sales = quantity * price
                
                fruits_data.append({
                    'name': fruit_name,
                    'quantity': quantity,
                    'price': price,
                    'sales': sales
                })
                total_sales += sales

# 输出销售额超过4000元的水果
for fruit in fruits_data:
    if fruit['sales'] >= 4000:
        print(f"{fruit['name']}: {fruit['sales']:.2f}元")

# 输出所有水果的总销售额
print(f"所有水果总销售额: {total_sales:.2f}元")
