#!/usr/bin/env bash

# 00000003-0000-0000-c000-000000000000 is Azure Graph API id
# to view all permissions see: 
# az ad sp show --id 00000003-0000-0000-c000-000000000000
# df021288-bdef-4463-88db-98f22de89214 is User.Read.All permissions
# see docs: https://learn.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http
cat <<EOF > manifest.json
[{
    "resourceAppId": "00000003-0000-0000-c000-000000000000",
    "resourceAccess": [
        {
            "id": "df021288-bdef-4463-88db-98f22de89214",
            "type": "Role"
        }
    ]
}]
EOF

id=$(az ad app create \
  --display-name azure-ad-search \
  --required-resource-accesses @manifest.json | jq .id)

az ad app permission admin-consent --id ${id}
az ad app credential reset --id ${id}

rm manifest.json
