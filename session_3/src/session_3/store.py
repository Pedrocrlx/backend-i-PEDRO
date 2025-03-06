class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} costs ${self.price:.2f}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"



# Create User instances
user = User("pedro", "pedrosantos@gmail.com")
user1 = User("diogo", "diogodomingues@gmail.com")
user2 = User("joreg", "joreg@gmail.com")


# Define the AddUser function
def AddUser(*args):
    allUsers = []  # List to store all user dictionaries
    
    for user in args:  # Iterate over the passed users
        users = {}  # Create a dictionary for each user
        users[user.username] = user.email  # Add user to the dictionary
        allUsers.append(users)  # Append the dictionary to the list
    
    return allUsers

# Call the function with multiple users
result = AddUser(user, user1, user2)

# Print the result
print(result)


# def AddUser(user):
#     users = {}
#     users[user.username] = user.email

#     allUsers = [] 
#     allUsers.append(users)
#     return allUsers


# print(AddUser(user))

# def addUser(user):
#     users.append(user)
#     return print(users)

# addUser(user)
