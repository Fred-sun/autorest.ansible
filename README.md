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
        output-artifact: source-file-cli
    ansible/emitter:
        input: generate
        scope: scope-here

scope-here:
    is-object: false
    output-artifact:
        - source-file-cli
modelerfour:
    additional-checks: false
```
