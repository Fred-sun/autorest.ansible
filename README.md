# configuration

See documentation [here](doc/00-overview.md)

``` yaml
use-extension:
  "@autorest/clicommon": "0.4.12"


pipeline-model: v3

pipeline:
    ansible/generate:
        plugin: ansible
        input: clicommon/identity
        output-artifact: some-file-generated-by-hello-world
modelerfour:
    additional-checks: false
```
