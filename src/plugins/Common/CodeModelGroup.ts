import {LogCallback} from "../../index";
import {CodeModel, SwaggerModelType} from "./CodeModel";
import {ModuleMethod, ModuleOption, ModuleOptionKind} from "./ModuleMap";

export class CodeModelGroup {
    private _swagger: any = null;
    public models: CodeModel[] = [];
    private _log: LogCallback;
    constructor(swagger: any, log: LogCallback) {
        this._swagger = swagger;
        this._log = log;
    }
    public init(){
        for (let m of this._swagger.operationGroups){
            let codeModel = new CodeModel();
            codeModel.ModuleName = m["$key"];
            codeModel.ObjectName = codeModel.ModuleObjectName();
            codeModel.ModuleClassName = codeModel.GetModuleClassName();
            codeModel.BasicURL = this.GetBasicCRUDUrl(m.operations);
            for (let method of m.operations){
                this.AddMethod(method, codeModel);
            }
        }
    }

    private GetBasicCRUDUrl(methods: any[]): string {
        let baseUrl: string = "";

        // find base CRUD URL it will be used to classify get methods
        for (let method of methods)
        {
            if (method.requests[0].protocol.http.method !== undefined) {
                let httpMethod = method.requests[0].protocol.http.method;
                if (httpMethod == 'put' || httpMethod == 'patch' || httpMethod == 'delete') {
                    if (method.requests[0].protocol.http.path !== undefined) {
                        baseUrl = method.requests[0].protocol.http.path;
                        break;
                    }
                }

            }
        }

        return baseUrl;
    }

    private AddMethod(method:any, codeModel:CodeModel)
    {

        var moduleMethod = new ModuleMethod();
        let name = method.language.default.name;
        moduleMethod.Name = name;
        moduleMethod.NameSwagger = name;
        if (method.requests[0].protocol != undefined && method.requests[0].protocol.http != undefined) {
            moduleMethod.Url = (method.requests[0].protocol.http.path != undefined) ? method.requests[0].protocol.http.path : "";
            moduleMethod.HttpMethod = (method.requests[0].protocol.http.method != undefined) ? method.requests[0].protocol.http.method : "";
        }
        moduleMethod.ApiVersion = method.apiVersions[0].version;

        // moduleMethod.Kind = this.ClassifyMethod(moduleMethod, codeModel.BasicURL);

        for (var p of method.parameters)
        {
            let option: ModuleOption = this.LoadModuleOption(p);

            if (option != undefined) {
                // this._log("add option:" + option.NameSwagger + " for method:" + moduleMethod.Name);
                if (option.Kind === TFModuleOptionKind.MODULE_OPTION_PATH)
                {
                    let splittedId: string[] = moduleMethod.Url.split("/{" + option.NameSwagger + '}');

                    if (splittedId.length == 2)
                    {
                        option.IdPortion = splittedId[0].split('/').pop();
                    }
                    else
                    {
                        this._log("ERROR: COULDN'T EXTRACT ID PORTION");
                        splittedId.forEach(element => {
                            this._log(" ... part: " + element);
                        });
                        this._log(" ... {" + option.NameSwagger + "}");
                        this._log(" ... " + moduleMethod.Url);
                    }

                    /* ajust path option schema name. */
                    let name = option.NameSwagger;
                    if (this.needTrimPackageName(option, moduleMethod.Url, codeModel)) {
                        name = TrimPackageName(TrimPackageName(pascalCase(option.NameSwagger), this._cliName.toLowerCase()), TrimPluralName(codeModel.NameSwagger));
                    }
                    if (this._validMethodKind.has(moduleMethod.Kind)) {
                        /* ajust it to resource name if it is the last part of the url. */
                        if (moduleMethod.Url.endsWith("/{" + option.NameSwagger + '}')) {
                            name = "name";
                        }

                    }
                    option.NameSwagger = Uncapitalize(name);
                    option.SwaggerPath[0] = option.NameSwagger;
                    option.GoVariableName = GetEscapedReservedName(Uncapitalize(name));
                    option.GoFieldName = ToGoCase(name);
                    option.SetSchemaName(ToSnakeCase(name));
                }
                moduleMethod.Options.push(option);
                if (option.Required)
                {
                    moduleMethod.RequiredOptions.push(option);
                }
            }

        }

        /* load body requests. */
        if (method.requests[0].parameters !== undefined) {
            for (var p of method.requests[0].parameters) {
                let option: TFModuleOption = this.LoadModuleOption(p);
                moduleMethod.Options.push(option);
                if (option.Required)
                {
                    moduleMethod.RequiredOptions.push(option);
                }

            }
        }
        /* sort the request option according to the type: in-path, in-body, in-header */
        //moduleMethod.Options.sort((n1, n2) => n1.Kind - n2.Kind);
        // moduleMethod.Options.sort((n1, n2) => ((n1.Required ? 1 : 0) - (n2.Required ? 1:0)));

        moduleMethod.IsAsync = false; //Get the value from model 4.
        if (method.extensions !== undefined && method.extensions["x-ms-long-running-operation"] !== undefined) {
            moduleMethod.IsAsync = method.extensions["x-ms-long-running-operation"];
        }
        moduleMethod.Documentation = (method.language.default.description != undefined) ? method.language.default.description: "";

        for (var p of method.responses) {
            if (p.schema == undefined) continue;
            if (!ContainOptionByName(p.language.default.name,p.schema.language.default.name, moduleMethod.RequiredOptions)) {
                let responseoption :TFModuleOption = this.LoadModuleOption(p, true);
                if (responseoption != undefined) {
                    moduleMethod.ResponseOptions.push(responseoption);
                }
            }
        }

        moduleMethod.Timeout = this.GetMethodDefaultTimeout(moduleMethod.Kind);

        this.ClassifyComputed(moduleMethod);

        /* add examples. */
        if (method.extensions !== undefined && method.extensions["x-ms-examples"] !== undefined) {
            this._log("add examples");
            for (let key in method.extensions["x-ms-examples"]) {
                moduleMethod.Examples.push(method.extensions["x-ms-examples"][key]);
            }
        }

        moduleMethod.SetDiscriminateBaseOptions();
        if (moduleMethod.Kind === TFModuleMethodKind.MODULE_METHOD_CREATE) {
            let containedBase:Set<string> = new Set<string>();
            for (let base of moduleMethod.DiscriminatorBaseOptions) {
                if (containedBase.has(base.NameInModelSchema)) continue;
                let moduleDiscriminateConfig = new TFModuleDiscriminateConfig(base.NameInModelSchema);
                for (let dis of base.Discriminator.EnumValues) {
                    if (base.GetChild(dis.Value) !== null) {
                        moduleDiscriminateConfig.DiscriminatorValues.push(dis.Value);
                        this._log("add discriminator value " + dis.Key + " of base " + base.NameInModelSchema + " to " + codeModel.NameSwagger);
                    }
                }
                base.NeedSeparated = codeModel.NeedSeparated;
                codeModel.Discrminates.push(moduleDiscriminateConfig);
                containedBase.add(base.NameInModelSchema);
            }
            if (moduleMethod.DiscriminatorBaseOptions.length > 0) codeModel.Polymorphism = true;
        }

        codeModel.Methods.push(moduleMethod);
    }

    private LoadModuleOption(p: any, isResponse:boolean = false): ModuleOption {
        return this.LoadTopLevelOption(p, isResponse);
    }

    private LoadTopLevelOption(p: any, isResponse:boolean = false): ModuleOption {
        let option = this.LoadOption(p, isResponse);
        if (option === undefined) return undefined;
        return option;
    }

    private LoadOption(p: any, isResponse:boolean = false, parent: ModuleOption = null): ModuleOption {
        let name = p.language.default.name;
        this._log("load option:" + name);

        let serializedName = p.language.default.serializedName;
        let extensions:any = p.extensions;
        let required = p.required != undefined ? p.required : false;
        let description = p.language.default.description;

        let option: any;
        let targetschema = p.schema;
        let type = p.schema.type;
        if (type === SwaggerModelType.SWAGGER_MODEL_ARRAY || type === SwaggerModelType.SWAGGER_MODEL_DICTIONARY) {
            targetschema = p.schema.elementType;
        }

        option = new ModuleOption(name);
        option.Required = required;
        option.Documentation = description;
        // if (parent !== null) {
        //     option.SwaggerPath = option.SwaggerPath.concat(parent.SwaggerPath);
        // }
        // option.SwaggerPath.push(name);

        // if (p.readOnly != undefined) {
        //     option.Readonly = p.readOnly;
        //     option.Computed = option.Readonly;
        // }
        if (isResponse) {
            option.Kind = ModuleOptionKind.MODULE_OPTION_RESPONSE;
        } else {
            if (p.protocol != undefined && p.protocol.http != undefined && p.protocol.http.in != undefined) {
                let location = p.protocol.http.in;
                if (location == "url") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                } else if (location == "path") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                } else if (location == "body") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
                } else if (location == "header") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_HEADER;
                } else if (location === "query") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_QUERY;
                } else {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                }
            } else {
                option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
            }
        }

        if (p.implementation != undefined) {
            option.Implementation = p.implementation;
        }

        // if (p.schema != undefined) {
        //     this.LoadSchema(p.schema, option, filterFunction, isResponse);
        // } else {
        //     this._log("no schema for option " + name);
        // }
        //
        //
        // option.GoFieldName = ToGoCase(name);
        // option.GoVariableName = GetEscapedReservedName(Uncapitalize(name));
        // this.ClassifyOptionGoType(p.schema, option);
        //
        // if (option.GoFieldName === "Properties" &&
        //     (option.Type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM) || option.Type === SwaggerModelType.SWAGGER_MODEL_OBJECT)) {
        //     option.GoFieldName = option.GoTypeName;
        //     if (option.Type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) option.GoFieldName = option.ItemGoTypeName;
        // }
        //
        // option.SetSchemaName(ToSnakeCase(name));
        // this.ClassifyOptionSchemaType(p.schema, option);
        //
        // option.ExpandFunc = this.GetOptionExpandFunc(option.Type);
        // option.ValidateFunc = this.GetOptionValidateFunc(option.Type)
        //
        // if (option.IsBase && option instanceof TFDiscriminatorBaseOption) {
        //     this.AdjustDerivedOptionNames(option);
        //     let typename = option.GoTypeName;
        //     if (option.IsList || option.IsMap) {
        //         typename = option.ItemGoTypeName;
        //     }
        //     option.InterfaceName = "Basic" + Capitalize(typename);
        // }

        return option;

    }
}
