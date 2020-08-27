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
module: azure_rm_resourcesku_info
version_added: '2.9'
short_description: Get ResourceSku info.
description:
  - Get info of ResourceSku.
options:
  filter:
    description:
      - >-
        The filter to apply on the operation. Only **location** filter is
        supported currently.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Lists all available Resource SKUs
      azure_rm_resourcesku_info: 
        {}
        

    - name: Lists all available Resource SKUs for the specified region
      azure_rm_resourcesku_info: 
        {}
        

'''

RETURN = '''
resource_skus:
  description: >-
    A list of dict results where the key is the name of the ResourceSku and the
    values are the facts for that ResourceSku.
  returned: always
  type: complex
  contains:
    value:
      description:
        - The list of skus available for the subscription.
      returned: always
      type: list
      sample: null
      contains:
        resource_type:
          description:
            - The type of resource the SKU applies to.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of SKU.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - >-
              Specifies the tier of virtual machines in a scale set.:code:`<br
              />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
              **Standard**\ :code:`<br />`:code:`<br />` **Basic**
          returned: always
          type: str
          sample: null
        size:
          description:
            - The Size of the SKU.
          returned: always
          type: str
          sample: null
        family:
          description:
            - The Family of this particular SKU.
          returned: always
          type: str
          sample: null
        kind:
          description:
            - The Kind of resources that are supported in this SKU.
          returned: always
          type: str
          sample: null
        capacity:
          description:
            - Specifies the number of virtual machines in the scale set.
          returned: always
          type: dict
          sample: null
          contains:
            minimum:
              description:
                - The minimum capacity.
              returned: always
              type: integer
              sample: null
            maximum:
              description:
                - The maximum capacity that can be set.
              returned: always
              type: integer
              sample: null
            default:
              description:
                - The default capacity.
              returned: always
              type: integer
              sample: null
            scale_type:
              description:
                - The scale type applicable to the sku.
              returned: always
              type: sealed-choice
              sample: null
        locations:
          description:
            - The set of locations that the SKU is available.
          returned: always
          type: list
          sample: null
        location_info:
          description:
            - >-
              A list of locations and availability zones in those locations
              where the SKU is available.
          returned: always
          type: list
          sample: null
          contains:
            location:
              description:
                - Location of the SKU
              returned: always
              type: str
              sample: null
            zones:
              description:
                - List of availability zones where the SKU is supported.
              returned: always
              type: list
              sample: null
            zone_details:
              description:
                - Details of capabilities available to a SKU in specific zones.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - >-
                      The set of zones that the SKU is available in with the
                      specified capabilities.
                  returned: always
                  type: list
                  sample: null
                capabilities:
                  description:
                    - >-
                      A list of capabilities that are available for the SKU in
                      the specified list of zones.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - An invariant to describe the feature.
                      returned: always
                      type: str
                      sample: null
                    value:
                      description:
                        - An invariant if the feature is measured by quantity.
                      returned: always
                      type: str
                      sample: null
        api_versions:
          description:
            - The api versions that support this SKU.
          returned: always
          type: list
          sample: null
        costs:
          description:
            - Metadata for retrieving price info.
          returned: always
          type: list
          sample: null
          contains:
            meter_id:
              description:
                - Used for querying price from commerce.
              returned: always
              type: str
              sample: null
            quantity:
              description:
                - The multiplier is needed to extend the base metered cost.
              returned: always
              type: integer
              sample: null
            extended_unit:
              description:
                - An invariant to show the extended unit.
              returned: always
              type: str
              sample: null
        capabilities:
          description:
            - A name value pair to describe the capability.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - An invariant to describe the feature.
              returned: always
              type: str
              sample: null
            value:
              description:
                - An invariant if the feature is measured by quantity.
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
                - The type of restrictions.
              returned: always
              type: sealed-choice
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
            restriction_info:
              description:
                - >-
                  The information about the restriction where the SKU cannot be
                  used.
              returned: always
              type: dict
              sample: null
              contains:
                locations:
                  description:
                    - Locations where the SKU is restricted
                  returned: always
                  type: list
                  sample: null
                zones:
                  description:
                    - List of availability zones where the SKU is restricted.
                  returned: always
                  type: list
                  sample: null
            reason_code:
              description:
                - The reason for restriction.
              returned: always
              type: sealed-choice
              sample: null
    next_link:
      description:
        - >-
          The URI to fetch the next page of Resource Skus. Call ListNext() with
          this URI to fetch the next page of Resource Skus
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
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMResourceSkuInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            filter=dict(
                type='str',
                required=True
            )
        )

        self.filter = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMResourceSkuInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-04-01')

        else:
            self.results['resource_skus'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.resource_skus.list(filter=self.filter)
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
    AzureRMResourceSkuInfo()


if __name__ == '__main__':
    main()
