from datetime import datetime




n = datetime.now()
print('%02d-%02d-%04d' % (n.month, n.day, n.year))
print('%02d-%02d-%02d' % (n.hour, n.minute, n.second))
print('%02d-%02d-%04d %02d:%02d:%02d' % (n.month, n.day, n.year, n.hour, n.minute, n.second))
#l = []
#for _ in range(0, int(input())):
#    k = input()
#    v = list(map(int, input().split()))
#    d = {k:v}

#    l.append(d)
#s = input()
#for i in l:
#    if(s in i):
#        print(sum(i[s])//len(i[s]))

#        #print(avg(i["s"]))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print("{0:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))