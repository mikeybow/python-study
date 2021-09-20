price = 1000000
good_credit = True


if good_credit:
    down_payment = 0.1 * price
    print('You owe 10 percent down paymemnt')
else:
    down_payment = 0.2 * price
    print('You owe a 20 percent down payment')
print(f"down_payment: ${down_payment}")