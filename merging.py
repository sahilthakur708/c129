import csv

data_1=[]

with open("bright_stars.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data_1.append(row)

headers_1=data_1[0]
stars_data_1=data_1[1:]

data_2=[]

with open("sorted_data_final.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data_2.append(row)

headers_2=data_2[0]
stars_data_2=data_2[1:]

headers=headers_1+headers_2

stars_data=[]

for index,row in enumerate(stars_data_1):
    stars_data.append(stars_data_1[index]+stars_data_2[index])

with open("merged_data.csv",'a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)