import csv

def profit_loss():
    profitandloss = []
    profit_results = 0
    profit_details = 0
    profit_deficit_day = []
    profit_deficit_amt = []
    profit_surplus = 0

    #Creating file path for the excel
    with open('csv_reports/profit-and-loss-usd.csv', 'r') as file:

        # instantiate a reader object
        reader = csv.reader(file)
        # use `next()` to skip the header.
        next(reader)


    # Create nested loop to access each value in the list
    # and append the value to the dict.
        for line in reader:
                for value in line:
                    profitandloss.append(value)
    for i in range(4,len(profitandloss)-4,5):
        if float(profitandloss[i+5]) - float(profitandloss[i])>0:
            profit_surplus = profit_surplus + 1   
        elif int(profitandloss[i+5]) - int(profitandloss[i])<=0:
            profit_deficit_day.append(profitandloss[i+1])
            profit_deficit_amt.append(abs(int(profitandloss[i+5])-int(profitandloss[i])))
   
    if profit_surplus == len(profitandloss)/2:
        profit_results = "HIGHER"
        profit_details = "NET PROFIT SURPLUS"
    elif profit_surplus == 0:
        profit_results = "LOWER"
        profit_details = "NET PROFIT LOSS"
    else:
        profit_details = "PROFIT DEFICIT" 
    


    with open("summary_report.txt", "a") as f:
        
        if profit_results == 0:

            for m in range (len(profit_deficit_amt)):
                f.write("[{0}] DAY: {1}, AMOUNT: USD {2}\n".format(profit_details,profit_deficit_day[m],profit_deficit_amt[m]))
        
        else:
            f.write("[{0}] NET PROFIT ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(profit_details,profit_results))
