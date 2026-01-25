"""Create a list of 5 automation tools you know.

Convert it to a tuple and print it.

Create a dictionary that stores project name, tools used, and duration.

Add a new key ‘status’: ‘Completed’ to it dynamically."""

automation_tools = ["pytest", "Robot", "slash", "postman", "swagger"]
print(automation_tools)
tuple1 = tuple(automation_tools)
print(tuple1)
dict1 = {
    "name": "Project1",
    "tools": automation_tools,
    "duration": 3.5
}
print(dict1)
dict1["status"] = "Completed"
print(dict1)