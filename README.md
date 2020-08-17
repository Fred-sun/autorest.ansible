# configuration

See documentation [here](doc/00-overview.md)

``` yaml
use-extension:
  "@autorest/clicommon": "0.4.13"


pipeline-model: v3

modelerfour:
    lenient-model-deduplication: true
    group-parameters: true
    flatten-models: true
    flatten-payloads: true

pipeline:
    ansible:
        input: clicommon/identity
        output-artifact: some-file-generated-by-ansible
    ansible/emitter:
        input: ansible
        scope: scope-ansible/emitter
scope-ansible/emitter:
    input-artifact: some-file-generated-by-ansible
    output-uri-expr: $key
    output-artifact: some-file-generated-by-ansible


```
