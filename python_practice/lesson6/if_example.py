my_age = 21
if my_age == 20: #True
    print("You are 20")

# and or is not

card_number = 1111222233334443
cvv = 125

# if card_number == 1111222233334444 and cvv == 124: #if True and True -> True / if False and True -> False
#     print("Transaction is complete")
# elif card_number != 1111222233334444:
#     print("Wrong card number")
# elif cvv != 124:
#     print("Wrong cvv")
# else:
#     print("Something goes wrong")

# if True:
#     print("True")
# if False:
#     print("False")
#
# if card_number == 1111222233334444 or cvv == 123: #if False or True -> True
#     print("Transaction is complete")


# response = []
# if not response: # if not False -> if True
#     print("Empty response")

if card_number == 1111222233334444 and cvv == 124:
    print("Transaction is complete")
else:
    print("Transaction is canceled")
    if card_number != 1111222233334444:
        print("Wrong card number")
    if cvv != 124:
        print("Wrong cvv")

#if
#if
#elif
    #if

#else