from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "E-KYC Verification"

    DATABASE_URL: str = "sqlite:///./kyc.db"

    SECRET_KEY: str = "super-secret-key"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    UPLOAD_DOC_DIR: str = "uploads/documents"

    UPLOAD_SELFIE_DIR: str = "uploads/selfies"

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()