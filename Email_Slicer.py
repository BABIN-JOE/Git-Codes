# Get the email address from the user
email = input("Enter an email address: ")

# Split the email address into username and domain
username, domain = email.split("@")

# Print the results
print(f"Username: {username}")
print(f"Domain: {domain}")
