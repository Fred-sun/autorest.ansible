import {AnsibleCodeModel} from "./plugins/Common/AnsibleCodeModel";
import {GenerateAll} from "./plugins/Ansible/AnsibleGenerator";
import {EOL} from "os";


export type LogCallback = (message: string) => void;
export type FileCallback = (path: string, rows: string[]) => void;
export  enum ArtifactType {
    ArtifactTypeAnsibleSdk,
    ArtifactTypeAnsibleRest,
    ArtifactTypeAnsibleCollection
}


export async function main() {

    let ss : string[] = [];
    function Info(s: string)
    {
        ss.push(s);
    }

    function WriteFile(path: string, rows: string[])
    {
        let fs = require("fs");
        fs.writeFile("./tmp/"+path, rows.join('\r\n'), function (err) {
            if (err) {
                return console.error(err);
            }
        })
    }
    let fs = require("fs");
    const inputFileUri = "./model4.yaml";


    const input : string = fs.readFileSync(inputFileUri);

    const jsyaml = require('js-yaml');
    let model = jsyaml.safeLoad(input);

    let codeModel = new AnsibleCodeModel(model);
    let files = [];
    files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk);
    for (let f in files) {
        WriteFile(f, files[f]);
    }
    // for (let m of climodel.operationGroups){
    //     Info("============== moduleName: "+m["$key"]+" =================");
    //
    //     let idx1 = 1;
    //     for (let method of m.operations){
    //         Info("============== method: "+idx1+"  =================");
    //         Info("      method: "+method.requests[0].protocol.http.method);
    //         Info("      name: "+method.language.default.name);
    //         Info("      path:" + method.requests[0].protocol.http.path);
    //         Info("      version:" + method.apiVersions[0].version)
    //         idx1++;
    //         let idx2 = 1;
    //         for (var p of method.parameters){
    //             Info("============parameter: "+idx2 + "==============")
    //             Info("" + yaml.dump(p));
    //             idx2++;
    //         }
    //     }
    // }
    // WriteFile("test.txt",ss);

}

main();
