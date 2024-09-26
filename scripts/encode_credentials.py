import base64
import os


def encode_credentials():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(parent_dir)
    secrets_dir = os.path.join(root_dir, "secrets")

    username_file = os.path.join(secrets_dir, "api_username.txt")
    password_file = os.path.join(secrets_dir, "api_password.txt")

    if not os.path.exists(username_file):
        raise FileNotFoundError(f"Username file not found: {username_file}")
    if not os.path.exists(password_file):
        raise FileNotFoundError(f"Password file not found: {password_file}")

    with open(username_file, "r") as uf:
        username = uf.read().strip()

    with open(password_file, "r") as pf:
        password = pf.read().strip()

    credentials = f"{username}:{password}"

    base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    print(f"Base64 Encoded Credentials: {base64_credentials}")

    return base64_credentials


if __name__ == "__main__":
    encode_credentials()
