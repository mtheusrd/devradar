#app/core/config.py

# Importacoes padrão
# 'os' acessamos o sistema operacional
from os import getenv

# Pydantic e a biblioteca de validação de dados do FastAPI
# 'BaseSettings' classe especial para ler variaveis de ambiente
from pydantic_settings import BaseSettings, SettingsConfigDict

# CLASSE - 'class' define um tipo novo--
# cada atributo da classe vira uma variável de ambiente
class Settings(BaseSettings):
    app_name: str = "DevRadar"
    app_version: str = "0.1.0"
    app_description: str = "Agregador de vagas tech"
    debug: bool = True
    port: int = 8000
    database_url: str = "postgresql://user:password@localhost:5432/devradar"
    redis_url: str =  "redis://localhost:6379/0"
    allowed_hosts: list[str] = ["localhost", "127.0.0.1", "0.0.0.0"]

    # model_config diz ao Pydantic ler o ficheiro .env
    # 'extra = ignore' faz faz ignorar variáveis no .env que não estão na classe
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    secret_key: str = "muda-esta-chave-em-producao"
    access_token_expire_minutes: int = 30
# PADRÃO SINGLETON - criar UMA instância que é importada em todo o projeto
# é como uma variável global

settings = Settings()