import {AnsibleCodeModel} from "../Common/AnsibleCodeModel";

import {GenerateModuleRestInfo} from "./AnsibleModuleRestInfo";
import {GenerateModuleSdk} from "./AnsibleModuleSdk";
import {GenerateModuleSdkInfo} from "./AnsibleModuleSdkInfo";
import {GenerateModuleRest} from "./AnsibleModuleRest";


export  enum ArtifactType {
    ArtifactTypeAnsibleSdk,
    ArtifactTypeAnsibleRest,
    ArtifactTypeAnsibleCollection
}


export function GenerateAll(model:AnsibleCodeModel, type:ArtifactType) {
    let modules = model.Modules;
    let files = [];
    let path = "";
    for (let module of modules){
        console.log(module.ModuleName);
        if (module.IsInfoModule){
            if (type == ArtifactType.ArtifactTypeAnsibleRest){
                files[path+module.ModuleName+".py"] = GenerateModuleRestInfo(module, false);
            }
            if (type == ArtifactType.ArtifactTypeAnsibleSdk){
                files[path+module.ModuleName+".py"] = GenerateModuleSdkInfo(module);
            }
        }else {
            if (type == ArtifactType.ArtifactTypeAnsibleRest){
                files[path+module.ModuleName+".py"] = GenerateModuleRest(module, false);
            }
            if (type == ArtifactType.ArtifactTypeAnsibleSdk){
                files[path+module.ModuleName+".py"] = GenerateModuleSdk(module);
            }
        }
    }
    return files;
}
