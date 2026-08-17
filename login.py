def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login successful"
    else:
        return "Invalid username or password"


print(login("admin", "1234"))