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
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMContainerService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            container_service_name=dict(
                type='str'
            ),
            location=dict(
                type='str',
                disposition='null'
            ),
            orchestrator_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    orchestrator_type=dict(
                        type='sealed-choice',
                        disposition='null',
                        required=true
                    )
                )
            ),
            custom_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    orchestrator=dict(
                        type='str',
                        disposition='null',
                        required=true
                    )
                )
            ),
            service_principal_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    secret=dict(
                        type='str',
                        disposition='null',
                        required=true
                    )
                )
            ),
            master_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    count=dict(
                        type='choice',
                        disposition='null'
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    fqdn=dict(
                        type='str',
                        updatable=False,
                        disposition='null'
                    )
                )
            ),
            agent_pool_profiles=dict(
                type='list',
                disposition='null'
            ),
            windows_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='null',
                        required=true
                    )
                )
            ),
            linux_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='null',
                        required=true
                    ),
                    ssh=dict(
                        type='dict',
                        disposition='null',
                        required=true,
                        options=dict(
                            public_keys=dict(
                                type='list',
                                disposition='null',
                                required=true
                            )
                        )
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='null',
                options=dict(
                    vm_diagnostics=dict(
                        type='dict',
                        disposition='null',
                        required=true,
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='null',
                                required=true
                            ),
                            storage_uri=dict(
                                type='str',
                                updatable=False,
                                disposition='null'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.container_service_name = None
        self.location = None
        self.tags = None
        self.orchestrator_profile = None
        self.custom_profile = None
        self.service_principal_profile = None
        self.master_profile = None
        self.agent_pool_profiles = None
        self.windows_profile = None
        self.linux_profile = None
        self.diagnostics_profile = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainerService, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                      supports_check_mode=True,
                                                      supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            setattr(self, key, kwargs[key])


        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

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
            response = self.mgmt_client.containerservices.create_or_update(resource_group_name=self.resource_group_name,
                                                                           container_service_name=self.container_service_name,
                                                                           location=self.location)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContainerService instance.')
            self.fail('Error creating the ContainerService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.containerservices.delete(resource_group_name=self.resource_group_name,
                                                                 container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContainerService instance.')
            self.fail('Error deleting the ContainerService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.containerservices.get(resource_group_name=self.resource_group_name,
                                                              container_service_name=self.container_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainerService()


if __name__ == '__main__':
    main()
