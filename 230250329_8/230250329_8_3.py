f1 = open("/Users/wzj/Documents/Coding-repo/dhu-python/230250329_8/newscore.txt", "r")
r1 = list(f1.readlines())
class_student = {}
for line in r1:
    line = line.rstrip("\n")
    sid, sname, sclass, sscore = line.split(",")
    # print(class_student.get(sclass))
    sscore_level = int(sscore) // 10
    # print(sscore_level)
    if class_student.get(sscore_level) == None:
        class_student[sscore_level] = 1
    else:
        class_student[sscore_level] += 1
sorted_keys = sorted(class_student.keys())
class_student[sorted_keys[1]] += class_student[sorted_keys[0]]
class_student[sorted_keys[-2]] += class_student[sorted_keys[-1]]
sorted_keys.pop(0)
sorted_keys.pop(-1)
print(
    f"[{sorted_keys[-1]*10},{sorted_keys[-1]*10+10}]有：{class_student[sorted_keys[-1]]}人"
)
for key in reversed(sorted_keys[0:-1]):
    print(f"[{key*10},{key*10+10})有：{class_student[key]}人")
