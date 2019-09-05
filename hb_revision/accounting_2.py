#SALESPERSON_INDEX = 0
#INTERNET_INDEX = 1
#DORKY_LINE_LENGTH = 80

dorky_line_length = 80

#prints line with * for 80 chars
print("*" * dorky_line_length)

#function for calculating the types of melons
def melon_tally_calculator (order_type_file_name): 
    """ Calculates total number of melons for each type

        Input: File containing oder details for each type
    """
    #dict for storing various melon types and their counts
    melon_tallies = {"Musk":0, 
                     "Hybrid":0, 
                     "Watermelon":0, 
                     "Winter": 0}
    #open input file
    order_type_file = open(order_type_file_name)

    #read each line of the file
    for order in order_type_file:
        #split the file line on |
        order_details = order.split("|")
        #obtain melon type from the 2nd position in order_details
        melon_type = order_details[1]
        #obtain count of melons from the 3rd position in order_details
        melon_count = int(order_details[2])
        #for each type of melon add the count to the counts in melon_tallies 
        melon_tallies[melon_type] += melon_count


    #close the input file. 
    order_type_file.close() 

    #dict containing various melon types and their pricea
    melon_prices = { "Musk": 1.15, 
                     "Hybrid": 1.30, 
                     "Watermelon": 1.75, 
                     "Winter": 4.00 } 
    #variable to store total revenue of each melon type. 
    total_revenue = 0 
    for melon_type in melon_tallies: 
        price = melon_prices[melon_type] 
        revenue = price * melon_tallies[melon_type] 
        total_revenue += revenue
        # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)) 
        print("We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(
                melon_tallies[melon_type], 
                melon_type, 
                price, 
                revenue)) 
        
    print("*" * dorky_line_length)


#function to obtain the sales details for each order type
def melon_sales_calculator (order_sale_file_name): 
    """ Calculates the total sales by sale person and total sales by internet 

    INPUT: file containing order with sales details

    """
#f = open("orders-with-sales.txt")
    #open input file
    order_sale_file = open(order_sale_file_name)
    
    #sales = [0, 0]
    #dict to store salesperson sale internet sale
    sales_tallies = {"Internet": 0 , "Person": 0}
    
    for sale in order_sale_file: 
        #split the file line on |
        sale_details = sale.split("|") 
        #if 0 is present in the 1st position in sale details its internet sale
        if sale_details[1] == "0": 
            #add the sale from 2nd position in sale details to internet sale
            sales_tallies["Internet"] += float(sale_details[3]) 
        #else its an sales person sale
        else: 
            #add the sale from 3rd position in the sale details to person sale
            sales_tallies["Person"] += float(sale_details[3]) 

    #print the sale details for sales person sale and internet sale 
    print("Salespeople generated ${:.2f} in revenue.".format(sales_tallies["Person"]))
    print("Internet sales generated ${:.2f} in revenue.".format(sales_tallies["Internet"]))

    #compare totals of internet sale and sales person sale 
    #if sales person sales are more than internet sales
    if sales_tallies["Person"] > sales_tallies["Internet"]:
        #print below statment
        print("Guess there's some value to those salespeople after all.")
    #else
    else:
        #print below statment
        print("Time to fire the sales team! Online sales rule all!")

    #print * line for formatting
    print("*" * dorky_line_length)

#execute melon_tally_calculcator function
melon_tally_calculator('orders-by-type.txt')
#execute melon_sales_calculcator function
melon_sales_calculator('orders-with-sales.txt')