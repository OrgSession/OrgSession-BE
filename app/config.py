import os

APP_NAME = "OrgWide Session Demo"
VERSION = "v1"
APP_ENV = os.getenv("APP_ENV", "local")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
