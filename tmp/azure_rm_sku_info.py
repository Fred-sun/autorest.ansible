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
module: azure_rm_sku_info
version_added: '2.9'
short_description: Get Sku info.
description:
  - Get info of Sku.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: SkuList
      azure_rm_sku_info: 
        {}
        

'''

RETURN = '''
skus:
  description: >-
    A list of dict results where the key is the name of the Sku and the values
    are the facts for that Sku.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Get the list result of storage SKUs and their properties.
      returned: always
      type: list
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
        resource_type:
          description:
            - 'The type of the resource, usually it is ''storageAccounts''.'
          returned: always
          type: str
          sample: null
        kind:
          description:
            - Indicates the type of storage account.
          returned: always
          type: str
          sample: null
        locations:
          description:
            - >-
              The set of locations that the SKU is available. This will be
              supported and registered Azure Geo Regions (e.g. West US, East US,
              Southeast Asia, etc.).
          returned: always
          type: list
          sample: null
        capabilities:
          description:
            - >-
              The capability information in the specified SKU, including file
              encryption, network ACLs, change notification, etc.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of capability, The capability information in the
                  specified SKU, including file encryption, network ACLs, change
                  notification, etc.
              returned: always
              type: str
              sample: null
            value:
              description:
                - >-
                  A string value to indicate states of given capability.
                  Possibly 'true' or 'false'.
              returned: always
              type: str
              sample: null
        restrictions:
          description:
            - >-
              The restrictions because of which SKU cannot be used. This is
              empty if there are no restrictions.
          returned: always
          type: list
          sample: null
          contains:
            type:
              description:
                - >-
                  The type of restrictions. As of now only possible value for
                  this is location.
              returned: always
              type: str
              sample: null
            values:
              description:
                - >-
                  The value of restrictions. If the restriction type is set to
                  location. This would be different locations where the SKU is
                  restricted.
              returned: always
              type: list
              sample: null
            reason_code:
              description:
                - >-
                  The reason for the restriction. As of now this can be
                  "QuotaId" or "NotAvailableForSubscription". Quota Id is set
                  when the SKU has requiredQuotas parameter as the subscription
                  does not belong to that quota. The
                  "NotAvailableForSubscription" is related to capacity at DC.
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


class AzureRMSkuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


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
        super(AzureRMSkuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        else:
            self.results['skus'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.skus.list()
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
    AzureRMSkuInfo()


if __name__ == '__main__':
    main()
