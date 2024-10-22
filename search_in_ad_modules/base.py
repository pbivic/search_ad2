from functools import cached_property
from ldap3 import Server, Connection

from pydantic import BaseModel, Field
from sekoia_automation.action import Action
from sekoia_automation.module import Module


class MicrosoftADConfiguration(BaseModel):
    servername: str = Field(..., description="Remote machine IP or Name")
    admin_username: str = Field(..., description="Admin username")
    admin_password: str = Field(secret=True, description="Admin password")


class MicrosoftADModule(Module):
    configuration: MicrosoftADConfiguration


class MicrosoftADAction(Action):
    module: MicrosoftADModule

    @cached_property
    def client(self):
        server = Server(
            host=self.module.configuration.servername,
            port=636,
            use_ssl=True,
        )
        conn = Connection(
            server,
            auto_bind=True,
            user=self.module.configuration.admin_username,
            password=self.module.configuration.admin_password,
        )

        return conn