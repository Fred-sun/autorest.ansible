# configuration

See documentation [here](doc/00-overview.md)

``` yaml

python:
    reason: 'make sure python flag exists to load config in python.md'
azure-arm: true

output-folder: $(az-output-folder)
debug-output-folder: $(az-output-folder)/_az_debug

use-extension:
  "@autorest/clicommon": "0.4.12"

cli:
    reason: 'make sure cli flag exists to load config in cli.md'
    naming:
        default:
            parameter: 'snake'
            property: 'snake'
            operation: 'snake'
            operationGroup:  'pascal'
            choice:  'pascal'
            choiceValue:  'snake'
            constant:  'snake'
            type:  'pascal'

require:
  - ./readme.python.md

pipeline-model: v3

modelerfour:
    lenient-model-deduplication: true
    group-parameters: true
    flatten-models: true
    flatten-payloads: true


#payload-flattening-threshold: 4
#recursive-payload-flattening: true

pipeline:
    ansible/generate:
        plugin: ansible
        input: clicommon/identity
        output-artifact: source-file-cli
    trenton/emitter:
        input: generate
        scope: scope-here
scope-here:
    is-object: false
    output-artifact:
        #- source-file-az-hider
        #- source-file-pynamer
        #- source-file-aznamer
        #- source-file-modifiers
        #- source-file-merger
        - source-file-extension
    output-folder: $(az-output-folder)

scope-clicommon:
    output-folder: $(debug-output-folder)
```
