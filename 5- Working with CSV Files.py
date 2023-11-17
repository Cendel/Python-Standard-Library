# CSV (Comma-separated Value)

import csv

with open("test_folder/data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# in order to open it in read mode:
with open("test_folder/data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))  # gets all the data in the zip file and converts it into a list object
    # we can also iterate over it:
    for row in reader:
        print(row)