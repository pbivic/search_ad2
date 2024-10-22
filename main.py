from search_in_ad_modules.search import SearchAction
from search_in_ad_modules import SearchInAdModule


if __name__ == "__main__":
    module = SearchInAdModule()
    module.register(SearchAction, "search-ad")    
    module.run()
