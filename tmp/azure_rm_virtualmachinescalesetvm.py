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
module: azure_rm_virtualmachinescalesetvm
version_added: '2.9'
short_description: Manage Azure VirtualMachineScaleSetVM instance.
description:
  - 'Create, update and delete instance of Azure VirtualMachineScaleSetVM.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  vm_scale_set_name:
    description:
      - The name of the VM scale set.
    type: str
  instance_id:
    description:
      - The instance ID of the virtual machine.
    type: str
  temp_disk:
    description:
      - >-
        Specifies whether to reimage temp disk. Default value: false. Note: This
        temp disk reimage parameter is only supported for VM/VMSS with Ephemeral
        OS disk.
    type: bool
  location:
    description:
      - Resource location
    type: str
  plan:
    description:
      - >-
        Specifies information about the marketplace image used to create the
        virtual machine. This element is only used for marketplace images.
        Before you can use a marketplace image from an API, you must enable the
        image for programmatic use.  In the Azure portal, find the marketplace
        image that you want to use and then click **Want to deploy
        programmatically, Get Started ->**. Enter any required information and
        then click **Save**.
    type: dict
    suboptions:
      name:
        description:
          - The plan ID.
        type: str
      publisher:
        description:
          - The publisher ID.
        type: str
      product:
        description:
          - >-
            Specifies the product of the image from the marketplace. This is the
            same value as Offer under the imageReference element.
        type: str
      promotion_code:
        description:
          - The promotion code.
        type: str
  hardware_profile:
    description:
      - Specifies the hardware settings for the virtual machine.
    type: dict
    suboptions:
      vm_size:
        description:
          - >-
            Specifies the size of the virtual machine. For more information
            about virtual machine sizes, see `Sizes for virtual machines
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            :code:`<br>`:code:`<br>` The available VM sizes depend on region and
            availability set. For a list of available sizes use these APIs: 
            :code:`<br>`:code:`<br>` `List all available virtual machine sizes
            in an availability set
            <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
            :code:`<br>`:code:`<br>` `List all available virtual machine sizes
            in a region
            <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
            :code:`<br>`:code:`<br>` `List all available virtual machine sizes
            for resizing
            <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
        type: choice
  storage_profile:
    description:
      - Specifies the storage settings for the virtual machine disks.
    type: dict
    suboptions:
      image_reference:
        description:
          - >-
            Specifies information about the image to use. You can specify
            information about platform images, marketplace images, or virtual
            machine images. This element is required when you want to use a
            platform image, marketplace image, or virtual machine image, but is
            not used in other creation operations.
        type: dict
        suboptions:
          publisher:
            description:
              - The image publisher.
            type: str
          offer:
            description:
              - >-
                Specifies the offer of the platform image or marketplace image
                used to create the virtual machine.
            type: str
          sku:
            description:
              - The image SKU.
            type: str
          version:
            description:
              - >-
                Specifies the version of the platform image or marketplace image
                used to create the virtual machine. The allowed formats are
                Major.Minor.Build or 'latest'. Major, Minor, and Build are
                decimal numbers. Specify 'latest' to use the latest version of
                an image available at deploy time. Even if you use 'latest', the
                VM image will not automatically update after deploy time even if
                a new version becomes available.
            type: str
          exact_version:
            description:
              - >-
                Specifies in decimal numbers, the version of platform image or
                marketplace image used to create the virtual machine. This
                readonly field differs from 'version', only if the value
                specified in 'version' field is 'latest'.
            type: str
      os_disk:
        description:
          - >-
            Specifies information about the operating system disk used by the
            virtual machine. :code:`<br>`:code:`<br>` For more information about
            disks, see `About disks and VHDs for Azure virtual machines
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
        type: dict
        suboptions:
          os_type:
            description:
              - >-
                This property allows you to specify the type of the OS that is
                included in the disk if creating a VM from user-image or a
                specialized VHD. :code:`<br>`:code:`<br>` Possible values are:
                :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                **Linux**
            type: sealed-choice
          encryption_settings:
            description:
              - >-
                Specifies the encryption settings for the OS Disk.
                :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
            type: dict
            suboptions:
              disk_encryption_key:
                description:
                  - >-
                    Specifies the location of the disk encryption key, which is
                    a Key Vault Secret.
                type: dict
                suboptions:
                  secret_url:
                    description:
                      - The URL referencing a secret in a Key Vault.
                    required: true
                    type: str
                  source_vault:
                    description:
                      - The relative URL of the Key Vault containing the secret.
                    required: true
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
              key_encryption_key:
                description:
                  - >-
                    Specifies the location of the key encryption key in Key
                    Vault.
                type: dict
                suboptions:
                  key_url:
                    description:
                      - The URL referencing a key encryption key in Key Vault.
                    required: true
                    type: str
                  source_vault:
                    description:
                      - The relative URL of the Key Vault containing the key.
                    required: true
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
              enabled:
                description:
                  - >-
                    Specifies whether disk encryption should be enabled on the
                    virtual machine.
                type: bool
          name:
            description:
              - The disk name.
            type: str
          vhd:
            description:
              - The virtual hard disk.
            type: dict
            suboptions:
              uri:
                description:
                  - Specifies the virtual hard disk's uri.
                type: str
          image:
            description:
              - >-
                The source user image virtual hard disk. The virtual hard disk
                will be copied before being attached to the virtual machine. If
                SourceImage is provided, the destination virtual hard drive must
                not exist.
            type: dict
            suboptions:
              uri:
                description:
                  - Specifies the virtual hard disk's uri.
                type: str
          caching:
            description:
              - >-
                Specifies the caching requirements. :code:`<br>`:code:`<br>`
                Possible values are: :code:`<br>`:code:`<br>` **None**
                :code:`<br>`:code:`<br>` **ReadOnly** :code:`<br>`:code:`<br>`
                **ReadWrite** :code:`<br>`:code:`<br>` Default: **None** for
                Standard storage. **ReadOnly** for Premium storage.
            type: sealed-choice
          write_accelerator_enabled:
            description:
              - >-
                Specifies whether writeAccelerator should be enabled or disabled
                on the disk.
            type: bool
          diff_disk_settings:
            description:
              - >-
                Specifies the ephemeral Disk Settings for the operating system
                disk used by the virtual machine.
            type: dict
            suboptions:
              option:
                description:
                  - >-
                    Specifies the ephemeral disk settings for operating system
                    disk.
                type: choice
              placement:
                description:
                  - >-
                    Specifies the ephemeral disk placement for operating system
                    disk.:code:`<br>`:code:`<br>` Possible values are:
                    :code:`<br>`:code:`<br>` **CacheDisk**
                    :code:`<br>`:code:`<br>` **ResourceDisk**
                    :code:`<br>`:code:`<br>` Default: **CacheDisk** if one is
                    configured for the VM size otherwise **ResourceDisk** is
                    used.:code:`<br>`:code:`<br>` Refer to VM size documentation
                    for Windows VM at
                    https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                    and Linux VM at
                    https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                    to check which VM sizes exposes a cache disk.
                type: choice
          create_option:
            description:
              - >-
                Specifies how the virtual machine should be
                created.:code:`<br>`:code:`<br>` Possible values
                are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is
                used when you are using a specialized disk to create the virtual
                machine.:code:`<br>`:code:`<br>` **FromImage** \u2013 This value
                is used when you are using an image to create the virtual
                machine. If you are using a platform image, you also use the
                imageReference element described above. If you are using a
                marketplace image, you  also use the plan element previously
                described.
            required: true
            type: choice
          disk_size_gb:
            description:
              - >-
                Specifies the size of an empty data disk in gigabytes. This
                element can be used to overwrite the size of the disk in a
                virtual machine image. :code:`<br>`:code:`<br>` This value
                cannot be larger than 1023 GB
            type: integer
          managed_disk:
            description:
              - The managed disk parameters.
            type: dict
            suboptions:
              storage_account_type:
                description:
                  - >-
                    Specifies the storage account type for the managed disk.
                    NOTE: UltraSSD_LRS can only be used with data disks, it
                    cannot be used with OS Disk.
                type: choice
              disk_encryption_set:
                description:
                  - >-
                    Specifies the customer managed disk encryption set resource
                    id for the managed disk.
                type: dict
                suboptions:
                  id:
                    description:
                      - Resource Id
                    type: str
      data_disks:
        description:
          - >-
            Specifies the parameters that are used to add a data disk to a
            virtual machine. :code:`<br>`:code:`<br>` For more information about
            disks, see `About disks and VHDs for Azure virtual machines
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
        type: list
  additional_capabilities:
    description:
      - >-
        Specifies additional capabilities enabled or disabled on the virtual
        machine in the scale set. For instance: whether the virtual machine has
        the capability to support attaching managed data disks with UltraSSD_LRS
        storage account type.
    type: dict
    suboptions:
      ultra_ssd_enabled:
        description:
          - >-
            The flag that enables or disables a capability to have one or more
            managed data disks with UltraSSD_LRS storage account type on the VM
            or VMSS. Managed disks with storage account type UltraSSD_LRS can be
            added to a virtual machine or virtual machine scale set only if this
            property is enabled.
        type: bool
  os_profile:
    description:
      - Specifies the operating system settings for the virtual machine.
    type: dict
    suboptions:
      computer_name:
        description:
          - >-
            Specifies the host OS name of the virtual machine.
            :code:`<br>`:code:`<br>` This name cannot be updated after the VM is
            created. :code:`<br>`:code:`<br>` **Max-length (Windows):** 15
            characters :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
            characters. :code:`<br>`:code:`<br>` For naming conventions and
            restrictions see `Azure infrastructure services implementation
            guidelines
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions>`_.
        type: str
      admin_username:
        description:
          - >-
            Specifies the name of the administrator account.
            :code:`<br>`:code:`<br>` This property cannot be updated after the
            VM is created. :code:`<br>`:code:`<br>` **Windows-only
            restriction:** Cannot end in "." :code:`<br>`:code:`<br>`
            **Disallowed values:** "administrator", "admin", "user", "user1",
            "test", "user2", "test1", "user3", "admin1", "1", "123", "a",
            "actuser", "adm", "admin2", "aspnet", "backup", "console", "david",
            "guest", "john", "owner", "root", "server", "sql", "support",
            "support_388945a0", "sys", "test2", "test3", "user4", "user5".
            :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1  character
            :code:`<br>`:code:`<br>` **Max-length (Linux):** 64 characters
            :code:`<br>`:code:`<br>` **Max-length (Windows):** 20 characters 
            :code:`<br>`:code:`<br>`:code:`<li>` For root access to the Linux
            VM, see `Using root privileges on Linux virtual machines in Azure
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
            :code:`<br>`:code:`<li>` For a list of built-in system users on
            Linux that should not be used in this field, see `Selecting User
            Names for Linux on Azure
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
        type: str
      admin_password:
        description:
          - >-
            Specifies the password of the administrator account.
            :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8 characters
            :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 6 characters
            :code:`<br>`:code:`<br>` **Max-length (Windows):** 123 characters
            :code:`<br>`:code:`<br>` **Max-length (Linux):** 72 characters
            :code:`<br>`:code:`<br>` **Complexity requirements:** 3 out of 4
            conditions below need to be fulfilled :code:`<br>` Has lower
            characters :code:`<br>`Has upper characters :code:`<br>` Has a digit
            :code:`<br>` Has a special character (Regex match [\W_])
            :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123",
            "P@$$w0rd", "P@ssw0rd", "P@ssword123", "Pa$$word", "pass@word1",
            "Password!", "Password1", "Password22", "iloveyou!"
            :code:`<br>`:code:`<br>` For resetting the password, see `How to
            reset the Remote Desktop service or its login password in a Windows
            VM
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
            :code:`<br>`:code:`<br>` For resetting root password, see `Manage
            users, SSH, and check or repair disks on Azure Linux VMs using the
            VMAccess Extension
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
        type: str
      custom_data:
        description:
          - >-
            Specifies a base-64 encoded string of custom data. The base-64
            encoded string is decoded to a binary array that is saved as a file
            on the Virtual Machine. The maximum length of the binary array is
            65535 bytes. :code:`<br>`:code:`<br>` **Note: Do not pass any
            secrets or passwords in customData property**
            :code:`<br>`:code:`<br>` This property cannot be updated after the
            VM is created. :code:`<br>`:code:`<br>` customData is passed to the
            VM to be saved as a file, for more information see `Custom Data on
            Azure VMs
            <https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/>`_
            :code:`<br>`:code:`<br>` For using cloud-init for your Linux VM, see
            `Using cloud-init to customize a Linux VM during creation
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
        type: str
      windows_configuration:
        description:
          - Specifies Windows operating system settings on the virtual machine.
        type: dict
        suboptions:
          provision_vm_agent:
            description:
              - >-
                Indicates whether virtual machine agent should be provisioned on
                the virtual machine. :code:`<br>`:code:`<br>` When this property
                is not specified in the request body, default behavior is to set
                it to true.  This will ensure that VM Agent is installed on the
                VM so that extensions can be added to the VM later.
            type: bool
          enable_automatic_updates:
            description:
              - >-
                Indicates whether Automatic Updates is enabled for the Windows
                virtual machine. Default value is true. :code:`<br>`:code:`<br>`
                For virtual machine scale sets, this property can be updated and
                updates will take effect on OS reprovisioning.
            type: bool
          time_zone:
            description:
              - >-
                Specifies the time zone of the virtual machine. e.g. "Pacific
                Standard Time". :code:`<br>`:code:`<br>` Possible values can be
                `TimeZoneInfo.Id
                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                value from time zones returned by
                `TimeZoneInfo.GetSystemTimeZones
                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
            type: str
          additional_unattend_content:
            description:
              - >-
                Specifies additional base-64 encoded XML formatted information
                that can be included in the Unattend.xml file, which is used by
                Windows Setup.
            type: list
          patch_settings:
            description:
              - Specifies settings related to in-guest patching (KBs).
            type: dict
            suboptions:
              patch_mode:
                description:
                  - >-
                    Specifies the mode of in-guest patching to IaaS virtual
                    machine.:code:`<br />`:code:`<br />` Possible values
                    are::code:`<br />`:code:`<br />` **Manual** - You  control
                    the application of patches to a virtual machine. You do this
                    by applying patches manually inside the VM. In this mode,
                    automatic updates are disabled; the property
                    WindowsConfiguration.enableAutomaticUpdates must be
                    false:code:`<br />`:code:`<br />` **AutomaticByOS** - The
                    virtual machine will automatically be updated by the OS. The
                    property WindowsConfiguration.enableAutomaticUpdates must be
                    true. :code:`<br />`:code:`<br />` ** AutomaticByPlatform**
                    - the virtual machine will automatically updated by the
                    platform. The properties provisionVMAgent and
                    WindowsConfiguration.enableAutomaticUpdates must be true
                type: choice
          win_rm:
            description:
              - >-
                Specifies the Windows Remote Management listeners. This enables
                remote Windows PowerShell.
            type: dict
            suboptions:
              listeners:
                description:
                  - The list of Windows Remote Management listeners
                type: list
      linux_configuration:
        description:
          - >-
            Specifies the Linux operating system settings on the virtual
            machine. :code:`<br>`:code:`<br>`For a list of supported Linux
            distributions, see `Linux on Azure-Endorsed Distributions
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
            :code:`<br>`:code:`<br>` For running non-endorsed distributions, see
            `Information for Non-Endorsed Distributions
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
        type: dict
        suboptions:
          disable_password_authentication:
            description:
              - Specifies whether password authentication should be disabled.
            type: bool
          ssh:
            description:
              - Specifies the ssh key configuration for a Linux OS.
            type: dict
            suboptions:
              public_keys:
                description:
                  - >-
                    The list of SSH public keys used to authenticate with linux
                    based VMs.
                type: list
          provision_vm_agent:
            description:
              - >-
                Indicates whether virtual machine agent should be provisioned on
                the virtual machine. :code:`<br>`:code:`<br>` When this property
                is not specified in the request body, default behavior is to set
                it to true.  This will ensure that VM Agent is installed on the
                VM so that extensions can be added to the VM later.
            type: bool
      secrets:
        description:
          - >-
            Specifies set of certificates that should be installed onto the
            virtual machine.
        type: list
      allow_extension_operations:
        description:
          - >-
            Specifies whether extension operations should be allowed on the
            virtual machine. :code:`<br>`:code:`<br>`This may only be set to
            False when no extensions are present on the virtual machine.
        type: bool
      require_guest_provision_signal:
        description:
          - >-
            Specifies whether the guest provision signal is required to infer
            provision success of the virtual machine.  **Note: This property is
            for private testing only, and all customers must not set the
            property to false.**
        type: bool
  security_profile:
    description:
      - Specifies the Security related profile settings for the virtual machine.
    type: dict
    suboptions:
      encryption_at_host:
        description:
          - >-
            This property can be used by user in the request to enable or
            disable the Host Encryption for the virtual machine or virtual
            machine scale set. This will enable the encryption for all the disks
            including Resource/Temp disk at host itself.
            :code:`<br>`:code:`<br>` Default: The Encryption at host will be
            disabled unless this property is set to true for the resource.
        type: bool
  network_profile:
    description:
      - Specifies the network interfaces of the virtual machine.
    type: dict
    suboptions:
      network_interfaces:
        description:
          - >-
            Specifies the list of resource Ids for the network interfaces
            associated with the virtual machine.
        type: list
  network_profile_configuration:
    description:
      - Specifies the network profile configuration of the virtual machine.
    type: dict
    suboptions:
      network_interface_configurations:
        description:
          - The list of network configurations.
        type: list
  diagnostics_profile:
    description:
      - >-
        Specifies the boot diagnostic settings state.
        :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
    type: dict
    suboptions:
      boot_diagnostics:
        description:
          - >-
            Boot Diagnostics is a debugging feature which allows you to view
            Console Output and Screenshot to diagnose VM status.
            :code:`<br>`:code:`<br>` You can easily view the output of your
            console log. :code:`<br>`:code:`<br>` Azure also enables you to see
            a screenshot of the VM from the hypervisor.
        type: dict
        suboptions:
          enabled:
            description:
              - >-
                Whether boot diagnostics should be enabled on the Virtual
                Machine.
            type: bool
          storage_uri:
            description:
              - >-
                Uri of the storage account to use for placing the console output
                and screenshot. :code:`<br>`:code:`<br>`If storageUri is not
                specified while enabling boot diagnostics, managed storage will
                be used.
            type: str
  availability_set:
    description:
      - >-
        Specifies information about the availability set that the virtual
        machine should be assigned to. Virtual machines specified in the same
        availability set are allocated to different nodes to maximize
        availability. For more information about availability sets, see `Manage
        the availability of virtual machines
        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
        :code:`<br>`:code:`<br>` For more information on Azure planned
        maintenance, see `Planned maintenance for virtual machines in Azure
        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
        :code:`<br>`:code:`<br>` Currently, a VM can only be added to
        availability set at creation time. An existing VM cannot be added to an
        availability set.
    type: dict
    suboptions:
      id:
        description:
          - Resource Id
        type: str
  license_type:
    description:
      - >-
        Specifies that the image or disk that is being used was licensed
        on-premises. This element is only used for images that contain the
        Windows Server operating system. :code:`<br>`:code:`<br>` Possible
        values are: :code:`<br>`:code:`<br>` Windows_Client
        :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>` If this
        element is included in a request for an update, the value must match the
        initial value. This value cannot be updated. :code:`<br>`:code:`<br>`
        For more information, see `Azure Hybrid Use Benefit for Windows Server
        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
        :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
    type: str
  protection_policy:
    description:
      - Specifies the protection policy of the virtual machine.
    type: dict
    suboptions:
      protect_from_scale_in:
        description:
          - >-
            Indicates that the virtual machine scale set VM shouldn't be
            considered for deletion during a scale-in operation.
        type: bool
      protect_from_scale_set_actions:
        description:
          - >-
            Indicates that model updates or actions (including scale-in)
            initiated on the virtual machine scale set should not be applied to
            the virtual machine scale set VM.
        type: bool
  expand:
    description:
      - >-
        The expand expression to apply to the operation. Allowed values are
        'instanceView'.
    type: str
  virtual_machine_scale_set_name:
    description:
      - The name of the VM scale set.
    type: str
  filter:
    description:
      - >-
        The filter to apply to the operation. Allowed values are
        'startswith(instanceView/statuses/code, 'PowerState') eq true',
        'properties/latestModelApplied eq true', 'properties/latestModelApplied
        eq false'.
    type: str
  select:
    description:
      - >-
        The list parameters. Allowed values are 'instanceView',
        'instanceView/statuses'.
    type: str
  skip_shutdown:
    description:
      - >-
        The parameter to request non-graceful VM shutdown. True value for this
        flag indicates non-graceful shutdown whereas false indicates otherwise.
        Default value for this flag is false if not specified
    type: bool
  sas_uri_expiration_time_in_minutes:
    description:
      - >-
        Expiration duration in minutes for the SAS URIs with a value between 1
        to 1440 minutes. :code:`<br>`:code:`<br>`NOTE: If not specified, SAS
        URIs will be generated with a default expiration duration of 120
        minutes.
    type: integer
  command_id:
    description:
      - The run command id.
    type: str
  script:
    description:
      - >-
        Optional. The script to be executed.  When this value is given, the
        given script will override the default script of the command.
    type: list
  parameters:
    description:
      - The run command parameters.
    type: list
  state:
    description:
      - Assert the state of the VirtualMachineScaleSetVM.
      - >-
        Use C(present) to create or update an VirtualMachineScaleSetVM and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''


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


class AzureRMVirtualMachineScaleSetVM(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            instance_id=dict(
                type='str'
            ),
            temp_disk=dict(
                type='bool',
                disposition='/temp_disk'
            ),
            location=dict(
                type='str',
                disposition='/location'
            ),
            plan=dict(
                type='dict',
                disposition='/plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    )
                )
            ),
            hardware_profile=dict(
                type='dict',
                disposition='/hardware_profile',
                options=dict(
                    vm_size=dict(
                        type='choice',
                        disposition='vm_size'
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/storage_profile',
                options=dict(
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            publisher=dict(
                                type='str',
                                disposition='publisher'
                            ),
                            offer=dict(
                                type='str',
                                disposition='offer'
                            ),
                            sku=dict(
                                type='str',
                                disposition='sku'
                            ),
                            version=dict(
                                type='str',
                                disposition='version'
                            ),
                            exact_version=dict(
                                type='str',
                                updatable=False,
                                disposition='exact_version'
                            )
                        )
                    ),
                    os_disk=dict(
                        type='dict',
                        disposition='os_disk',
                        options=dict(
                            os_type=dict(
                                type='sealed-choice',
                                disposition='os_type'
                            ),
                            encryption_settings=dict(
                                type='dict',
                                disposition='encryption_settings',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='disk_encryption_key',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='secret_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='key_encryption_key',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='key_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    )
                                )
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='vhd',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            image=dict(
                                type='dict',
                                disposition='image',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            caching=dict(
                                type='sealed-choice',
                                disposition='caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='write_accelerator_enabled'
                            ),
                            diff_disk_settings=dict(
                                type='dict',
                                disposition='diff_disk_settings',
                                options=dict(
                                    option=dict(
                                        type='choice',
                                        disposition='option'
                                    ),
                                    placement=dict(
                                        type='choice',
                                        disposition='placement'
                                    )
                                )
                            ),
                            create_option=dict(
                                type='choice',
                                disposition='create_option',
                                required=True
                            ),
                            disk_size_gb=dict(
                                type='integer',
                                disposition='disk_size_gb'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='managed_disk',
                                options=dict(
                                    storage_account_type=dict(
                                        type='choice',
                                        disposition='storage_account_type'
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='disk_encryption_set',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    data_disks=dict(
                        type='list',
                        disposition='data_disks'
                    )
                )
            ),
            additional_capabilities=dict(
                type='dict',
                disposition='/additional_capabilities',
                options=dict(
                    ultra_ssd_enabled=dict(
                        type='bool',
                        disposition='ultra_ssd_enabled'
                    )
                )
            ),
            os_profile=dict(
                type='dict',
                disposition='/os_profile',
                options=dict(
                    computer_name=dict(
                        type='str',
                        disposition='computer_name'
                    ),
                    admin_username=dict(
                        type='str',
                        disposition='admin_username'
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password'
                    ),
                    custom_data=dict(
                        type='str',
                        disposition='custom_data'
                    ),
                    windows_configuration=dict(
                        type='dict',
                        disposition='windows_configuration',
                        options=dict(
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            ),
                            enable_automatic_updates=dict(
                                type='bool',
                                disposition='enable_automatic_updates'
                            ),
                            time_zone=dict(
                                type='str',
                                disposition='time_zone'
                            ),
                            additional_unattend_content=dict(
                                type='list',
                                disposition='additional_unattend_content'
                            ),
                            patch_settings=dict(
                                type='dict',
                                disposition='patch_settings',
                                options=dict(
                                    patch_mode=dict(
                                        type='choice',
                                        disposition='patch_mode'
                                    )
                                )
                            ),
                            win_rm=dict(
                                type='dict',
                                disposition='win_rm',
                                options=dict(
                                    listeners=dict(
                                        type='list',
                                        disposition='listeners'
                                    )
                                )
                            )
                        )
                    ),
                    linux_configuration=dict(
                        type='dict',
                        disposition='linux_configuration',
                        options=dict(
                            disable_password_authentication=dict(
                                type='bool',
                                disposition='disable_password_authentication'
                            ),
                            ssh=dict(
                                type='dict',
                                disposition='ssh',
                                options=dict(
                                    public_keys=dict(
                                        type='list',
                                        disposition='public_keys'
                                    )
                                )
                            ),
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            )
                        )
                    ),
                    secrets=dict(
                        type='list',
                        disposition='secrets'
                    ),
                    allow_extension_operations=dict(
                        type='bool',
                        disposition='allow_extension_operations'
                    ),
                    require_guest_provision_signal=dict(
                        type='bool',
                        disposition='require_guest_provision_signal'
                    )
                )
            ),
            security_profile=dict(
                type='dict',
                disposition='/security_profile',
                options=dict(
                    encryption_at_host=dict(
                        type='bool',
                        disposition='encryption_at_host'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    network_interfaces=dict(
                        type='list',
                        disposition='network_interfaces'
                    )
                )
            ),
            network_profile_configuration=dict(
                type='dict',
                disposition='/network_profile_configuration',
                options=dict(
                    network_interface_configurations=dict(
                        type='list',
                        disposition='network_interface_configurations'
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='boot_diagnostics',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled'
                            ),
                            storage_uri=dict(
                                type='str',
                                disposition='storage_uri'
                            )
                        )
                    )
                )
            ),
            availability_set=dict(
                type='dict',
                disposition='/availability_set',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/license_type'
            ),
            protection_policy=dict(
                type='dict',
                disposition='/protection_policy',
                options=dict(
                    protect_from_scale_in=dict(
                        type='bool',
                        disposition='protect_from_scale_in'
                    ),
                    protect_from_scale_set_actions=dict(
                        type='bool',
                        disposition='protect_from_scale_set_actions'
                    )
                )
            ),
            expand=dict(
                type='constant'
            ),
            virtual_machine_scale_set_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            select=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            ),
            skip_shutdown=dict(
                type='bool'
            ),
            sas_uri_expiration_time_in_minutes=dict(
                type='integer'
            ),
            command_id=dict(
                type='str',
                disposition='/command_id'
            ),
            script=dict(
                type='list',
                disposition='/script'
            ),
            parameters=dict(
                type='list',
                disposition='/parameters'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.expand = None
        self.virtual_machine_scale_set_name = None
        self.filter = None
        self.select = None
        self.expand = None
        self.skip_shutdown = None
        self.sas_uri_expiration_time_in_minutes = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineScaleSetVM, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.virtual_machine_scale_set_vms.create_or_update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSetVM instance.')
            self.fail('Error creating the VirtualMachineScaleSetVM instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.delete(resource_group_name=self.resource_group_name,
                                                                             vm_scale_set_name=self.vm_scale_set_name,
                                                                             instance_id=self.instance_id)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSetVM instance.')
            self.fail('Error deleting the VirtualMachineScaleSetVM instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        found = False
        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get(resource_group_name=self.resource_group_name,
                                                                          vm_scale_set_name=self.vm_scale_set_name,
                                                                          instance_id=self.instance_id,
                                                                          expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineScaleSetVM()


if __name__ == '__main__':
    main()
