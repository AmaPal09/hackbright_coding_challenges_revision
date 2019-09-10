def melon_count(day_num, path): 
    """Produces report for given day number & path delivery report
       
       Opens the delivery report at the path provided and processes
       each line to print the report
    """

    print("Day {}".format(day_num))
    the_file = open(path)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        # print(words)

        melon = words[0] 
        count = words[1] 
        amount = words[2]
        # source the correct values for printing

        # print(melon, count, amount)
        print("Delivered {} {}s for total of ${}".format(count, melon, amount))
    the_file.close()

melon_count("1", "um-deliveries-20140519.txt" )
melon_count("2", "um-deliveries-20140520.txt" )
melon_count("3", "um-deliveries-20140521.txt" )