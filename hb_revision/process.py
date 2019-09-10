log_file = open("um-server-01.txt")
#It opens the um-server-01 files and loads it to log_file

def sales_reports(log_file):
    """Function for print sales report

    It prints the log report for a particular day coded in the function """
    for line in log_file:
        # reads each new line in the code
        line = line.rstrip()
        # strinps the line of any blank spaces at the end on the right
        day = line[0:3]
        # loads the characters in the first 3 position in the line to day
        # variable
        if day == "Mon":
            # Made changes to print log for Monday instead of Tuesday
            print(line)


sales_reports(log_file)
