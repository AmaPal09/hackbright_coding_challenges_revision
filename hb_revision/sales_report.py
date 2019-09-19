"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

def create_sales_report(filename): 
    """ Create sales report for file provided""" 

    sales_report_dict = {}
    f = open(filename)

    for line in f:
        # split the line into a list on | after stripping it
        line = line.rstrip()
        entries = line.split("|")

        salesperson = entries[0]
        melons = int(entries[2])

        sales_report_dict[salesperson] = sales_report_dict.get(salesperson, melons) + melons

    f.close()

    return sales_report_dict


def print_sales_report(report_dict): 
    """ Print the sales report """

    for salesperson, melons in report_dict.items():
        print("{} sold {} melons".format(salesperson, melons))


sales_report_dict = create_sales_report("sales-report.txt")
print_sales_report(sales_report_dict)