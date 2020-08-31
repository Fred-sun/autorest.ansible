#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_storageaccount_info
version_added: '2.9'
short_description: Get StorageAccount info.
description:
  - Get info of StorageAccount.
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    type: str
  account_name:
    description:
      - >-
        The name of the storage account within the specified resource group.
        Storage account names must be between 3 and 24 characters in length and
        use numbers and lower-case letters only.
    type: str
  expand:
    description:
      - >-
        May be used to expand the properties within account's properties. By
        default, data is not included when fetching properties. Currently we
        only support geoReplicationStats and blobRestoreStatus.
    type: sealed-choice
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountGetProperties
      azure_rm_storageaccount_info: 
        account_name: sto8596
        resource_group_name: res9407
        

    - name: StorageAccountGetPropertiesCMKEnabled
      azure_rm_storageaccount_info: 
        account_name: sto8596
        resource_group_name: res9407
        

    - name: StorageAccountList
      azure_rm_storageaccount_info: 
        {}
        

    - name: StorageAccountListByResourceGroup
      azure_rm_storageaccount_info: 
        resource_group_name: res6117
        

'''

RETURN = '''
storage_accounts:
  description: >-
    A list of dict results where the key is the name of the StorageAccount and
    the values are the facts for that StorageAccount.
  returned: always
  type: complex
  contains:
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    location:
      description:
        - The geo-location where the resource lives
      returned: always
      type: str
      sample: null
    sku:
      description:
        - Gets the SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              The SKU name. Required for account creation; optional for update.
              Note that in older versions, SKU name was called accountType.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - The SKU tier. This is based on the SKU name.
          returned: always
          type: sealed-choice
          sample: null
    kind:
      description:
        - Gets the Kind.
      returned: always
      type: str
      sample: null
    identity:
      description:
        - The identity of the resource.
      returned: always
      type: dict
      sample: null
      contains:
        principal_id:
          description:
            - The principal ID of resource identity.
          returned: always
          type: str
          sample: null
        tenant_id:
          description:
            - The tenant ID of resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The identity type.
          returned: always
          type: constant
          sample: null
    provisioning_state:
      description:
        - >-
          Gets the status of the storage account at the time the operation was
          called.
      returned: always
      type: sealed-choice
      sample: null
    primary_endpoints:
      description:
        - >-
          Gets the URLs that are used to perform a retrieval of a public blob,
          queue, or table object. Note that Standard_ZRS and Premium_LRS
          accounts only return the blob endpoint.
      returned: always
      type: dict
      sample: null
      contains:
        blob:
          description:
            - Gets the blob endpoint.
          returned: always
          type: str
          sample: null
        queue:
          description:
            - Gets the queue endpoint.
          returned: always
          type: str
          sample: null
        table:
          description:
            - Gets the table endpoint.
          returned: always
          type: str
          sample: null
        file:
          description:
            - Gets the file endpoint.
          returned: always
          type: str
          sample: null
        web:
          description:
            - Gets the web endpoint.
          returned: always
          type: str
          sample: null
        dfs:
          description:
            - Gets the dfs endpoint.
          returned: always
          type: str
          sample: null
        microsoft_endpoints:
          description:
            - Gets the microsoft routing storage endpoints.
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            queue:
              description:
                - Gets the queue endpoint.
              returned: always
              type: str
              sample: null
            table:
              description:
                - Gets the table endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
        internet_endpoints:
          description:
            - Gets the internet routing storage endpoints
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
    primary_location:
      description:
        - Gets the location of the primary data center for the storage account.
      returned: always
      type: str
      sample: null
    status_of_primary:
      description:
        - >-
          Gets the status indicating whether the primary location of the storage
          account is available or unavailable.
      returned: always
      type: sealed-choice
      sample: null
    last_geo_failover_time:
      description:
        - >-
          Gets the timestamp of the most recent instance of a failover to the
          secondary location. Only the most recent timestamp is retained. This
          element is not returned if there has never been a failover instance.
          Only available if the accountType is Standard_GRS or Standard_RAGRS.
      returned: always
      type: str
      sample: null
    secondary_location:
      description:
        - >-
          Gets the location of the geo-replicated secondary for the storage
          account. Only available if the accountType is Standard_GRS or
          Standard_RAGRS.
      returned: always
      type: str
      sample: null
    status_of_secondary:
      description:
        - >-
          Gets the status indicating whether the secondary location of the
          storage account is available or unavailable. Only available if the SKU
          name is Standard_GRS or Standard_RAGRS.
      returned: always
      type: sealed-choice
      sample: null
    creation_time:
      description:
        - Gets the creation date and time of the storage account in UTC.
      returned: always
      type: str
      sample: null
    custom_domain:
      description:
        - Gets the custom domain the user assigned to this storage account.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              Gets or sets the custom domain name assigned to the storage
              account. Name is the CNAME source.
          returned: always
          type: str
          sample: null
        use_sub_domain_name:
          description:
            - >-
              Indicates whether indirect CName validation is enabled. Default
              value is false. This should only be set on updates.
          returned: always
          type: bool
          sample: null
    secondary_endpoints:
      description:
        - >-
          Gets the URLs that are used to perform a retrieval of a public blob,
          queue, or table object from the secondary location of the storage
          account. Only available if the SKU name is Standard_RAGRS.
      returned: always
      type: dict
      sample: null
      contains:
        blob:
          description:
            - Gets the blob endpoint.
          returned: always
          type: str
          sample: null
        queue:
          description:
            - Gets the queue endpoint.
          returned: always
          type: str
          sample: null
        table:
          description:
            - Gets the table endpoint.
          returned: always
          type: str
          sample: null
        file:
          description:
            - Gets the file endpoint.
          returned: always
          type: str
          sample: null
        web:
          description:
            - Gets the web endpoint.
          returned: always
          type: str
          sample: null
        dfs:
          description:
            - Gets the dfs endpoint.
          returned: always
          type: str
          sample: null
        microsoft_endpoints:
          description:
            - Gets the microsoft routing storage endpoints.
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            queue:
              description:
                - Gets the queue endpoint.
              returned: always
              type: str
              sample: null
            table:
              description:
                - Gets the table endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
        internet_endpoints:
          description:
            - Gets the internet routing storage endpoints
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
    encryption:
      description:
        - >-
          Gets the encryption settings on the account. If unspecified, the
          account is unencrypted.
      returned: always
      type: dict
      sample: null
      contains:
        services:
          description:
            - List of services which support encryption.
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - The encryption function of the blob storage service.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - >-
                      A boolean indicating whether or not the service encrypts
                      the data as it is stored.
                  returned: always
                  type: bool
                  sample: null
                last_enabled_time:
                  description:
                    - >-
                      Gets a rough estimate of the date/time when the encryption
                      was last enabled by the user. Only returned when
                      encryption is enabled. There might be some unencrypted
                      blobs which were written after this time, as it is just a
                      rough estimate.
                  returned: always
                  type: str
                  sample: null
                key_type:
                  description:
                    - >-
                      Encryption key type to be used for the encryption service.
                      'Account' key type implies that an account-scoped
                      encryption key will be used. 'Service' key type implies
                      that a default service key is used.
                  returned: always
                  type: str
                  sample: null
            file:
              description:
                - The encryption function of the file storage service.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - >-
                      A boolean indicating whether or not the service encrypts
                      the data as it is stored.
                  returned: always
                  type: bool
                  sample: null
                last_enabled_time:
                  description:
                    - >-
                      Gets a rough estimate of the date/time when the encryption
                      was last enabled by the user. Only returned when
                      encryption is enabled. There might be some unencrypted
                      blobs which were written after this time, as it is just a
                      rough estimate.
                  returned: always
                  type: str
                  sample: null
                key_type:
                  description:
                    - >-
                      Encryption key type to be used for the encryption service.
                      'Account' key type implies that an account-scoped
                      encryption key will be used. 'Service' key type implies
                      that a default service key is used.
                  returned: always
                  type: str
                  sample: null
            table:
              description:
                - The encryption function of the table storage service.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - >-
                      A boolean indicating whether or not the service encrypts
                      the data as it is stored.
                  returned: always
                  type: bool
                  sample: null
                last_enabled_time:
                  description:
                    - >-
                      Gets a rough estimate of the date/time when the encryption
                      was last enabled by the user. Only returned when
                      encryption is enabled. There might be some unencrypted
                      blobs which were written after this time, as it is just a
                      rough estimate.
                  returned: always
                  type: str
                  sample: null
                key_type:
                  description:
                    - >-
                      Encryption key type to be used for the encryption service.
                      'Account' key type implies that an account-scoped
                      encryption key will be used. 'Service' key type implies
                      that a default service key is used.
                  returned: always
                  type: str
                  sample: null
            queue:
              description:
                - The encryption function of the queue storage service.
              returned: always
              type: dict
              sample: null
              contains:
                enabled:
                  description:
                    - >-
                      A boolean indicating whether or not the service encrypts
                      the data as it is stored.
                  returned: always
                  type: bool
                  sample: null
                last_enabled_time:
                  description:
                    - >-
                      Gets a rough estimate of the date/time when the encryption
                      was last enabled by the user. Only returned when
                      encryption is enabled. There might be some unencrypted
                      blobs which were written after this time, as it is just a
                      rough estimate.
                  returned: always
                  type: str
                  sample: null
                key_type:
                  description:
                    - >-
                      Encryption key type to be used for the encryption service.
                      'Account' key type implies that an account-scoped
                      encryption key will be used. 'Service' key type implies
                      that a default service key is used.
                  returned: always
                  type: str
                  sample: null
        key_source:
          description:
            - >-
              The encryption keySource (provider). Possible values
              (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault
          returned: always
          type: str
          sample: null
        require_infrastructure_encryption:
          description:
            - >-
              A boolean indicating whether or not the service applies a
              secondary layer of encryption with platform managed keys for data
              at rest.
          returned: always
          type: bool
          sample: null
        key_vault_properties:
          description:
            - Properties provided by key vault.
          returned: always
          type: dict
          sample: null
          contains:
            key_name:
              description:
                - The name of KeyVault key.
              returned: always
              type: str
              sample: null
            key_version:
              description:
                - The version of KeyVault key.
              returned: always
              type: str
              sample: null
            key_vault_uri:
              description:
                - The Uri of KeyVault.
              returned: always
              type: str
              sample: null
            current_versioned_key_identifier:
              description:
                - >-
                  The object identifier of the current versioned Key Vault Key
                  in use.
              returned: always
              type: str
              sample: null
            last_key_rotation_timestamp:
              description:
                - Timestamp of last rotation of the Key Vault Key.
              returned: always
              type: str
              sample: null
    access_tier:
      description:
        - >-
          Required for storage accounts where kind = BlobStorage. The access
          tier used for billing.
      returned: always
      type: sealed-choice
      sample: null
    azure_files_identity_based_authentication:
      description:
        - Provides the identity based authentication settings for Azure Files.
      returned: always
      type: dict
      sample: null
      contains:
        directory_service_options:
          description:
            - Indicates the directory service used.
          returned: always
          type: str
          sample: null
        active_directory_properties:
          description:
            - Required if choose AD.
          returned: always
          type: dict
          sample: null
          contains:
            domain_name:
              description:
                - >-
                  Specifies the primary domain that the AD DNS server is
                  authoritative for.
              returned: always
              type: str
              sample: null
            net_bios_domain_name:
              description:
                - Specifies the NetBIOS domain name.
              returned: always
              type: str
              sample: null
            forest_name:
              description:
                - Specifies the Active Directory forest to get.
              returned: always
              type: str
              sample: null
            domain_guid:
              description:
                - Specifies the domain GUID.
              returned: always
              type: str
              sample: null
            domain_sid:
              description:
                - Specifies the security identifier (SID).
              returned: always
              type: str
              sample: null
            azure_storage_sid:
              description:
                - Specifies the security identifier (SID) for Azure Storage.
              returned: always
              type: str
              sample: null
    enable_https_traffic_only:
      description:
        - Allows https traffic only to storage service if sets to true.
      returned: always
      type: bool
      sample: null
    network_rule_set:
      description:
        - Network rule set
      returned: always
      type: dict
      sample: null
      contains:
        bypass:
          description:
            - >-
              Specifies whether traffic is bypassed for
              Logging/Metrics/AzureServices. Possible values are any combination
              of Logging|Metrics|AzureServices (For example, "Logging,
              Metrics"), or None to bypass none of those traffics.
          returned: always
          type: str
          sample: null
        virtual_network_rules:
          description:
            - Sets the virtual network rules
          returned: always
          type: list
          sample: null
          contains:
            virtual_network_resource_id:
              description:
                - >-
                  Resource ID of a subnet, for example:
                  /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
              returned: always
              type: str
              sample: null
            action:
              description:
                - The action of virtual network rule.
              returned: always
              type: constant
              sample: null
            state:
              description:
                - Gets the state of virtual network rule.
              returned: always
              type: sealed-choice
              sample: null
        ip_rules:
          description:
            - Sets the IP ACL rules
          returned: always
          type: list
          sample: null
          contains:
            ip_address_or_range:
              description:
                - >-
                  Specifies the IP or IP range in CIDR format. Only IPV4 address
                  is allowed.
              returned: always
              type: str
              sample: null
            action:
              description:
                - The action of IP ACL rule.
              returned: always
              type: constant
              sample: null
        default_action:
          description:
            - >-
              Specifies the default action of allow or deny when no other rules
              match.
          returned: always
          type: sealed-choice
          sample: null
    is_hns_enabled:
      description:
        - Account HierarchicalNamespace enabled if sets to true.
      returned: always
      type: bool
      sample: null
    geo_replication_stats:
      description:
        - Geo Replication Stats
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              The status of the secondary location. Possible values are: - Live:
              Indicates that the secondary location is active and operational. -
              Bootstrap: Indicates initial synchronization from the primary
              location to the secondary location is in progress.This typically
              occurs when replication is first enabled. - Unavailable: Indicates
              that the secondary location is temporarily unavailable.
          returned: always
          type: str
          sample: null
        last_sync_time:
          description:
            - >-
              All primary writes preceding this UTC date/time value are
              guaranteed to be available for read operations. Primary writes
              following this point in time may or may not be available for
              reads. Element may be default value if value of LastSyncTime is
              not available, this can happen if secondary is offline or we are
              in bootstrap.
          returned: always
          type: str
          sample: null
        can_failover:
          description:
            - >-
              A boolean flag which indicates whether or not account failover is
              supported for the account.
          returned: always
          type: bool
          sample: null
    failover_in_progress:
      description:
        - >-
          If the failover is in progress, the value will be true, otherwise, it
          will be null.
      returned: always
      type: bool
      sample: null
    large_file_shares_state:
      description:
        - >-
          Allow large file shares if sets to Enabled. It cannot be disabled once
          it is enabled.
      returned: always
      type: str
      sample: null
    private_endpoint_connections:
      description:
        - >-
          List of private endpoint connection associated with the specified
          storage account
      returned: always
      type: list
      sample: null
      contains:
        private_endpoint:
          description:
            - The resource of private end point.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The ARM identifier for Private Endpoint
              returned: always
              type: str
              sample: null
        private_link_service_connection_state:
          description:
            - >-
              A collection of information about the state of the connection
              between service consumer and provider.
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  Indicates whether the connection has been
                  Approved/Rejected/Removed by the owner of the service.
              returned: always
              type: str
              sample: null
            description:
              description:
                - The reason for approval/rejection of the connection.
              returned: always
              type: str
              sample: null
            action_required:
              description:
                - >-
                  A message indicating if changes on the service provider
                  require any updates on the consumer.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - >-
              The provisioning state of the private endpoint connection
              resource.
          returned: always
          type: str
          sample: null
    routing_preference:
      description:
        - >-
          Maintains information about the network routing choice opted by the
          user for data transfer
      returned: always
      type: dict
      sample: null
      contains:
        routing_choice:
          description:
            - >-
              Routing Choice defines the kind of network routing opted by the
              user.
          returned: always
          type: str
          sample: null
        publish_microsoft_endpoints:
          description:
            - >-
              A boolean flag which indicates whether microsoft routing storage
              endpoints are to be published
          returned: always
          type: bool
          sample: null
        publish_internet_endpoints:
          description:
            - >-
              A boolean flag which indicates whether internet routing storage
              endpoints are to be published
          returned: always
          type: bool
          sample: null
    blob_restore_status:
      description:
        - Blob restore status
      returned: always
      type: dict
      sample: null
      contains:
        status:
          description:
            - >-
              The status of blob restore progress. Possible values are: -
              InProgress: Indicates that blob restore is ongoing. - Complete:
              Indicates that blob restore has been completed successfully. -
              Failed: Indicates that blob restore is failed.
          returned: always
          type: str
          sample: null
        failure_reason:
          description:
            - Failure reason when blob restore is failed.
          returned: always
          type: str
          sample: null
        restore_id:
          description:
            - Id for tracking blob restore request.
          returned: always
          type: str
          sample: null
        parameters:
          description:
            - Blob restore request parameters.
          returned: always
          type: dict
          sample: null
          contains:
            time_to_restore:
              description:
                - Restore blob to the specified time.
              returned: always
              type: str
              sample: null
            blob_ranges:
              description:
                - Blob ranges to restore.
              returned: always
              type: list
              sample: null
              contains:
                start_range:
                  description:
                    - >-
                      Blob start range. This is inclusive. Empty means account
                      start.
                  returned: always
                  type: str
                  sample: null
                end_range:
                  description:
                    - >-
                      Blob end range. This is exclusive. Empty means account
                      end.
                  returned: always
                  type: str
                  sample: null
    allow_blob_public_access:
      description:
        - >-
          Allow or disallow public access to all blobs or containers in the
          storage account. The default interpretation is true for this property.
      returned: always
      type: bool
      sample: null
    minimum_tls_version:
      description:
        - >-
          Set the minimum TLS version to be permitted on requests to storage.
          The default interpretation is TLS 1.0 for this property.
      returned: always
      type: str
      sample: null
    value:
      description:
        - Gets the list of storage accounts and their properties.
      returned: always
      type: list
      sample: null
      contains:
        sku:
          description:
            - Gets the SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  The SKU name. Required for account creation; optional for
                  update. Note that in older versions, SKU name was called
                  accountType.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - The SKU tier. This is based on the SKU name.
              returned: always
              type: sealed-choice
              sample: null
        kind:
          description:
            - Gets the Kind.
          returned: always
          type: str
          sample: null
        identity:
          description:
            - The identity of the resource.
          returned: always
          type: dict
          sample: null
          contains:
            principal_id:
              description:
                - The principal ID of resource identity.
              returned: always
              type: str
              sample: null
            tenant_id:
              description:
                - The tenant ID of resource.
              returned: always
              type: str
              sample: null
            type:
              description:
                - The identity type.
              returned: always
              type: constant
              sample: null
        provisioning_state:
          description:
            - >-
              Gets the status of the storage account at the time the operation
              was called.
          returned: always
          type: sealed-choice
          sample: null
        primary_endpoints:
          description:
            - >-
              Gets the URLs that are used to perform a retrieval of a public
              blob, queue, or table object. Note that Standard_ZRS and
              Premium_LRS accounts only return the blob endpoint.
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            queue:
              description:
                - Gets the queue endpoint.
              returned: always
              type: str
              sample: null
            table:
              description:
                - Gets the table endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
            microsoft_endpoints:
              description:
                - Gets the microsoft routing storage endpoints.
              returned: always
              type: dict
              sample: null
              contains:
                blob:
                  description:
                    - Gets the blob endpoint.
                  returned: always
                  type: str
                  sample: null
                queue:
                  description:
                    - Gets the queue endpoint.
                  returned: always
                  type: str
                  sample: null
                table:
                  description:
                    - Gets the table endpoint.
                  returned: always
                  type: str
                  sample: null
                file:
                  description:
                    - Gets the file endpoint.
                  returned: always
                  type: str
                  sample: null
                web:
                  description:
                    - Gets the web endpoint.
                  returned: always
                  type: str
                  sample: null
                dfs:
                  description:
                    - Gets the dfs endpoint.
                  returned: always
                  type: str
                  sample: null
            internet_endpoints:
              description:
                - Gets the internet routing storage endpoints
              returned: always
              type: dict
              sample: null
              contains:
                blob:
                  description:
                    - Gets the blob endpoint.
                  returned: always
                  type: str
                  sample: null
                file:
                  description:
                    - Gets the file endpoint.
                  returned: always
                  type: str
                  sample: null
                web:
                  description:
                    - Gets the web endpoint.
                  returned: always
                  type: str
                  sample: null
                dfs:
                  description:
                    - Gets the dfs endpoint.
                  returned: always
                  type: str
                  sample: null
        primary_location:
          description:
            - >-
              Gets the location of the primary data center for the storage
              account.
          returned: always
          type: str
          sample: null
        status_of_primary:
          description:
            - >-
              Gets the status indicating whether the primary location of the
              storage account is available or unavailable.
          returned: always
          type: sealed-choice
          sample: null
        last_geo_failover_time:
          description:
            - >-
              Gets the timestamp of the most recent instance of a failover to
              the secondary location. Only the most recent timestamp is
              retained. This element is not returned if there has never been a
              failover instance. Only available if the accountType is
              Standard_GRS or Standard_RAGRS.
          returned: always
          type: str
          sample: null
        secondary_location:
          description:
            - >-
              Gets the location of the geo-replicated secondary for the storage
              account. Only available if the accountType is Standard_GRS or
              Standard_RAGRS.
          returned: always
          type: str
          sample: null
        status_of_secondary:
          description:
            - >-
              Gets the status indicating whether the secondary location of the
              storage account is available or unavailable. Only available if the
              SKU name is Standard_GRS or Standard_RAGRS.
          returned: always
          type: sealed-choice
          sample: null
        creation_time:
          description:
            - Gets the creation date and time of the storage account in UTC.
          returned: always
          type: str
          sample: null
        custom_domain:
          description:
            - Gets the custom domain the user assigned to this storage account.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  Gets or sets the custom domain name assigned to the storage
                  account. Name is the CNAME source.
              returned: always
              type: str
              sample: null
            use_sub_domain_name:
              description:
                - >-
                  Indicates whether indirect CName validation is enabled.
                  Default value is false. This should only be set on updates.
              returned: always
              type: bool
              sample: null
        secondary_endpoints:
          description:
            - >-
              Gets the URLs that are used to perform a retrieval of a public
              blob, queue, or table object from the secondary location of the
              storage account. Only available if the SKU name is Standard_RAGRS.
          returned: always
          type: dict
          sample: null
          contains:
            blob:
              description:
                - Gets the blob endpoint.
              returned: always
              type: str
              sample: null
            queue:
              description:
                - Gets the queue endpoint.
              returned: always
              type: str
              sample: null
            table:
              description:
                - Gets the table endpoint.
              returned: always
              type: str
              sample: null
            file:
              description:
                - Gets the file endpoint.
              returned: always
              type: str
              sample: null
            web:
              description:
                - Gets the web endpoint.
              returned: always
              type: str
              sample: null
            dfs:
              description:
                - Gets the dfs endpoint.
              returned: always
              type: str
              sample: null
            microsoft_endpoints:
              description:
                - Gets the microsoft routing storage endpoints.
              returned: always
              type: dict
              sample: null
              contains:
                blob:
                  description:
                    - Gets the blob endpoint.
                  returned: always
                  type: str
                  sample: null
                queue:
                  description:
                    - Gets the queue endpoint.
                  returned: always
                  type: str
                  sample: null
                table:
                  description:
                    - Gets the table endpoint.
                  returned: always
                  type: str
                  sample: null
                file:
                  description:
                    - Gets the file endpoint.
                  returned: always
                  type: str
                  sample: null
                web:
                  description:
                    - Gets the web endpoint.
                  returned: always
                  type: str
                  sample: null
                dfs:
                  description:
                    - Gets the dfs endpoint.
                  returned: always
                  type: str
                  sample: null
            internet_endpoints:
              description:
                - Gets the internet routing storage endpoints
              returned: always
              type: dict
              sample: null
              contains:
                blob:
                  description:
                    - Gets the blob endpoint.
                  returned: always
                  type: str
                  sample: null
                file:
                  description:
                    - Gets the file endpoint.
                  returned: always
                  type: str
                  sample: null
                web:
                  description:
                    - Gets the web endpoint.
                  returned: always
                  type: str
                  sample: null
                dfs:
                  description:
                    - Gets the dfs endpoint.
                  returned: always
                  type: str
                  sample: null
        encryption:
          description:
            - >-
              Gets the encryption settings on the account. If unspecified, the
              account is unencrypted.
          returned: always
          type: dict
          sample: null
          contains:
            services:
              description:
                - List of services which support encryption.
              returned: always
              type: dict
              sample: null
              contains:
                blob:
                  description:
                    - The encryption function of the blob storage service.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    enabled:
                      description:
                        - >-
                          A boolean indicating whether or not the service
                          encrypts the data as it is stored.
                      returned: always
                      type: bool
                      sample: null
                    last_enabled_time:
                      description:
                        - >-
                          Gets a rough estimate of the date/time when the
                          encryption was last enabled by the user. Only returned
                          when encryption is enabled. There might be some
                          unencrypted blobs which were written after this time,
                          as it is just a rough estimate.
                      returned: always
                      type: str
                      sample: null
                    key_type:
                      description:
                        - >-
                          Encryption key type to be used for the encryption
                          service. 'Account' key type implies that an
                          account-scoped encryption key will be used. 'Service'
                          key type implies that a default service key is used.
                      returned: always
                      type: str
                      sample: null
                file:
                  description:
                    - The encryption function of the file storage service.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    enabled:
                      description:
                        - >-
                          A boolean indicating whether or not the service
                          encrypts the data as it is stored.
                      returned: always
                      type: bool
                      sample: null
                    last_enabled_time:
                      description:
                        - >-
                          Gets a rough estimate of the date/time when the
                          encryption was last enabled by the user. Only returned
                          when encryption is enabled. There might be some
                          unencrypted blobs which were written after this time,
                          as it is just a rough estimate.
                      returned: always
                      type: str
                      sample: null
                    key_type:
                      description:
                        - >-
                          Encryption key type to be used for the encryption
                          service. 'Account' key type implies that an
                          account-scoped encryption key will be used. 'Service'
                          key type implies that a default service key is used.
                      returned: always
                      type: str
                      sample: null
                table:
                  description:
                    - The encryption function of the table storage service.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    enabled:
                      description:
                        - >-
                          A boolean indicating whether or not the service
                          encrypts the data as it is stored.
                      returned: always
                      type: bool
                      sample: null
                    last_enabled_time:
                      description:
                        - >-
                          Gets a rough estimate of the date/time when the
                          encryption was last enabled by the user. Only returned
                          when encryption is enabled. There might be some
                          unencrypted blobs which were written after this time,
                          as it is just a rough estimate.
                      returned: always
                      type: str
                      sample: null
                    key_type:
                      description:
                        - >-
                          Encryption key type to be used for the encryption
                          service. 'Account' key type implies that an
                          account-scoped encryption key will be used. 'Service'
                          key type implies that a default service key is used.
                      returned: always
                      type: str
                      sample: null
                queue:
                  description:
                    - The encryption function of the queue storage service.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    enabled:
                      description:
                        - >-
                          A boolean indicating whether or not the service
                          encrypts the data as it is stored.
                      returned: always
                      type: bool
                      sample: null
                    last_enabled_time:
                      description:
                        - >-
                          Gets a rough estimate of the date/time when the
                          encryption was last enabled by the user. Only returned
                          when encryption is enabled. There might be some
                          unencrypted blobs which were written after this time,
                          as it is just a rough estimate.
                      returned: always
                      type: str
                      sample: null
                    key_type:
                      description:
                        - >-
                          Encryption key type to be used for the encryption
                          service. 'Account' key type implies that an
                          account-scoped encryption key will be used. 'Service'
                          key type implies that a default service key is used.
                      returned: always
                      type: str
                      sample: null
            key_source:
              description:
                - >-
                  The encryption keySource (provider). Possible values
                  (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault
              returned: always
              type: str
              sample: null
            require_infrastructure_encryption:
              description:
                - >-
                  A boolean indicating whether or not the service applies a
                  secondary layer of encryption with platform managed keys for
                  data at rest.
              returned: always
              type: bool
              sample: null
            key_vault_properties:
              description:
                - Properties provided by key vault.
              returned: always
              type: dict
              sample: null
              contains:
                key_name:
                  description:
                    - The name of KeyVault key.
                  returned: always
                  type: str
                  sample: null
                key_version:
                  description:
                    - The version of KeyVault key.
                  returned: always
                  type: str
                  sample: null
                key_vault_uri:
                  description:
                    - The Uri of KeyVault.
                  returned: always
                  type: str
                  sample: null
                current_versioned_key_identifier:
                  description:
                    - >-
                      The object identifier of the current versioned Key Vault
                      Key in use.
                  returned: always
                  type: str
                  sample: null
                last_key_rotation_timestamp:
                  description:
                    - Timestamp of last rotation of the Key Vault Key.
                  returned: always
                  type: str
                  sample: null
        access_tier:
          description:
            - >-
              Required for storage accounts where kind = BlobStorage. The access
              tier used for billing.
          returned: always
          type: sealed-choice
          sample: null
        azure_files_identity_based_authentication:
          description:
            - >-
              Provides the identity based authentication settings for Azure
              Files.
          returned: always
          type: dict
          sample: null
          contains:
            directory_service_options:
              description:
                - Indicates the directory service used.
              returned: always
              type: str
              sample: null
            active_directory_properties:
              description:
                - Required if choose AD.
              returned: always
              type: dict
              sample: null
              contains:
                domain_name:
                  description:
                    - >-
                      Specifies the primary domain that the AD DNS server is
                      authoritative for.
                  returned: always
                  type: str
                  sample: null
                net_bios_domain_name:
                  description:
                    - Specifies the NetBIOS domain name.
                  returned: always
                  type: str
                  sample: null
                forest_name:
                  description:
                    - Specifies the Active Directory forest to get.
                  returned: always
                  type: str
                  sample: null
                domain_guid:
                  description:
                    - Specifies the domain GUID.
                  returned: always
                  type: str
                  sample: null
                domain_sid:
                  description:
                    - Specifies the security identifier (SID).
                  returned: always
                  type: str
                  sample: null
                azure_storage_sid:
                  description:
                    - Specifies the security identifier (SID) for Azure Storage.
                  returned: always
                  type: str
                  sample: null
        enable_https_traffic_only:
          description:
            - Allows https traffic only to storage service if sets to true.
          returned: always
          type: bool
          sample: null
        network_rule_set:
          description:
            - Network rule set
          returned: always
          type: dict
          sample: null
          contains:
            bypass:
              description:
                - >-
                  Specifies whether traffic is bypassed for
                  Logging/Metrics/AzureServices. Possible values are any
                  combination of Logging|Metrics|AzureServices (For example,
                  "Logging, Metrics"), or None to bypass none of those traffics.
              returned: always
              type: str
              sample: null
            virtual_network_rules:
              description:
                - Sets the virtual network rules
              returned: always
              type: list
              sample: null
              contains:
                virtual_network_resource_id:
                  description:
                    - >-
                      Resource ID of a subnet, for example:
                      /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
                  returned: always
                  type: str
                  sample: null
                action:
                  description:
                    - The action of virtual network rule.
                  returned: always
                  type: constant
                  sample: null
                state:
                  description:
                    - Gets the state of virtual network rule.
                  returned: always
                  type: sealed-choice
                  sample: null
            ip_rules:
              description:
                - Sets the IP ACL rules
              returned: always
              type: list
              sample: null
              contains:
                ip_address_or_range:
                  description:
                    - >-
                      Specifies the IP or IP range in CIDR format. Only IPV4
                      address is allowed.
                  returned: always
                  type: str
                  sample: null
                action:
                  description:
                    - The action of IP ACL rule.
                  returned: always
                  type: constant
                  sample: null
            default_action:
              description:
                - >-
                  Specifies the default action of allow or deny when no other
                  rules match.
              returned: always
              type: sealed-choice
              sample: null
        is_hns_enabled:
          description:
            - Account HierarchicalNamespace enabled if sets to true.
          returned: always
          type: bool
          sample: null
        geo_replication_stats:
          description:
            - Geo Replication Stats
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  The status of the secondary location. Possible values are: -
                  Live: Indicates that the secondary location is active and
                  operational. - Bootstrap: Indicates initial synchronization
                  from the primary location to the secondary location is in
                  progress.This typically occurs when replication is first
                  enabled. - Unavailable: Indicates that the secondary location
                  is temporarily unavailable.
              returned: always
              type: str
              sample: null
            last_sync_time:
              description:
                - >-
                  All primary writes preceding this UTC date/time value are
                  guaranteed to be available for read operations. Primary writes
                  following this point in time may or may not be available for
                  reads. Element may be default value if value of LastSyncTime
                  is not available, this can happen if secondary is offline or
                  we are in bootstrap.
              returned: always
              type: str
              sample: null
            can_failover:
              description:
                - >-
                  A boolean flag which indicates whether or not account failover
                  is supported for the account.
              returned: always
              type: bool
              sample: null
        failover_in_progress:
          description:
            - >-
              If the failover is in progress, the value will be true, otherwise,
              it will be null.
          returned: always
          type: bool
          sample: null
        large_file_shares_state:
          description:
            - >-
              Allow large file shares if sets to Enabled. It cannot be disabled
              once it is enabled.
          returned: always
          type: str
          sample: null
        private_endpoint_connections:
          description:
            - >-
              List of private endpoint connection associated with the specified
              storage account
          returned: always
          type: list
          sample: null
          contains:
            private_endpoint:
              description:
                - The resource of private end point.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - The ARM identifier for Private Endpoint
                  returned: always
                  type: str
                  sample: null
            private_link_service_connection_state:
              description:
                - >-
                  A collection of information about the state of the connection
                  between service consumer and provider.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - >-
                      Indicates whether the connection has been
                      Approved/Rejected/Removed by the owner of the service.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - The reason for approval/rejection of the connection.
                  returned: always
                  type: str
                  sample: null
                action_required:
                  description:
                    - >-
                      A message indicating if changes on the service provider
                      require any updates on the consumer.
                  returned: always
                  type: str
                  sample: null
            provisioning_state:
              description:
                - >-
                  The provisioning state of the private endpoint connection
                  resource.
              returned: always
              type: str
              sample: null
        routing_preference:
          description:
            - >-
              Maintains information about the network routing choice opted by
              the user for data transfer
          returned: always
          type: dict
          sample: null
          contains:
            routing_choice:
              description:
                - >-
                  Routing Choice defines the kind of network routing opted by
                  the user.
              returned: always
              type: str
              sample: null
            publish_microsoft_endpoints:
              description:
                - >-
                  A boolean flag which indicates whether microsoft routing
                  storage endpoints are to be published
              returned: always
              type: bool
              sample: null
            publish_internet_endpoints:
              description:
                - >-
                  A boolean flag which indicates whether internet routing
                  storage endpoints are to be published
              returned: always
              type: bool
              sample: null
        blob_restore_status:
          description:
            - Blob restore status
          returned: always
          type: dict
          sample: null
          contains:
            status:
              description:
                - >-
                  The status of blob restore progress. Possible values are: -
                  InProgress: Indicates that blob restore is ongoing. -
                  Complete: Indicates that blob restore has been completed
                  successfully. - Failed: Indicates that blob restore is failed.
              returned: always
              type: str
              sample: null
            failure_reason:
              description:
                - Failure reason when blob restore is failed.
              returned: always
              type: str
              sample: null
            restore_id:
              description:
                - Id for tracking blob restore request.
              returned: always
              type: str
              sample: null
            parameters:
              description:
                - Blob restore request parameters.
              returned: always
              type: dict
              sample: null
              contains:
                time_to_restore:
                  description:
                    - Restore blob to the specified time.
                  returned: always
                  type: str
                  sample: null
                blob_ranges:
                  description:
                    - Blob ranges to restore.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    start_range:
                      description:
                        - >-
                          Blob start range. This is inclusive. Empty means
                          account start.
                      returned: always
                      type: str
                      sample: null
                    end_range:
                      description:
                        - >-
                          Blob end range. This is exclusive. Empty means account
                          end.
                      returned: always
                      type: str
                      sample: null
        allow_blob_public_access:
          description:
            - >-
              Allow or disallow public access to all blobs or containers in the
              storage account. The default interpretation is true for this
              property.
          returned: always
          type: bool
          sample: null
        minimum_tls_version:
          description:
            - >-
              Set the minimum TLS version to be permitted on requests to
              storage. The default interpretation is TLS 1.0 for this property.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          Request URL that can be used to query next page of storage accounts.
          Returned when total number of requested storage accounts exceed
          maximum page size.
      returned: always
      type: str
      sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMStorageAccountInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            account_name=dict(
                type='str'
            ),
            expand=dict(
                type='sealed-choice'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMStorageAccountInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None):
            self.results['storage_accounts'] = self.format_item(self.getproperty())
        elif (self.resource_group_name is not None):
            self.results['storage_accounts'] = self.format_item(self.listbyresourcegroup())
        else:
            self.results['storage_accounts'] = self.format_item(self.list())
        return self.results

    def getproperty(self):
        response = None

        try:
            response = self.mgmt_client.storage_accounts.get_property(resource_group_name=self.resource_group_name,
                                                                      account_name=self.account_name,
                                                                      expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def listbyresourcegroup(self):
        response = None

        try:
            response = self.mgmt_client.storage_accounts.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.storage_accounts.list()
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
               result.append(tmp.as_dict())
            return result


def main():
    AzureRMStorageAccountInfo()


if __name__ == '__main__':
    main()
