import os
import getpass


def run_setup():
    username = input("Please enter the API username: ")
    password = getpass.getpass("Please enter the API password: ")
    confirm_password = getpass.getpass("Please confirm the API password: ")

    if password != confirm_password:
        print("Error: Passwords do not match. Exiting...")
        return

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(parent_dir)
    secrets_dir = os.path.join(root_dir, "secrets")
    username_file = os.path.join(secrets_dir, "api_username.txt")
    password_file = os.path.join(secrets_dir, "api_password.txt")

    os.makedirs(secrets_dir, exist_ok=True)

    with open(username_file, "w") as f:
        f.write(username)

    with open(password_file, "w") as f:
        f.write(password)

    print(f"Secrets have been created successfully in the '{secrets_dir}' directory.")
    print(f"- {username_file}")
    print(f"- {password_file}")


if __name__ == "__main__":
    run_setup()
