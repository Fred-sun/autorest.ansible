# configuration

See documentation [here](doc/00-overview.md)

``` yaml
use-extension:
  "@autorest/clicommon": "0.4.12"


pipeline-model: v3

pipeline:
    ansible:
        input: clicommon/identity
        output-artifact: some-file-generated-by-ansible
modelerfour:
    additional-checks: false
```
