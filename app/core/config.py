from pydantic import field_validator, Field, SecretStr
from pydantic_settings import SettingsConfigDict, BaseSettings
import secrets


class Settings(BaseSettings):
    APP_NAME: str = "Set Game API"
    VERSION: str = "1.0.0"
    ALLOWED_HOSTS: list = ["*"]
    DEBUG: bool = True
    API_USERNAME: SecretStr | None = Field(alias="api_username", default=None)
    API_PASSWORD: SecretStr | None = Field(alias="api_password", default=None)
    model_config = SettingsConfigDict(secrets_dir="/run/secrets")

    @field_validator("API_USERNAME")
    @classmethod
    def validate_username(cls, v):
        if v is None:
            v = SecretStr(secrets.token_urlsafe(8))
            print(f"Generated API username: {v.get_secret_value()}")
        return v

    @field_validator("API_PASSWORD")
    @classmethod
    def validate_password(cls, v):
        if v is None:
            v = SecretStr(secrets.token_urlsafe(8))
            print(f"Generated API password: {v.get_secret_value()}")
        return v


settings = Settings()
