import csv

data=[]

with open("dwarf_stars.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers=data[0]
stars_data=data[1:]

for row in stars_data:
    row[2]=row[2].lower()

stars_data.sort(key=lambda stars_data:stars_data[2])

with open ("sorted_data.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)

with open ("sorted_data.csv") as input, open ('sorted_data_final.csv','w',newline='') as output:
    csv_writer=csv.writer(output)
    for row in csv.reader(input):
        if any (field.strip() for field in row):
            csv_writer.writerow(row)

