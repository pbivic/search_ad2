from pydantic import BaseModel, Field


class SearchInAdModuleConfiguration(BaseModel):
    servername: str = Field(..., description="Remote machine IP or Name")
    admin_username: str = Field(..., description="Admin username")
    admin_password: str = Field(secret=True, description="Admin password")

