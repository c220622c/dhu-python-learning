f1 = open("/Users/wzj/Documents/Coding-repo/dhu-python/230250329_8/newscore.txt", "r")
r1 = list(f1.readlines())
class_student = {}
for line in r1:
    line = line.rstrip("\n")
    sid, sname, sclass, sscore = line.split(",")
    grade = sid[0:2]
    if class_student.get(grade) == None:
        class_student[grade] = 1
    else:
        class_student[grade] += 1
for k, v in class_student.items():
    print(f"{k}级有{v}人")
