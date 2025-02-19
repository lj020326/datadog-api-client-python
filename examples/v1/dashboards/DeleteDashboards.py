"""
Delete dashboards returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.model.dashboard_bulk_action_data import DashboardBulkActionData
from datadog_api_client.v1.model.dashboard_bulk_delete_request import DashboardBulkDeleteRequest
from datadog_api_client.v1.model.dashboard_resource_type import DashboardResourceType

# there is a valid "dashboard" in the system
DASHBOARD_ID = environ["DASHBOARD_ID"]

body = DashboardBulkDeleteRequest(
    data=[
        DashboardBulkActionData(
            id=DASHBOARD_ID,
            type=DashboardResourceType.DASHBOARD,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    api_instance.delete_dashboards(body=body)
