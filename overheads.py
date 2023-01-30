#Import overhead csv
import csv


def highest_overhead():
    #"open" function is used to open the "cash-on-hand-usd.csv" in read mode and assign it to "file" variable
    with open('csv_reports/overheads-day-90.csv', 'r') as file:
        #csv.reader is used to create a reader object for the file
        reader = csv.reader(file)
        #Skips the header row of the csv file
        next(reader)

        #Create empty lists to store the categories and overhead amounts
        categories = []
        overheads = []

        #Create a for loop to iterate and append the categories and overhead amounts into the empty lists
        for category,overhead in reader:
            categories.append(category)
            #Change overhead to float data type before appending into empty list
            overheads.append(float(overhead))
    #Use max() function to find the highest overhead amount
    #Use .index() function to find the index position of highest overhead amount and assign to "highest_overhead_index" variable
    highest_overhead_index = overheads.index(max(overheads))
    #Open summary_report.txt file in write mode and write highest overhead category with amount
    with open("summary_report.txt", "w") as txtfile:
        txtfile.write(f"[HIGHEST OVERHEADS] {categories[highest_overhead_index].upper()}: {overheads[highest_overhead_index]}%\n")