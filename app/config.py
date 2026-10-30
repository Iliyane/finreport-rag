from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FinanceReportRAG"
    app_env: str = "development"
    app_debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    vectorstore_provider: str = "faiss"
    vectorstore_path: str = "./data/vectorstore"
    documents_path: str = "./data/documents"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
