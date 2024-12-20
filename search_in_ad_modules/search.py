from .base import MicrosoftADAction 
from pydantic import BaseModel
from typing import List
from ldap3 import ALL_ATTRIBUTES

class SearchArguments(BaseModel):
    search_filter: str
    basedn: str
    attributes: List[str]| None


class SearchAction(MicrosoftADAction):
    name = "Search"
    description = "Search in your AD"

    def run(self, arguments: SearchArguments) -> str:
        attributes = arguments.attributes or ALL_ATTRIBUTES
        try:
            self.client.search(
                search_base=arguments.basedn, search_filter=arguments.search_filter, attributes=attributes
            )
        except:
            raise Exception(f"Failed to search in this base {arguments.basedn}")
          

        return str(self.client.response)

