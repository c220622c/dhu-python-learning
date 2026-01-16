students_count = 0
results = []
with open("exam_5/scores_raw.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
    # 跳过标题行
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line:  # 跳过空行
            parts = line.split(',')
            if len(parts) == 3:
                name = parts[0]
                daily_score = float(parts[1])
                final_score = float(parts[2])
                
                # 计算总评成绩
                total_score = daily_score * 0.4 + final_score * 0.6
                
                # 存储结果
                results.append(f"{name}:{total_score:.1f}")
                students_count += 1

# 写入输出文件
with open("exam_5/final_report.txt", 'w', encoding='utf-8') as f:
    for result in results:
        f.write(f"{result}\n")

# 输出处理完成信息
print(f"处理完成，共处理了 {students_count} 名学生数据")
