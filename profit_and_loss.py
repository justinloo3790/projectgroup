#Import csv module
import csv

def profit_loss():
    #Lists and Variables
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


        #Create nested loop to access each value in the list and append the value to the 'profitandloss' list.
        for line in reader:
                for value in line:
                    profitandloss.append(value)
    
    #The 'i' in the loop represents the position of the value in the list
    #The loop starts from the 4th number in the list and only takes the net profit of each day which are in intervals of 5 in the 'profitandloss' list               
    for i in range(4,len(profitandloss)-4,5):
        #if the value of the current day is higher than the value of the previous day
        if float(profitandloss[i+5]) - float(profitandloss[i])>0:
            #it will add 1 into the profit_surplus variable
            profit_surplus = profit_surplus + 1   
        #else if the value of the current day is lower or equal to the value of the previous day
        elif int(profitandloss[i+5]) - int(profitandloss[i])<=0:
            #the day when the value of the current day is lower or equal to the value of the previous day
            #is appended into the profit_deficit_day list
            profit_deficit_day.append(profitandloss[i+1])
            #the amount when the value of the current day is lower or equal to the value of the previous day
            #is appended into the profit_deficit_amt list
            profit_deficit_amt.append(abs(int(profitandloss[i+5])-int(profitandloss[i])))
    #The if else will summarise the results and determine whether if all of the days were more or less than the previous 
    #if its neither, it has a mixed number of losses and surpluses then it will be categorised as profit deficit
    if profit_surplus == len(profitandloss)/2:
        profit_results = "HIGHER"
        profit_details = "NET PROFIT SURPLUS"
    elif profit_surplus == 0:
        profit_results = "LOWER"
        profit_details = "NET PROFIT LOSS"
    else:
        profit_details = "PROFIT DEFICIT" 
    

    #Iterates items in the list and prints a message showing details of  
    #whether it is a net profit surplus, net profit loss or profit deficit with the amounts and day on the text file
    with open("summary_report.txt", "a") as f:
        
        if profit_results == 0:

            for m in range (len(profit_deficit_amt)):
                f.write("[{0}] DAY: {1}, AMOUNT: USD {2}\n".format(profit_details,profit_deficit_day[m],profit_deficit_amt[m]))
        
        else:
            f.write("[{0}] NET PROFIT ON EACH DAY IS {1} THAN THE PREVIOUS DAY\n".format(profit_details,profit_results))
