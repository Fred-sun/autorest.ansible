#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}



import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMVirtualMachineExtensionImageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=true
            ),
            publisher_name=dict(
                type='str',
                required=true
            ),
            type=dict(
                type='str'
            ),
            version=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='integer'
            ),
            orderby=dict(
                type='str'
            )
        )

        self.location = None
        self.publisher_name = None
        self.type = None
        self.version = None
        self.filter = None
        self.top = None
        self.orderby = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineExtensionImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.location is not None and
            self.publisher_name is not None and
            self.type is not None and
            self.version is not None):
            self.results['virtualmachineextensionimages'] = self.format_item(self.get())
        elif (self.location is not None and
              self.publisher_name is not None and
              self.type is not None and
              self.filter is not None and
              self.top is not None and
              self.orderby is not None):
            self.results['virtualmachineextensionimages'] = self.format_item(self.listversions())
        elif (self.location is not None and
              self.publisher_name is not None):
            self.results['virtualmachineextensionimages'] = self.format_item(self.listtypes())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url= '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version}'
        self.url = self.url.replace('{location}', self.location)
        self.url = self.url.replace('{publisherName}', self.publisher_name)
        self.url = self.url.replace('{type}', self.type)
        self.url = self.url.replace('{version}', self.version)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listversions(self):
        response = None
        results = {}
        # prepare url
        self.url= '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions'
        self.url = self.url.replace('{location}', self.location)
        self.url = self.url.replace('{publisherName}', self.publisher_name)
        self.url = self.url.replace('{type}', self.type)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listtypes(self):
        response = None
        results = {}
        # prepare url
        self.url= '/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types'
        self.url = self.url.replace('{location}', self.location)
        self.url = self.url.replace('{publisherName}', self.publisher_name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMVirtualMachineExtensionImageInfo()


if __name__ == '__main__':
    main()
