import csv

with open('data2345.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            desc = row[7]
            desc = desc.replace('¬†','')

            row[7] = desc
            temp =[]

            prod = row[9]
            prod = prod.replace('\n',';')

            row[9] = prod

            temp.append(row)

            with open('final1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(temp)
