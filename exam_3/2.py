f1 = open("exam_3/record.txt", 'r', encoding="utf-8")
sentences = f1.readlines()
hero_skills_dict = {}
all_skills = set()

for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        # 按冒号分隔姓名和武功列表
        parts = sentence.split(':')
        hero = parts[0]
        skills = parts[1].split(',')
        # 统计该人物的武功数量
        hero_skills_dict[hero] = len(skills)
        # 添加到所有武功集合中
        for skill in skills:
            all_skills.add(skill.strip())

f1.close()

# 输出会三种以上武功的武侠人物信息
for hero in hero_skills_dict:
    if hero_skills_dict[hero] > 3:
        print(f"{hero},武功数量:{hero_skills_dict[hero]}")

# 输出武功总数
print(f"武功总数:{len(all_skills)}")
