
# Importing OS and CSV modules 
import os
import csv

# Setting the path for the file 
csvpath = os.path.join(r"C:\Users\abc\Desktop\python-Challenge\PyBank\Resources\budget_data.csv")

#variable declaration   

months_list =[]
months = 0
profit_loss = []
revenue_change=[]

# Opening the CSV file excluding the header
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)

# Looping through each row in the file after the header
    for row in csvreader:
        m = row[0]  # assigning a variable that holds the first column for months
        p_l = row[1] # assigning a variable that holds the second column for profit/losses
        months_list.append(m)
        profit_loss.append(p_l)

# converting the profit_loss list to int so that we can perform arithmetic operations
  
    for i in range(0,len(profit_loss)):
        profit_loss[i] = int(profit_loss[i])

    m = len(months_list) # count the total months with the length function
    #print(m) checking to see if it works

    p_l = sum(profit_loss) # finding the sum of all the profit/losses
    # print(p_l) checking to see if it works

    # looping through the profit_loss list and calculating the difference between one month and the other
    for x in range(1,len(profit_loss)): 
        revenue_change.append((int(profit_loss[x]-int(profit_loss[x-1]))))

    #finding out the average by diving sum and the len of revenue change 
    revenue_average = sum(revenue_change)/len(revenue_change)
    #print(revenue_average)

     # greatest increase in revenue
    greatest_increase = max(revenue_change)
    #print(greatest_increase) checking to see if it works

    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)
    # print(greatest_decrease) checking to see if it works


   #Printing the Results 
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(m))

    print("Total: " + "$" + str(p_l))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months_list[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months_list[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease)+ ")")


    # output to a text file

    file = open(r"C:\Users\abc\Desktop\python-Challenge\PyBank\Analysis\Election Results.txt", "w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(m) + "\n")

    file.write("Total: " + "$" + str(p_l) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months_list[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")"+ "\n")

    file.write("Greatest Decrease in Profits: " + str(months_list[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")" + "\n")

    file.close()