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


class AzureRMGalleryApplicationVersionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            subscription_id=dict(
                type='str',
                required=true
            ),
            resource_group_name=dict(
                type='str',
                required=true
            ),
            gallery_name=dict(
                type='str',
                required=true
            ),
            gallery_application_name=dict(
                type='str',
                required=true
            ),
            gallery_application_version_name=dict(
                type='str'
            ),
            expand=dict(
                type='choice'
            )
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGalleryApplicationVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.subscription_id is not None and
            self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_application_name is not None and
            self.gallery_application_version_name is not None and
            self.expand is not None):
            self.results['null'] = self.format_item(self.get())
        elif (self.subscription_id is not None and
              self.resource_group is not None and
              self.gallery_name is not None and
              self.gallery_application_name is not None):
            self.results['null'] = self.format_item(self.listbygalleryapplication())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{subscriptionId}' +
                    '/resourceGroups' +
                    '/{resourceGroupName}' +
                    '/providers' +
                    '/Microsoft.Compute' +
                    '/galleries' +
                    '/{galleryName}' +
                    '/applications' +
                    '/{galleryApplicationName}' +
                    '/versions' +
                    '/{galleryApplicationVersionName}')

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

    def listbygalleryapplication(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{subscriptionId}' +
                    '/resourceGroups' +
                    '/{resourceGroupName}' +
                    '/providers' +
                    '/Microsoft.Compute' +
                    '/galleries' +
                    '/{galleryName}' +
                    '/applications' +
                    '/{galleryApplicationName}' +
                    '/versions')

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
    AzureRMGalleryApplicationVersionInfo()


if __name__ == '__main__':
    main()