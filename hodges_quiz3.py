def t_tropic(climate: str):
    temp_list = []
    while True:
        temp = float(input("Enter a temperature (enter '0' to exit): "))
        if temp == 0:
            break
        temp_list.append(temp)
    for temp in temp_list:
        if climate == "Tropical":
            if temp <= 30:
                print("F")
            else:
                print("U")
        elif climate == "Continental":
            if temp <= 25:
                print("F")
            else:
                print("U")
        else:
            if temp <= 18:
                print("F")
            else:
                print("U")