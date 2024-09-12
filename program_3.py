def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.
    item1 = float(input('Enter item #1: '))
    item2 = float(input('Enter item #2: '))
    item3 = float(input('Enter item #3: '))
    item4 = float(input('Enter item #4: '))
    item5 = float(input('Enter item #5: '))

    subtotal = round(item1 + item2 + item3 + item4 + item5)

    tax = round((subtotal * 0.07), 2)

    total = subtotal + tax

    print('$',subtotal, sep='')
    print('$',tax,sep='')
    print('$',total,sep='')



calculate_total_purchase()