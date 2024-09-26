from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets

from core.config import settings

security = HTTPBasic()


def verify_basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    username = credentials.username.encode("utf-8")
    password = credentials.password.encode("utf-8")
    correct_username = settings.API_USERNAME.get_secret_value().encode("utf-8")
    correct_password = settings.API_PASSWORD.get_secret_value().encode("utf-8")

    # Compare digest helps to prevent timing attacks
    correct_username = secrets.compare_digest(username, correct_username)
    correct_password = secrets.compare_digest(password, correct_password)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True
