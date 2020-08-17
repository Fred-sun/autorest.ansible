# configuration

See documentation [here](doc/00-overview.md)

``` yaml
use-extension:
  "@autorest/python": "5.1.0-preview.4"
  "@autorest/clicommon": "0.4.13"

require:
  - ./readme.python.md

pipeline-model: v3

modelerfour:
    lenient-model-deduplication: true
    group-parameters: true
    flatten-models: true
    flatten-payloads: true

pipeline:
    python/m2r:
        input: clicommon/identity
    ansible:
        input: python/namer
        output-artifact: some-file-generated-by-ansible
    ansible/emitter:
        input: ansible
        scope: scope-ansible/emitter
scope-ansible/emitter:
    input-artifact: some-file-generated-by-ansible
    output-uri-expr: $key
    output-artifact: some-file-generated-by-ansible


```
