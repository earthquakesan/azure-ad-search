import asyncio
import os

from azure.identity import AzureCliCredential, ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder


async def get_user(user_name: str, client: GraphServiceClient) -> dict:
    # The query used here is the same when searching for users in Azure AD via web console
    query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
        search=[
            f'("displayName:{user_name}" OR "mail:{user_name}" OR "userPrincipalName:{user_name}" OR "givenName:{user_name}" OR "surName:{user_name}" OR "otherMails:{user_name}")'
        ],
    )
    request_configuration = (
        UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
            query_parameters=query_params, headers={"ConsistencyLevel": "eventual"}
        )
    )

    response = await client.users.get(request_configuration=request_configuration)
    if response.value:
        user = response.value[0]
        print(
            f"Found user for {user_name} in the Azure AD with user principal name {user.user_principal_name} and display name {user.display_name}"
        )
        return user
    else:
        print(f"{user_name} user in the Azure AD not found")
        return None


def create_graph_client(credentials) -> GraphServiceClient:
    scopes = ["https://graph.microsoft.com/.default"]
    client = GraphServiceClient(credentials=credentials, scopes=scopes)
    return client


def create_azure_cli_graph_client() -> GraphServiceClient:
    # Create a credential object. Used to authenticate requests
    credentials = AzureCliCredential()
    return create_graph_client(credentials)


def create_client_id_secret_graph_client() -> GraphServiceClient:
    tenant_id = os.environ.get("TENANT_ID")
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    credentials = ClientSecretCredential(
        tenant_id=tenant_id, client_id=client_id, client_secret=client_secret
    )
    return create_graph_client(credentials)
