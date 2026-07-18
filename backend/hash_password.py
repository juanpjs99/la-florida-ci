from werkzeug.security import generate_password_hash

password = "Admin123*"

print(generate_password_hash(password))