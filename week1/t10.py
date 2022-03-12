def bob_function(message):
    print(message[0])  # alef
    if "K" in message:  # be
        print("K")
    print(message.split())  # pe
    for i in range(0, len(message), 2):  # te
        print(message[i], "", end="")
    for i in message:  # dal
        if i == str("m"):
            print("\nTrue")
            break


bob_function(message="Babak Khorramdin")
