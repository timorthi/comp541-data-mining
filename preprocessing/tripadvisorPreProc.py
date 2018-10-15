import csv
f = open('tripadvisor_in-restaurant_sample.csv', encoding="UTF-8")
output = open('tripadvisor_data_processed_USA.csv', 'w', encoding="UTF-8")
csv_f = csv.reader(f)

count = 0

for row in csv_f:
    if (row[7] == 'United States'):
        output.write('"'+row[0].replace(',',' ')+'","')
        output.write(row[2].replace(',',' ')+'","')
        output.write(row[3].replace(',',' ')+'","')
        output.write(row[5].replace(',',' ')+'","')
        output.write(row[6].replace(',',' ')+'","')
        output.write(row[7].replace(',',' ')+'","')
        output.write(row[8].replace(',',' ')+'","')
        output.write(row[12].replace(',',' ')+'","')
        output.write(row[13].replace(',',' ')+'","')
        output.write(row[15].replace(',',' ')+'","')
        output.write(row[19].replace(',',' ')+'","')
        output.write(row[22].replace(',',' ')+'","')
        output.write(row[23].replace(',',' ')+'","')
        output.write(row[27].replace(',',' ')+'","')
        output.write(row[0].replace(',',' ')+'"\n')
        count += 1

print(count)

f.close()
output.close()
