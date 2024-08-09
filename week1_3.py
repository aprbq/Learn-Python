import csv
with open('std_record.csv', mode='r') as f:
    r = csv.reader(f, delimiter=',')
    print("{:10}{:5}{:20}{:12}{:8}".format("Name","Age","E-mail","Mobile","Sex"))
    for i in r:
        print("{:10}{:5}{:20}{:12}{:8}".format(i[0],i[1],i[2],i[3],i[4]))
