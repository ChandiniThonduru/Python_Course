from calc import fact, sine_cos_tan
#handling of exceptions

try:
    #Exception may occur
    x = int(input("Enter a Number: "))
    result = fact(x)               # No errors
    #result = factOfNumber(x)      occurs variable name error
    #result = fact(x)/0            arithmetic error will occur
    print("Result:", result)

except KeyboardInterrupt:
    print("\nKeyboard Interrupt occurred.")

except NameError:
    print("\nName Error occurred. Please check your variable names.")

except ArithmeticError:
    print("\nArithmetic Error occurred. Division by zero is not allowed.")

else:
    # Executed if no exception occurs
    print("\nNo exception occurred.")

finally:
    # Executed regardless of whether an exception occurs or not
    print("Program execution completed.")