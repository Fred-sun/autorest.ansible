import {AnsibleCodeModel} from "../Common/AnsibleCodeModel";
import {ArtifactType} from "../../test";
import {GenerateModuleRestInfo} from "./AnsibleModuleRestInfo";
import {GenerateModuleSdk} from "./AnsibleModuleSdk";
import {GenerateModuleSdkInfo} from "./AnsibleModuleSdkInfo";
import {GenerateModuleRest} from "./AnsibleModuleRest";


export function GenerateAll(model:AnsibleCodeModel, type:ArtifactType) {
    let modules = model.modules;
    let files = [];
    let path = "";
    for (let module of modules){
        if (module.IsInfoModule){
            if (type == ArtifactType.ArtifactTypeAnsibleRest){
                files[path+module.ModuleName+".py"] = GenerateModuleRestInfo(model, false);
            }
            if (type == ArtifactType.ArtifactTypeAnsibleSdk){
                files[path+module.ModuleName+".py"] = GenerateModuleSdkInfo(model);
            }
        }else {
            if (type == ArtifactType.ArtifactTypeAnsibleRest){
                files[path+module.ModuleName+".py"] = GenerateModuleRest(model, false);
            }
            if (type == ArtifactType.ArtifactTypeAnsibleSdk){
                files[path+module.ModuleName+".py"] = GenerateModuleSdk(model);
            }
        }
    }
    return files;
}
