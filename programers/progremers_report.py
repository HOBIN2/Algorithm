id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
mail = [0]*len(id_list)
report_count = [0]*len(id_list)
for i in report:
    report_men = i.split(" ")[1]
    report_count[id_list.index(report_men)] += 1
for j in report_count:
    print(report_count.index(j))
dic_report = {id: [] for id in id_list}
print(dic_report)
print(set(report))
print(dic_report['muzi'])