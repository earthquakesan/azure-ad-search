import pytest

from azureadsearch import *


@pytest.mark.asyncio
async def test_azure_cli_creds():
    clients = [create_azure_cli_graph_client(), create_client_id_secret_graph_client()]
    for client in clients:
        user = await get_user("does_not_exist", client)
        assert user is None
        user = await get_user("Ivan Ermilov", client)
        assert user.user_principal_name.split("@")[0] == "ivan.ermilov"
