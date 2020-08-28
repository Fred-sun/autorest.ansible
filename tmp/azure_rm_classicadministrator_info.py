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
module: azure_rm_classicadministrator_info
version_added: '2.9'
short_description: Get ClassicAdministrator info.
description:
  - Get info of ClassicAdministrator.
options: {}
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: GetConfigurations
      azure_rm_classicadministrator_info: 
        {}
        

'''

RETURN = '''
classic_administrators:
  description: >-
    A list of dict results where the key is the name of the ClassicAdministrator
    and the values are the facts for that ClassicAdministrator.
  returned: always
  type: complex
  contains:
    value:
      description:
        - An array of administrators.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The ID of the administrator.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the administrator.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the administrator.
          returned: always
          type: str
          sample: null
        email_address:
          description:
            - The email address of the administrator.
          returned: always
          type: str
          sample: null
        role:
          description:
            - The role of the administrator.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to use for getting the next set of results.
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
    from azure.mgmt.authorization import AuthorizationManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMClassicAdministratorInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2015-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMClassicAdministratorInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(AuthorizationManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2015-06-01')

        else:
            self.results['classic_administrators'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.classic_administrators.list()
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
    AzureRMClassicAdministratorInfo()


if __name__ == '__main__':
    main()
