from sekoia_automation.module import Module
from search_in_ad_modules.models import SearchInAdModuleConfiguration


class SearchInAdModule(Module):
    configuration: SearchInAdModuleConfiguration
