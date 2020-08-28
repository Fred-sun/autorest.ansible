/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
import * as yaml from "node-yaml";

// import { Example } from "../Common/Example";


import { AnsibleCodeModel} from "../Common/AnsibleCodeModel";

import { GenerateModuleRest } from "./AnsibleModuleRest";
import { GenerateModuleRestInfo } from "./AnsibleModuleRestInfo";
import { GenerateModuleSdk } from "./AnsibleModuleSdk";
import { GenerateModuleSdkInfo } from "./AnsibleModuleSdkInfo";

import {Channel, Host, startSession} from "@azure-tools/autorest-extension-base";
import {CodeModel, codeModelSchema} from "@azure-tools/codemodel";
import {EOL} from "os";
import {ArtifactType, GenerateAll} from "./AnsibleGenerator";
import {serialize} from "@azure-tools/codegen";


export async function processRequest(host: Host) {
    const debug = await host.GetValue('debug') || false;
    function WriteFile(path: string, rows: string[])
    {
        if (rows instanceof Array){
            host.WriteFile(path, rows.join("\r\n"));
        }
    }
    function Info(message: string) {
        host.Message({
            Channel: Channel.Information,
            Text: message
        });
    }
    try {
        const session = await startSession<CodeModel>(host, {}, codeModelSchema);
        let codeModel = new AnsibleCodeModel(session.model);
        let files = {};
        files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk);
        for (let f in files) {
            Info(f);
            WriteFile(f, files[f]);
        }
        host.WriteFile("model4.yaml",serialize(session.model));
    } catch (E) {
        if (debug) {
            console.error(`${__filename} - FAILURE  ${JSON.stringify(E)} ${E.stack}`);
        }
        // throw E;
    }

}

