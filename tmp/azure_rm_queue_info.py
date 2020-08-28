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
module: azure_rm_queue_info
version_added: '2.9'
short_description: Get Queue info.
description:
  - Get info of Queue.
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
  queue_name:
    description:
      - >-
        A queue name must be unique within a storage account and must be between
        3 and 63 characters.The name must comprise of lowercase alphanumeric and
        dash(-) characters only, it should begin and end with an alphanumeric
        character and it cannot have two consecutive dash(-) characters.
    type: str
  maxpagesize:
    description:
      - >-
        Optional, a maximum number of queues that should be included in a list
        queue response
    type: str
  filter:
    description:
      - >-
        Optional, When specified, only the queues with a name starting with the
        given filter will be listed.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: QueueOperationGet
      azure_rm_queue_info: 
        account_name: sto328
        queue_name: queue6185
        resource_group_name: res3376
        

    - name: QueueOperationList
      azure_rm_queue_info: 
        account_name: sto328
        resource_group_name: res9290
        

'''

RETURN = '''
queue:
  description: >-
    A list of dict results where the key is the name of the Queue and the values
    are the facts for that Queue.
  returned: always
  type: complex
  contains:
    id:
      description:
        - >-
          Fully qualified resource Id for the resource. Ex -
          /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the resource
      returned: always
      type: str
      sample: null
    type:
      description:
        - >-
          The type of the resource. Ex- Microsoft.Compute/virtualMachines or
          Microsoft.Storage/storageAccounts.
      returned: always
      type: str
      sample: null
    metadata:
      description:
        - A name-value pair that represents queue metadata.
      returned: always
      type: dictionary
      sample: null
    approximate_message_count:
      description:
        - >-
          Integer indicating an approximate number of messages in the queue.
          This number is not lower than the actual number of messages in the
          queue, but could be higher.
      returned: always
      type: integer
      sample: null
    value:
      description:
        - List of queues returned.
      returned: always
      type: list
      sample: null
      contains:
        metadata:
          description:
            - A name-value pair that represents queue metadata.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - Request URL that can be used to list next page of queues
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


class AzureRMQueueInfo(AzureRMModuleBase):
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
            queue_name=dict(
                type='str'
            ),
            maxpagesize=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.account_name = None
        self.queue_name = None
        self.maxpagesize = None
        self.filter = None

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
        super(AzureRMQueueInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(StorageManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-06-01')

        if (self.resource_group_name is not None and
            self.account_name is not None and
            self.queue_name is not None):
            self.results['queue'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.account_name is not None):
            self.results['queue'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.queue.get(resource_group_name=self.resource_group_name,
                                                  account_name=self.account_name,
                                                  queue_name=self.queue_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.queue.list(resource_group_name=self.resource_group_name,
                                                   account_name=self.account_name,
                                                   maxpagesize=self.maxpagesize,
                                                   filter=self.filter)
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
    AzureRMQueueInfo()


if __name__ == '__main__':
    main()
