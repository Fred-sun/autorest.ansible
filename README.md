# configuration

See documentation [here](doc/00-overview.md)

``` yaml

python:
    reason: 'make sure python flag exists to load config in python.md'
azure-arm: true

use-extension:
  "@autorest/python": "5.1.0-preview.4"
  "@autorest/clicommon": "0.4.13"

require:
  - ./readme.python.md
  - ./readme.cli.md

pipeline-model: v3

pipeline:
    python/m2r:
        input: clicommon/identity
    hider:
        input: python/namer
        output-artifact: source-file-hider
    python/codegen:
        input: hider
    ansible:
        input: python/namer
        output-artifact: some-file-generated-by-ansible
    ansible/emitter:
        input:
            - hider
            - ansible
        scope: scope-ansible/emitter

scope-ansible/emitter:
    is-object: false
    output-artifact:
        - source-file-hider
        - some-file-generated-by-ansible
    output-folder: $(az-output-folder)

modelerfour:
    lenient-model-deduplication: true
    group-parameters: true
    flatten-models: true
    flatten-payloads: true

```

