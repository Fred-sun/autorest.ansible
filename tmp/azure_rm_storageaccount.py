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
module: azure_rm_storageaccount
version_added: '2.9'
short_description: Manage Azure StorageAccount instance.
description:
  - 'Create, update and delete instance of Azure StorageAccount.'
options:
  resource_group_name:
    description:
      - >-
        The name of the resource group within the user's subscription. The name
        is case insensitive.
    required: true
    type: str
  account_name:
    description:
      - >-
        The name of the storage account within the specified resource group.
        Storage account names must be between 3 and 24 characters in length and
        use numbers and lower-case letters only.
    required: true
    type: str
  kind:
    description:
      - Required. Indicates the type of storage account.
      - >-
        Optional. Indicates the type of storage account. Currently only
        StorageV2 value supported by server.
    type: str
    choices:
      - Storage
      - StorageV2
      - BlobStorage
      - FileStorage
      - BlockBlobStorage
  location:
    description:
      - >-
        Required. Gets or sets the location of the resource. This will be one of
        the supported and registered Azure Geo Regions (e.g. West US, East US,
        Southeast Asia, etc.). The geo region of a resource cannot be changed
        once it is created, but if an identical geo region is specified on
        update, the request will succeed.
    type: str
  identity:
    description:
      - The identity of the resource.
    type: dict
    suboptions:
      principal_id:
        description:
          - The principal ID of resource identity.
        type: str
      tenant_id:
        description:
          - The tenant ID of resource.
        type: str
      type:
        description:
          - The identity type.
        required: true
        type: constant
  custom_domain:
    description:
      - >-
        User domain assigned to the storage account. Name is the CNAME source.
        Only one custom domain is supported per storage account at this time. To
        clear the existing custom domain, use an empty string for the custom
        domain name property.
      - >-
        Custom domain assigned to the storage account by the user. Name is the
        CNAME source. Only one custom domain is supported per storage account at
        this time. To clear the existing custom domain, use an empty string for
        the custom domain name property.
    type: dict
    suboptions:
      name:
        description:
          - >-
            Gets or sets the custom domain name assigned to the storage account.
            Name is the CNAME source.
        required: true
        type: str
      use_sub_domain_name:
        description:
          - >-
            Indicates whether indirect CName validation is enabled. Default
            value is false. This should only be set on updates.
        type: bool
  encryption:
    description:
      - >-
        Not applicable. Azure Storage encryption is enabled for all storage
        accounts and cannot be disabled.
      - >-
        Provides the encryption settings on the account. The default setting is
        unencrypted.
    type: dict
    suboptions:
      services:
        description:
          - List of services which support encryption.
        type: dict
        suboptions:
          blob:
            description:
              - The encryption function of the blob storage service.
            type: dict
            suboptions:
              enabled:
                description:
                  - >-
                    A boolean indicating whether or not the service encrypts the
                    data as it is stored.
                type: bool
              last_enabled_time:
                description:
                  - >-
                    Gets a rough estimate of the date/time when the encryption
                    was last enabled by the user. Only returned when encryption
                    is enabled. There might be some unencrypted blobs which were
                    written after this time, as it is just a rough estimate.
                type: str
              key_type:
                description:
                  - >-
                    Encryption key type to be used for the encryption service.
                    'Account' key type implies that an account-scoped encryption
                    key will be used. 'Service' key type implies that a default
                    service key is used.
                type: str
                choices:
                  - Service
                  - Account
          file:
            description:
              - The encryption function of the file storage service.
            type: dict
            suboptions:
              enabled:
                description:
                  - >-
                    A boolean indicating whether or not the service encrypts the
                    data as it is stored.
                type: bool
              last_enabled_time:
                description:
                  - >-
                    Gets a rough estimate of the date/time when the encryption
                    was last enabled by the user. Only returned when encryption
                    is enabled. There might be some unencrypted blobs which were
                    written after this time, as it is just a rough estimate.
                type: str
              key_type:
                description:
                  - >-
                    Encryption key type to be used for the encryption service.
                    'Account' key type implies that an account-scoped encryption
                    key will be used. 'Service' key type implies that a default
                    service key is used.
                type: str
                choices:
                  - Service
                  - Account
          table:
            description:
              - The encryption function of the table storage service.
            type: dict
            suboptions:
              enabled:
                description:
                  - >-
                    A boolean indicating whether or not the service encrypts the
                    data as it is stored.
                type: bool
              last_enabled_time:
                description:
                  - >-
                    Gets a rough estimate of the date/time when the encryption
                    was last enabled by the user. Only returned when encryption
                    is enabled. There might be some unencrypted blobs which were
                    written after this time, as it is just a rough estimate.
                type: str
              key_type:
                description:
                  - >-
                    Encryption key type to be used for the encryption service.
                    'Account' key type implies that an account-scoped encryption
                    key will be used. 'Service' key type implies that a default
                    service key is used.
                type: str
                choices:
                  - Service
                  - Account
          queue:
            description:
              - The encryption function of the queue storage service.
            type: dict
            suboptions:
              enabled:
                description:
                  - >-
                    A boolean indicating whether or not the service encrypts the
                    data as it is stored.
                type: bool
              last_enabled_time:
                description:
                  - >-
                    Gets a rough estimate of the date/time when the encryption
                    was last enabled by the user. Only returned when encryption
                    is enabled. There might be some unencrypted blobs which were
                    written after this time, as it is just a rough estimate.
                type: str
              key_type:
                description:
                  - >-
                    Encryption key type to be used for the encryption service.
                    'Account' key type implies that an account-scoped encryption
                    key will be used. 'Service' key type implies that a default
                    service key is used.
                type: str
                choices:
                  - Service
                  - Account
      key_source:
        description:
          - >-
            The encryption keySource (provider). Possible values
            (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault
        required: true
        type: str
        choices:
          - Microsoft.Storage
          - Microsoft.Keyvault
      require_infrastructure_encryption:
        description:
          - >-
            A boolean indicating whether or not the service applies a secondary
            layer of encryption with platform managed keys for data at rest.
        type: bool
      key_vault_properties:
        description:
          - Properties provided by key vault.
        type: dict
        suboptions:
          key_name:
            description:
              - The name of KeyVault key.
            type: str
          key_version:
            description:
              - The version of KeyVault key.
            type: str
          key_vault_uri:
            description:
              - The Uri of KeyVault.
            type: str
          current_versioned_key_identifier:
            description:
              - >-
                The object identifier of the current versioned Key Vault Key in
                use.
            type: str
          last_key_rotation_timestamp:
            description:
              - Timestamp of last rotation of the Key Vault Key.
            type: str
  network_rule_set:
    description:
      - Network rule set
    type: dict
    suboptions:
      bypass:
        description:
          - >-
            Specifies whether traffic is bypassed for
            Logging/Metrics/AzureServices. Possible values are any combination
            of Logging|Metrics|AzureServices (For example, "Logging, Metrics"),
            or None to bypass none of those traffics.
        type: str
        choices:
          - None
          - Logging
          - Metrics
          - AzureServices
      virtual_network_rules:
        description:
          - Sets the virtual network rules
        type: list
        suboptions:
          virtual_network_resource_id:
            description:
              - >-
                Resource ID of a subnet, for example:
                /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
            required: true
            type: str
          action:
            description:
              - The action of virtual network rule.
            type: constant
          state:
            description:
              - Gets the state of virtual network rule.
            type: sealed-choice
      ip_rules:
        description:
          - Sets the IP ACL rules
        type: list
        suboptions:
          ip_address_or_range:
            description:
              - >-
                Specifies the IP or IP range in CIDR format. Only IPV4 address
                is allowed.
            required: true
            type: str
          action:
            description:
              - The action of IP ACL rule.
            type: constant
      default_action:
        description:
          - >-
            Specifies the default action of allow or deny when no other rules
            match.
        required: true
        type: sealed-choice
  access_tier:
    description:
      - >-
        Required for storage accounts where kind = BlobStorage. The access tier
        used for billing.
    type: sealed-choice
  azure_files_identity_based_authentication:
    description:
      - Provides the identity based authentication settings for Azure Files.
    type: dict
    suboptions:
      directory_service_options:
        description:
          - Indicates the directory service used.
        required: true
        type: str
        choices:
          - None
          - AADDS
          - AD
      active_directory_properties:
        description:
          - Required if choose AD.
        type: dict
        suboptions:
          domain_name:
            description:
              - >-
                Specifies the primary domain that the AD DNS server is
                authoritative for.
            required: true
            type: str
          net_bios_domain_name:
            description:
              - Specifies the NetBIOS domain name.
            required: true
            type: str
          forest_name:
            description:
              - Specifies the Active Directory forest to get.
            required: true
            type: str
          domain_guid:
            description:
              - Specifies the domain GUID.
            required: true
            type: str
          domain_sid:
            description:
              - Specifies the security identifier (SID).
            required: true
            type: str
          azure_storage_sid:
            description:
              - Specifies the security identifier (SID) for Azure Storage.
            required: true
            type: str
  enable_https_traffic_only:
    description:
      - >-
        Allows https traffic only to storage service if sets to true. The
        default value is true since API version 2019-04-01.
    type: bool
  is_hns_enabled:
    description:
      - Account HierarchicalNamespace enabled if sets to true.
    type: bool
  large_file_shares_state:
    description:
      - >-
        Allow large file shares if sets to Enabled. It cannot be disabled once
        it is enabled.
    type: str
    choices:
      - Disabled
      - Enabled
  routing_preference:
    description:
      - >-
        Maintains information about the network routing choice opted by the user
        for data transfer
    type: dict
    suboptions:
      routing_choice:
        description:
          - >-
            Routing Choice defines the kind of network routing opted by the
            user.
        type: str
        choices:
          - MicrosoftRouting
          - InternetRouting
      publish_microsoft_endpoints:
        description:
          - >-
            A boolean flag which indicates whether microsoft routing storage
            endpoints are to be published
        type: bool
      publish_internet_endpoints:
        description:
          - >-
            A boolean flag which indicates whether internet routing storage
            endpoints are to be published
        type: bool
  allow_blob_public_access:
    description:
      - >-
        Allow or disallow public access to all blobs or containers in the
        storage account. The default interpretation is true for this property.
    type: bool
  minimum_tls_version:
    description:
      - >-
        Set the minimum TLS version to be permitted on requests to storage. The
        default interpretation is TLS 1.0 for this property.
    type: str
    choices:
      - TLS1_0
      - TLS1_1
      - TLS1_2
  name:
    description:
      - >-
        The SKU name. Required for account creation; optional for update. Note
        that in older versions, SKU name was called accountType.
    type: str
    choices:
      - Standard_LRS
      - Standard_GRS
      - Standard_RAGRS
      - Standard_ZRS
      - Premium_LRS
      - Premium_ZRS
      - Standard_GZRS
      - Standard_RAGZRS
  state:
    description:
      - Assert the state of the StorageAccount.
      - >-
        Use C(present) to create or update an StorageAccount and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: StorageAccountCreate
      azure_rm_storageaccount: 
        account_name: sto4445
        resource_group_name: res9101
        kind: Storage
        location: eastus
        properties:
          allow_blob_public_access: false
          encryption:
            key_source: Microsoft.Storage
            require_infrastructure_encryption: false
            services:
              blob:
                enabled: true
                key_type: Account
              file:
                enabled: true
                key_type: Account
          is_hns_enabled: true
          minimum_tls_version: TLS1_2
          routing_preference:
            publish_internet_endpoints: true
            publish_microsoft_endpoints: true
            routing_choice: MicrosoftRouting
        sku:
          name: Standard_GRS
        tags:
          key1: value1
          key2: value2
        

    - name: StorageAccountDelete
      azure_rm_storageaccount: 
        account_name: sto2434
        resource_group_name: res4228
        

    - name: StorageAccountEnableAD
      azure_rm_storageaccount: 
        account_name: sto8596
        resource_group_name: res9407
        properties:
          azure_files_identity_based_authentication:
            active_directory_properties:
              azure_storage_sid: S-1-5-21-2400535526-2334094090-2402026252-0012
              domain_guid: aebfc118-9fa9-4732-a21f-d98e41a77ae1
              domain_name: adtest.com
              domain_sid: S-1-5-21-2400535526-2334094090-2402026252
              forest_name: adtest.com
              net_bios_domain_name: adtest.com
            directory_service_options: AD
        

    - name: StorageAccountEnableCMK
      azure_rm_storageaccount: 
        account_name: sto8596
        resource_group_name: res9407
        properties:
          encryption:
            key_source: Microsoft.Keyvault
            keyvaultproperties:
              keyname: wrappingKey
              keyvaulturi: 'https://myvault8569.vault.azure.net'
              keyversion: ''
            services:
              blob:
                enabled: true
                key_type: Account
              file:
                enabled: true
                key_type: Account
        

    - name: StorageAccountUpdate
      azure_rm_storageaccount: 
        account_name: sto8596
        resource_group_name: res9407
        properties:
          allow_blob_public_access: false
          encryption:
            key_source: Microsoft.Storage
            services:
              blob:
                enabled: true
                key_type: Account
              file:
                enabled: true
                key_type: Account
          minimum_tls_version: TLS1_2
          network_acls:
            default_action: Allow
          routing_preference:
            publish_internet_endpoints: true
            publish_microsoft_endpoints: true
            routing_choice: MicrosoftRouting
        

'''

RETURN = '''
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
          The SKU name. Required for account creation; optional for update. Note
          that in older versions, SKU name was called accountType.
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
      queue, or table object. Note that Standard_ZRS and Premium_LRS accounts
      only return the blob endpoint.
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
      element is not returned if there has never been a failover instance. Only
      available if the accountType is Standard_GRS or Standard_RAGRS.
  returned: always
  type: str
  sample: null
secondary_location:
  description:
    - >-
      Gets the location of the geo-replicated secondary for the storage account.
      Only available if the accountType is Standard_GRS or Standard_RAGRS.
  returned: always
  type: str
  sample: null
status_of_secondary:
  description:
    - >-
      Gets the status indicating whether the secondary location of the storage
      account is available or unavailable. Only available if the SKU name is
      Standard_GRS or Standard_RAGRS.
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
          Gets or sets the custom domain name assigned to the storage account.
          Name is the CNAME source.
      returned: always
      type: str
      sample: null
    use_sub_domain_name:
      description:
        - >-
          Indicates whether indirect CName validation is enabled. Default value
          is false. This should only be set on updates.
      returned: always
      type: bool
      sample: null
secondary_endpoints:
  description:
    - >-
      Gets the URLs that are used to perform a retrieval of a public blob,
      queue, or table object from the secondary location of the storage account.
      Only available if the SKU name is Standard_RAGRS.
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
      Gets the encryption settings on the account. If unspecified, the account
      is unencrypted.
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
                  A boolean indicating whether or not the service encrypts the
                  data as it is stored.
              returned: always
              type: bool
              sample: null
            last_enabled_time:
              description:
                - >-
                  Gets a rough estimate of the date/time when the encryption was
                  last enabled by the user. Only returned when encryption is
                  enabled. There might be some unencrypted blobs which were
                  written after this time, as it is just a rough estimate.
              returned: always
              type: str
              sample: null
            key_type:
              description:
                - >-
                  Encryption key type to be used for the encryption service.
                  'Account' key type implies that an account-scoped encryption
                  key will be used. 'Service' key type implies that a default
                  service key is used.
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
                  A boolean indicating whether or not the service encrypts the
                  data as it is stored.
              returned: always
              type: bool
              sample: null
            last_enabled_time:
              description:
                - >-
                  Gets a rough estimate of the date/time when the encryption was
                  last enabled by the user. Only returned when encryption is
                  enabled. There might be some unencrypted blobs which were
                  written after this time, as it is just a rough estimate.
              returned: always
              type: str
              sample: null
            key_type:
              description:
                - >-
                  Encryption key type to be used for the encryption service.
                  'Account' key type implies that an account-scoped encryption
                  key will be used. 'Service' key type implies that a default
                  service key is used.
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
                  A boolean indicating whether or not the service encrypts the
                  data as it is stored.
              returned: always
              type: bool
              sample: null
            last_enabled_time:
              description:
                - >-
                  Gets a rough estimate of the date/time when the encryption was
                  last enabled by the user. Only returned when encryption is
                  enabled. There might be some unencrypted blobs which were
                  written after this time, as it is just a rough estimate.
              returned: always
              type: str
              sample: null
            key_type:
              description:
                - >-
                  Encryption key type to be used for the encryption service.
                  'Account' key type implies that an account-scoped encryption
                  key will be used. 'Service' key type implies that a default
                  service key is used.
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
                  A boolean indicating whether or not the service encrypts the
                  data as it is stored.
              returned: always
              type: bool
              sample: null
            last_enabled_time:
              description:
                - >-
                  Gets a rough estimate of the date/time when the encryption was
                  last enabled by the user. Only returned when encryption is
                  enabled. There might be some unencrypted blobs which were
                  written after this time, as it is just a rough estimate.
              returned: always
              type: str
              sample: null
            key_type:
              description:
                - >-
                  Encryption key type to be used for the encryption service.
                  'Account' key type implies that an account-scoped encryption
                  key will be used. 'Service' key type implies that a default
                  service key is used.
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
          A boolean indicating whether or not the service applies a secondary
          layer of encryption with platform managed keys for data at rest.
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
              The object identifier of the current versioned Key Vault Key in
              use.
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
      Required for storage accounts where kind = BlobStorage. The access tier
      used for billing.
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
          Logging/Metrics/AzureServices. Possible values are any combination of
          Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or
          None to bypass none of those traffics.
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
              Specifies the IP or IP range in CIDR format. Only IPV4 address is
              allowed.
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
          Bootstrap: Indicates initial synchronization from the primary location
          to the secondary location is in progress.This typically occurs when
          replication is first enabled. - Unavailable: Indicates that the
          secondary location is temporarily unavailable.
      returned: always
      type: str
      sample: null
    last_sync_time:
      description:
        - >-
          All primary writes preceding this UTC date/time value are guaranteed
          to be available for read operations. Primary writes following this
          point in time may or may not be available for reads. Element may be
          default value if value of LastSyncTime is not available, this can
          happen if secondary is offline or we are in bootstrap.
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
      If the failover is in progress, the value will be true, otherwise, it will
      be null.
  returned: always
  type: bool
  sample: null
large_file_shares_state:
  description:
    - >-
      Allow large file shares if sets to Enabled. It cannot be disabled once it
      is enabled.
  returned: always
  type: str
  sample: null
private_endpoint_connections:
  description:
    - >-
      List of private endpoint connection associated with the specified storage
      account
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
          A collection of information about the state of the connection between
          service consumer and provider.
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
              A message indicating if changes on the service provider require
              any updates on the consumer.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the private endpoint connection resource.
      returned: always
      type: str
      sample: null
routing_preference:
  description:
    - >-
      Maintains information about the network routing choice opted by the user
      for data transfer
  returned: always
  type: dict
  sample: null
  contains:
    routing_choice:
      description:
        - Routing Choice defines the kind of network routing opted by the user.
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
          Indicates that blob restore has been completed successfully. - Failed:
          Indicates that blob restore is failed.
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
                - Blob end range. This is exclusive. Empty means account end.
              returned: always
              type: str
              sample: null
allow_blob_public_access:
  description:
    - >-
      Allow or disallow public access to all blobs or containers in the storage
      account. The default interpretation is true for this property.
  returned: always
  type: bool
  sample: null
minimum_tls_version:
  description:
    - >-
      Set the minimum TLS version to be permitted on requests to storage. The
      default interpretation is TLS 1.0 for this property.
  returned: always
  type: str
  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.storage import StorageManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMStorageAccount(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            account_name=dict(
                type='str',
                required=True
            ),
            kind=dict(
                type='str',
                disposition='/kind',
                choices=['Storage',
                         'StorageV2',
                         'BlobStorage',
                         'FileStorage',
                         'BlockBlobStorage']
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    principal_id=dict(
                        type='str',
                        updatable=False,
                        disposition='principal_id'
                    ),
                    tenant_id=dict(
                        type='str',
                        updatable=False,
                        disposition='tenant_id'
                    ),
                    type=dict(
                        type='constant',
                        disposition='type',
                        required=True
                    )
                )
            ),
            custom_domain=dict(
                type='dict',
                disposition='/custom_domain',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    use_sub_domain_name=dict(
                        type='bool',
                        disposition='use_sub_domain_name'
                    )
                )
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    services=dict(
                        type='dict',
                        disposition='services',
                        options=dict(
                            blob=dict(
                                type='dict',
                                disposition='blob',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    ),
                                    last_enabled_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_enabled_time'
                                    ),
                                    key_type=dict(
                                        type='str',
                                        disposition='key_type',
                                        choices=['Service',
                                                 'Account']
                                    )
                                )
                            ),
                            file=dict(
                                type='dict',
                                disposition='file',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    ),
                                    last_enabled_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_enabled_time'
                                    ),
                                    key_type=dict(
                                        type='str',
                                        disposition='key_type',
                                        choices=['Service',
                                                 'Account']
                                    )
                                )
                            ),
                            table=dict(
                                type='dict',
                                disposition='table',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    ),
                                    last_enabled_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_enabled_time'
                                    ),
                                    key_type=dict(
                                        type='str',
                                        disposition='key_type',
                                        choices=['Service',
                                                 'Account']
                                    )
                                )
                            ),
                            queue=dict(
                                type='dict',
                                disposition='queue',
                                options=dict(
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    ),
                                    last_enabled_time=dict(
                                        type='str',
                                        updatable=False,
                                        disposition='last_enabled_time'
                                    ),
                                    key_type=dict(
                                        type='str',
                                        disposition='key_type',
                                        choices=['Service',
                                                 'Account']
                                    )
                                )
                            )
                        )
                    ),
                    key_source=dict(
                        type='str',
                        disposition='key_source',
                        choices=['Microsoft.Storage',
                                 'Microsoft.Keyvault'],
                        required=True
                    ),
                    require_infrastructure_encryption=dict(
                        type='bool',
                        disposition='require_infrastructure_encryption'
                    ),
                    key_vault_properties=dict(
                        type='dict',
                        disposition='key_vault_properties',
                        options=dict(
                            key_name=dict(
                                type='str',
                                disposition='key_name'
                            ),
                            key_version=dict(
                                type='str',
                                disposition='key_version'
                            ),
                            key_vault_uri=dict(
                                type='str',
                                disposition='key_vault_uri'
                            ),
                            current_versioned_key_identifier=dict(
                                type='str',
                                updatable=False,
                                disposition='current_versioned_key_identifier'
                            ),
                            last_key_rotation_timestamp=dict(
                                type='str',
                                updatable=False,
                                disposition='last_key_rotation_timestamp'
                            )
                        )
                    )
                )
            ),
            network_rule_set=dict(
                type='dict',
                disposition='/network_rule_set',
                options=dict(
                    bypass=dict(
                        type='str',
                        disposition='bypass',
                        choices=['None',
                                 'Logging',
                                 'Metrics',
                                 'AzureServices']
                    ),
                    virtual_network_rules=dict(
                        type='list',
                        disposition='virtual_network_rules',
                        elements='dict',
                        options=dict(
                            virtual_network_resource_id=dict(
                                type='str',
                                disposition='virtual_network_resource_id',
                                required=True
                            ),
                            action=dict(
                                type='constant',
                                disposition='action'
                            ),
                            state=dict(
                                type='sealed-choice',
                                disposition='state'
                            )
                        )
                    ),
                    ip_rules=dict(
                        type='list',
                        disposition='ip_rules',
                        elements='dict',
                        options=dict(
                            ip_address_or_range=dict(
                                type='str',
                                disposition='ip_address_or_range',
                                required=True
                            ),
                            action=dict(
                                type='constant',
                                disposition='action'
                            )
                        )
                    ),
                    default_action=dict(
                        type='sealed-choice',
                        disposition='default_action',
                        required=True
                    )
                )
            ),
            access_tier=dict(
                type='sealed-choice',
                disposition='/access_tier'
            ),
            azure_files_identity_based_authentication=dict(
                type='dict',
                disposition='/azure_files_identity_based_authentication',
                options=dict(
                    directory_service_options=dict(
                        type='str',
                        disposition='directory_service_options',
                        choices=['None',
                                 'AADDS',
                                 'AD'],
                        required=True
                    ),
                    active_directory_properties=dict(
                        type='dict',
                        disposition='active_directory_properties',
                        options=dict(
                            domain_name=dict(
                                type='str',
                                disposition='domain_name',
                                required=True
                            ),
                            net_bios_domain_name=dict(
                                type='str',
                                disposition='net_bios_domain_name',
                                required=True
                            ),
                            forest_name=dict(
                                type='str',
                                disposition='forest_name',
                                required=True
                            ),
                            domain_guid=dict(
                                type='str',
                                disposition='domain_guid',
                                required=True
                            ),
                            domain_sid=dict(
                                type='str',
                                disposition='domain_sid',
                                required=True
                            ),
                            azure_storage_sid=dict(
                                type='str',
                                disposition='azure_storage_sid',
                                required=True
                            )
                        )
                    )
                )
            ),
            enable_https_traffic_only=dict(
                type='bool',
                disposition='/enable_https_traffic_only'
            ),
            is_hns_enabled=dict(
                type='bool',
                disposition='/is_hns_enabled'
            ),
            large_file_shares_state=dict(
                type='str',
                disposition='/large_file_shares_state',
                choices=['Disabled',
                         'Enabled']
            ),
            routing_preference=dict(
                type='dict',
                disposition='/routing_preference',
                options=dict(
                    routing_choice=dict(
                        type='str',
                        disposition='routing_choice',
                        choices=['MicrosoftRouting',
                                 'InternetRouting']
                    ),
                    publish_microsoft_endpoints=dict(
                        type='bool',
                        disposition='publish_microsoft_endpoints'
                    ),
                    publish_internet_endpoints=dict(
                        type='bool',
                        disposition='publish_internet_endpoints'
                    )
                )
            ),
            allow_blob_public_access=dict(
                type='bool',
                disposition='/allow_blob_public_access'
            ),
            minimum_tls_version=dict(
                type='str',
                disposition='/minimum_tls_version',
                choices=['TLS1_0',
                         'TLS1_1',
                         'TLS1_2']
            ),
            name=dict(
                type='str',
                disposition='/name',
                choices=['Standard_LRS',
                         'Standard_GRS',
                         'Standard_RAGRS',
                         'Standard_ZRS',
                         'Premium_LRS',
                         'Premium_ZRS',
                         'Standard_GZRS',
                         'Standard_RAGZRS']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMStorageAccount, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                    supports_check_mode=True,
                                                    supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.storage_accounts.create(resource_group_name=self.resource_group_name,
                                                                    account_name=self.account_name,
                                                                    parameters=self.body)
            else:
                response = self.mgmt_client.storage_accounts.update(resource_group_name=self.resource_group_name,
                                                                    account_name=self.account_name,
                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the StorageAccount instance.')
            self.fail('Error creating the StorageAccount instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.storage_accounts.delete(resource_group_name=self.resource_group_name,
                                                                account_name=self.account_name)
        except CloudError as e:
            self.log('Error attempting to delete the StorageAccount instance.')
            self.fail('Error deleting the StorageAccount instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.storage_accounts.get()
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMStorageAccount()


if __name__ == '__main__':
    main()
