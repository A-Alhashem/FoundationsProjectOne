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
    print("We have the following: ")
    for x in menu:
        print ("%s is %sKD" % (x, menu[x]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for x in original_flavors:
        print (x)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for x in signature_flavors:
        print (x)


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
    order = str(input("Please enter your order in exact words, or type exit to cancel: "))
    order = order.lower()
    while order != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input().lower()

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
    print (order_list)
    print("total price is %s KD" % get_total_price(order_list))

    # NOTE TO INSTRUCTOR, I tried but I actually don't remember how to do this step!
