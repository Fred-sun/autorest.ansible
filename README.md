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


pipeline-model: v3

modelerfour:
    additional-checks: false


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
