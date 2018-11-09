####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Koanda"
signature_flavors = ["watermelon", "grapes", "kiwi"]
order_list = []



def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print()
    print("We have the following: ")
    print()
    print("---------------------------------------------")
    for x in menu:
        print ("- %s is: %.3fKD" % (x, menu[x]))
    print("---------------------------------------------")
    print()


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print(" ==== Our original flavor cupcakes (KD %.3f each) =======" % original_price)
    print()
    for x in original_flavors:
        print ("- %s" % (x))
    print()

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print(" ==== Our signature flavor cupcake (KD %.3f each) ====" % signature_price)
    print()
    for x in signature_flavors:
        print ("- %s" % (x))
    print ()


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu:
        return True
    elif order in signature_flavors:
        return True
    elif order in original_flavors:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print("Please enter your order in exact words, or type \"exit\" to cancel: ")
    print()
    order = str(input())
    order = order.lower()
    while order != "exit":
        if is_valid_order(order):
            order_list.append(order)
        else:
        	print("		=====================================")
        	print("I'm sorry, we currently do not have \"%s\", please choose another, or use lower case letters:" % order.upper())
        	print("		=====================================")
        	print()
        order = input().lower()
    print()

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in menu:
            total = total + menu[order]
        elif order in original_flavors:
            total = total + original_price
        elif order in signature_flavors:
            total = total + signature_price
        else:
            return False

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    print()
    for order in order_list:
    	
    	print("- %s" % order)
    print()
    print()

    total_price = get_total_price(order_list)
    print("The total price is: ")
    print("        ____________")
    print("       | %.3f KD   |" % total_price)
    print("        ------------")

    import time

    print("						Checking credit card validity based on price... ")
    time.sleep(3)
    if accept_credit_card(total_price):
    	print("					\"We do accept credit card if you wish to use it\"")
    else:
    	print("					\"We are sorry, we only accept \"CASH\" for orders under 5 KD\"")

    print()
    time.sleep(2)
    print("						Thank you for shopping at \"%s\"" % cupcake_shop_name.upper())
    print("							Have a great day!")
    print()

  
