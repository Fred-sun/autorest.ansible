import { AutoRestExtension, Channel, Host } from "@azure-tools/autorest-extension-base";
import {CodeModelGroup} from "./plugins/Common/CodeModelGroup";
import * as yaml from "node-yaml";


export type LogCallback = (message: string) => void;
export type FileCallback = (path: string, rows: string[]) => void;
export  enum ArtifactType {
    ArtifactTypeAnsibleSdk,
    ArtifactTypeAnsibleRest,
    ArtifactTypeAnsibleCollection
}


export async function main() {
    const extension = new AutoRestExtension();
    extension.Add("ansible", async autoRestApi => {
        let log = await autoRestApi.GetValue("log");
        var infoStr: string[];
        function Info(s: string)
        {
            if (log)
            {
                autoRestApi.Message({
                    Channel: Channel.Information,
                    Text: s
                });
                infoStr.push(s);
            }
        }

        function WriteFile(path: string, rows: string[])
        {
            autoRestApi.WriteFile(path, rows.join('\r\n'));
        }
        const inputFileUris = await autoRestApi.ListInputs();
        Info("input file:" + inputFileUris);
        const inputFiles: string[] = await Promise.all(inputFileUris.filter(uri =>uri.endsWith("no-tags.yaml")).map(uri => autoRestApi.ReadFile(uri)));
        autoRestApi.WriteFile("code-model-v4-no-tags.yaml", inputFiles.join('\r\n'));
        const inputFiles2: string[] = await Promise.all(inputFileUris.filter(uri =>uri.endsWith("v4.yaml")).map(uri => autoRestApi.ReadFile(uri)));
        autoRestApi.WriteFile("code-model-v4.yaml", inputFiles2.join('\r\n'));

        for (let iff of inputFiles){
            const jsyaml = require('js-yaml');
            let climodel = jsyaml.safeLoad(iff);
            // let modelGroup = new CodeModelGroup(climodel, Info);
            // modelGroup.init();
            for (let m of climodel.operationGroups){
                Info("============== moduleName: "+m["$key"]+" =================");
                for (let method of m.operations){
                    Info("      method: "+method.requests[0].protocol.http.method);
                    Info("      path:" + method.requests[0].protocol.http.path);
                    for (var p of method.parameters){
                        Info("              parameters:" + yaml.dump(p));
                    }
                }
            }
        }
        WriteFile("test.txt", infoStr);
    });
    extension.Run();
}

main();
