import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password_len = random.randint(5, 20)
password = ""
while len(password) < password_len:
    password = password + random.choice(characters)
print("Password:", password)