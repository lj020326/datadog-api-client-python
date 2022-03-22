"""
Update a user returns "User updated" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi
from datadog_api_client.v1.model.access_role import AccessRole
from datadog_api_client.v1.model.user import User

body = User(
    access_role=AccessRole("st"),
    disabled=False,
    email="test@datadoghq.com",
    handle="test@datadoghq.com",
    icon="/path/to/matching/gravatar/icon",
    name="test user",
    verified=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_user(user_handle="test@datadoghq.com", body=body)

    print(response)
