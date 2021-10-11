#collect the array information
#run the information through the different functions
#a function to average that uses the array and returns average
#a function to display numbers over average that uses the array and the average and returns the number over average
#a function to determine the top sales and return the sales and index location
#a main function that will call the other functions and output the data


#function that returns the array
def Sales():
     sales = [25478, 38749, 18749, 45247, 27481, 54632, 22749]
     return sales

#function that will average the data and return it
def Average(sales):
    total = 0
    average = 0
    for index in range(len(sales)):
        total = total + sales[index]
    average = total / len(sales)
    average = round(average, 2)
    return average

#function that will determine the amount of sales above the average and returns it
def OverAvg(average, sales):
    overavg = 0
    for index in range(len(sales)):
        if sales[index] > average:
            overavg = overavg + 1
    return overavg

#a function to determine the top sale and the location in the array, and returns them
def Top(sales):
    top = 0
    for index in range(len(sales)):
        if sales[index] > top:
            top = sales[index]
            location = index
    return top, location

#main to call our functions and output the data to the screen
def main():
    sales = Sales()
    average = Average(sales)
    overavg = OverAvg(average, sales)
    print("The Average jewelery sales was:", average, "\nThe number of sales that exceeded this was:", overavg)
    top, location = Top(sales)
    print("The highest sale was:", top, "and it was found in index:", location)

#calling our program
main()