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
module: azure_rm_usage_info
version_added: '2.9'
short_description: Get Usage info.
description:
  - Get info of Usage.
options:
  location:
    description:
      - The location of the Azure Storage resource.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: UsageList
      azure_rm_usage_info: 
        location: eastus2(stage)
        

'''

RETURN = '''
usages:
  description: >-
    A list of dict results where the key is the name of the Usage and the values
    are the facts for that Usage.
  returned: always
  type: complex
  contains:
    value:
      description:
        - Gets or sets the list of Storage Resource Usages.
      returned: always
      type: list
      sample: null
      contains:
        unit:
          description:
            - Gets the unit of measurement.
          returned: always
          type: sealed-choice
          sample: null
        current_value:
          description:
            - >-
              Gets the current count of the allocated resources in the
              subscription.
          returned: always
          type: integer
          sample: null
        limit:
          description:
            - >-
              Gets the maximum count of the resources that can be allocated in
              the subscription.
          returned: always
          type: integer
          sample: null
        name:
          description:
            - Gets the name of the type of usage.
          returned: always
          type: dict
          sample: null
          contains:
            value:
              description:
                - Gets a string describing the resource name.
              returned: always
              type: str
              sample: null
            localized_value:
              description:
                - Gets a localized string describing the resource name.
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


class AzureRMUsageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            )
        )

        self.location = None

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
        super(AzureRMUsageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.location is not None):
            self.results['usages'] = self.format_item(self.listbylocation())
        return self.results

    def listbylocation(self):
        response = None

        try:
            response = self.mgmt_client.usages.list_by_location(location=self.location)
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
    AzureRMUsageInfo()


if __name__ == '__main__':
    main()
