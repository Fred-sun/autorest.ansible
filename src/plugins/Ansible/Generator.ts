/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


// import { Example } from "../Common/Example";


import { AnsibleCodeModel} from "../Common/AnsibleCodeModel";

import { GenerateModuleRest } from "./AnsibleModuleRest";
import { GenerateModuleRestInfo } from "./AnsibleModuleRestInfo";
import { GenerateModuleSdk } from "./AnsibleModuleSdk";
import { GenerateModuleSdkInfo } from "./AnsibleModuleSdkInfo";

import {Host, startSession} from "@azure-tools/autorest-extension-base";
import {CodeModel, codeModelSchema} from "@azure-tools/codemodel";
import {EOL} from "os";
import {GenerateAll} from "./AnsibleGenerator";
import {serialize} from "@azure-tools/codegen";

// export function GenerateAnsible(artifactType: ArtifactType,
//                                 modelGroup: CodeModelGroup,
//                                 fileCb: FileCallback,
//                                 logCb: LogCallback)
// {
//     let path: string = "lib/ansible/modules/cloud/azure/";
//
//     let index = 0;
//     console.log(modelGroup.models.length);
//     for(let model of modelGroup.models){
//         try
//         {
//             // logCb(model.ModuleName);
//
//             // if (model.IsInfoModule){
//             //     if (artifactType == ArtifactType.ArtifactTypeAnsibleSdk)
//             //     {
//             //         fileCb(model.ModuleName + ".py", GenerateModuleSdkInfo(model));
//             //     }
//             //
//             //     if (artifactType == ArtifactType.ArtifactTypeAnsibleRest)
//             //     {
//             //
//             //         fileCb( model.ModuleName + ".py", GenerateModuleRestInfo(model, false));
//             //     }
//             //
//             //     if (artifactType == ArtifactType.ArtifactTypeAnsibleCollection)
//             //     {
//             //         fileCb(model.ModuleName.split('_info')[0].split('_').pop() + "_info.py", GenerateModuleRestInfo(model, true));
//             //     }
//             // }
//
//             if (!model.IsInfoModule){
//                 if (artifactType == ArtifactType.ArtifactTypeAnsibleSdk)
//                 {
//                     fileCb(model.ModuleName + ".py", GenerateModuleSdk(model));
//                 }
//
//                 if (artifactType == ArtifactType.ArtifactTypeAnsibleRest)
//                 {
//                     if (model.ModuleName != "azure_rm_gallery")
//                         continue;
//                     console.log(index + "======  "+model.ModuleName);
//                     let rows = GenerateModuleRest(model, false);
//                     console.log(index + "---------"+model.ModuleName);
//                     fileCb(model.ModuleName + ".py", rows);
//
//                 }
//
//                 if (artifactType == ArtifactType.ArtifactTypeAnsibleCollection)
//                 {
//                     fileCb(model.ModuleName.split('_').pop() + ".py", GenerateModuleRest(model, true));
//                 }
//             }
//
//         }
//         catch (e)
//         {
//           logCb("ERROR " + e.stack);
//         }
//         index++;
//     }
// }
export  enum ArtifactType {
    ArtifactTypeAnsibleSdk,
    ArtifactTypeAnsibleRest,
    ArtifactTypeAnsibleCollection
}


export async function processRequest(host: Host) {
    const debug = await host.GetValue('debug') || false;

    try {
        const session = await startSession<CodeModel>(host, {}, codeModelSchema);
        host.WriteFile("model4.yaml",serialize(session.model));
        // let model = new AnsibleCodeModel(session);
        // let files: any = await GenerateAll(model, ArtifactType.ArtifactTypeAnsibleRest);
        // for (let f in files) {
        //     host.WriteFile(f, files[f].join(EOL));
        // }
    } catch (E) {
        if (debug) {
            console.error(`${__filename} - FAILURE  ${JSON.stringify(E)} ${E.stack}`);
        }
        throw E;
    }

}

