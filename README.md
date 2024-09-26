# Instructions

1. **Setup**:
   - Run the command `python scripts/setup.py` and enter the credentials for the api. The credentials can be anything you choose.

2. **Running the Application**:
   - Ensure the port 80 is free in your environment
   - Run the command `docker compose up -d`

3. **Making a request**:
   - Use this example to call the "sets" endpoint: https://documenter.getpostman.com/view/11227058/2sAXqwa13w
   - If you need to use cURL, you can get the encoded credentials by running `python scripts/encode_credentials.py`
   - Alternatively, you can open http://localhost/docs to explore the builtin API documentation.
