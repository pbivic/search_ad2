from search_in_ad_modules.base import MicrosoftADModule, MicrosoftADAction
from search_in_ad_modules.search import SearchAction
from unittest.mock import patch
import pytest


def configured_action(action: MicrosoftADAction):
    module = MicrosoftADModule()
    a = action(module)

    # a.module.configuration = {
    #     "servername": "test_servername",
    #     "admin_username": "test_admin_username",
    #     "admin_password": "test_admin_password",
    # }

    a.module.configuration = {
        "servername": "10.1.2.4",
        "admin_username": "administrateur",
        "admin_password": "Shadow123",
    }
    

    return a


@pytest.fixture
def one_user_dn():
    return [["CN=integration_test,CN=Users,DC=lab,DC=test,DC=com", 512]]


@pytest.fixture
def two_users_dn():
    return [
        ["CN=integration_test,CN=Users,DC=lab,DC=test,DC=com", 512],
        ["CN=integration test1,CN=Users,DC=lab,DC=test,DC=com", 514],
    ]


def test_search():
    username = "Mick Lennon"
    search = (
            f"(|(samaccountname={username})(userPrincipalName={username})(mail={username})(givenName={username}))"
        )
    action = configured_action(SearchAction)
    results = action.run({"search_filter": search, "basedn": "CN=Users,DC=lab,DC=test,DC=com"})
    print(results)
    # with patch(
    #     "microsoft_ad.base.MicrosoftADAction.search_userdn_query",
    #     return_value=one_user_dn,
    # ):
    #     with patch("microsoft_ad.base.MicrosoftADAction.client") as mock_client:
    #         mock_client.modify.return_value = response
    #         mock_client.result.get.return_value = "success"

    #         results = action.run({"username": "test_username", "basedn": "cn=test_basedn"})

    #         assert results is None

