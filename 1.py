import csv

with open('scientist.txt', 'r', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    scientist = []
    preparations = []
    fake = []
    reader = sorted(reader, key=lambda x: (x['date']))
    for row in reader:
        if row['preparation'] not in preparations:
            preparations.append(row['preparation'])
            scientist.append(row)
        else:
            fake.append(row)

with open('scientist_origin.txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    writer.writeheader()
    writer.writerows(scientist)

print()
