import csv
dataset1 = []
dataset2 = []
with open('bright_stars.csv', 'r')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
        
with open('dwarf_stars.csv', 'r')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
        
headers1 = dataset1[0]
star_data1 = dataset1[1:]
headers2 = dataset2[0]
star_data2 = dataset2[1:]
headers = headers1 + headers2
star_data = []
for index, data_row in enumerate(star_data1):
    star_data.append(star_data1[index] + star_data2[index])
    
with open('final.csv', 'a+')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)