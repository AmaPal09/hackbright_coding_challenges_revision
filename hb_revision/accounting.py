melon_cost = 1.00


def melon_payment_calculator(payment_file_name): 
    """Payment calculation and verification for melons

    Opens the file with the payment details, process the payment needed 
    to be done by each customer for each pruchase and the looks for
    any underpayment issue
    """
    payment_file = open(payment_file_name) 
    # open the file with payment details

    for lines in payment_file: 
        # iterates through each line in the file

        transaction_detail = lines.split("|")
        #get ride of the | in each line

        customer_name = transaction_detail[1]
        customer_first_name = customer_name.split(" ")[0]
        #print(customer_name, customer_first_name)
        #get the first name of the customer

        customer_melons = float(transaction_detail[2])
        customer_paid = float(transaction_detail[3])
        #get the count of melons and payment done
        #print(transaction_detail[2],transaction_detail[3])

        customer_due = customer_melons * melon_cost

        
        # check if customer over or under paid for their melons
        if customer_due < customer_paid:
            print("{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_due))
            print("{} has overpaid for their melons.".format(customer_first_name))

        elif customer_due > customer_paid:
            print("{} paid ${:.2f}, expected ${:.2f}".format(
                customer_name, customer_paid, customer_due))
            print("{} has underpaid for their melons.".format(customer_first_name))
        

    # close the file
    payment_file.close()

melon_payment_calculator("customer-orders.txt")

"""
customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(customer1_name, "paid {:.2f}, expected {:.2f}".format(
        customer1_paid, customer1_expected))

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(customer2_name, "paid {:.2f}, expected {:.2f}".format(
        customer2_paid, customer2_expected))

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(customer3_name, "paid {:.2f}, expected {:.2f}".format(
        customer3_paid, customer3_expected))

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(customer4_name, "paid {:.2f}, expected {:.2f}".format(
        customer4_paid, customer4_expected))

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(customer5_name, "paid {:.2f}, expected {:.2f}".format(
        customer5_paid, customer5_expected))

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(customer6_name, "paid {:.2f}, expected {:.2f}".format(
        customer6_paid, customer6_expected))
"""

