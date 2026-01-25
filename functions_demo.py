"""
Hands-On Assignments

1️⃣ Create a function that accepts a list of logs and returns only those containing "ERROR".
2️⃣ Write a function that takes two numbers and returns both their sum and product.
3️⃣ Write a recursive function to calculate factorial of a number.
4️⃣ Create a lambda function to square numbers from a list.
"""
def log_error(logs):
    error_logs = [log for log in logs if "ERROR" in log]
    return error_logs


log_list = list(input("log_list ").split(" "))
print(log_list)
errors = log_error(log_list)
print("errors: ", errors)

