num1 = int(input("Enter a number1 : "));
num2 = int(input("Enter a number2 : "));
operator = input("Enter a operator");
match operator:
    case "+":
        print("Sum is :", num1 + num2);
    case "-":
        print("Difference is :",num1-num2);  
    case "%":
        print("Modulo is :",num1 % num2);
    case "/":
        print("The division is :",num1/num2);
    case "*":
        print("The product is :",num1*num2);
    case "//":
        print("the floor value is :",num1//num2);
    case "**":
        print("The powe is :",num1 ** num2);
    case _:
        print("enter a valid operator");