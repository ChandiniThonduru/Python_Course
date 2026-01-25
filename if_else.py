"""
Simple Login Validation
📌 Problem:

Validate user login based on username and password.
"""
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin":
    if password == "admin123":
        print("Login successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")


"""
Electricity Bill Calculation
📌 Problem:

Calculate electricity bill based on units consumed.

🔹 Input:

Units consumed (integer)

🔹 Conditions:
Units	Rate
0 – 100	₹5 per unit
101 – 200	₹7 per unit
> 200	₹10 per unit
🔹 Output:

Total electricity bill amount
"""

units_consumed = int(input("Enter the units consumed: "))
if 0 <= units_consumed <= 100:
    print("Total electricity bill amount ", units_consumed*5)
elif 101 >= units_consumed <= 200:
    print("Total electricity bill amount ", units_consumed * 7)
elif units_consumed > 200:
    print("Total electricity bill amount ", units_consumed * 10)

"""
ATM Withdrawal Program
📌 Problem:

Simulate ATM withdrawal with conditions.

🔹 Input:

Account balance (integer)

Withdrawal amount (integer)

🔹 Conditions:

Withdrawal amount must be multiple of 100

Withdrawal amount must be ≤ balance

Minimum balance of ₹500 should remain

🔹 Output:

Successful withdrawal with remaining balance
OR

Appropriate error message
"""
acc_bal = int(input("Enter Account balance (integer): "))
withdraw_amt = int(input("Enter Withdrawal amount (integer): "))

if withdraw_amt % 100 == 0:
    if withdraw_amt < acc_bal:
        if acc_bal - withdraw_amt >= 500:
            print("Successful withdrawal with remaining balance :", acc_bal - withdraw_amt)
        else:
            print("Minimum balance of ₹500 should remain")
    else:
        print("Withdrawal amount must be ≤ balance")
else:
    print("Withdrawal amount must be multiple of 100")
