print(" You can Choose the process : " , "\n",
      "1- +"
      ,"\n" ,
      "2- -"
      , "\n",
      "3- *"
      , "\n",
      "4- /"
      , "\n",
      "5- ^"
      )
number =input("Enter First number ")

if number.isdigit():
    number=int(number)
    op = input("Enter the process ")
    number2 = input("Enter second number ")
    if number2.isdigit():
        number2=int(number2)
        if op == "1" or op == "+":
            total = number + number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))

        elif op == "2" or op == "-":
            total = number - number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))

        elif op == "3" or op == "*":
            total = number * number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))

        elif op == "4" or op == "/":
            total = number / number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))

        elif op == "5" or op == "^":
            total = number ^ number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))

        elif op == "6" or op == "%":
            total = number % number2
            print("real total :", total)
            print("nearly :", round(total))
            print("integer value: ", int(total))
        else:
            print("Error in your input operator")
    else:
        print("invalid value2")

else:print("invalid value number 1")

