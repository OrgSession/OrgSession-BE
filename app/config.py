import os

APP_NAME = "OrgWide Session Demo - GitHub Actions"
VERSION = "v2"
APP_ENV = os.getenv("APP_ENV", "local")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
