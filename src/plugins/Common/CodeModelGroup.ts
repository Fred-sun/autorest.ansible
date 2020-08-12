import {LogCallback} from "../../index";
import {CodeModel, SwaggerModelType} from "./CodeModel";
import {ModuleMethod, ModuleOption, ModuleOptionKind} from "./ModuleMap";
import {ToSnakeCase, TrimPackageName, Uncapitalize} from "../../utils/helper";
import {pascalCase} from "@azure-tools/codegen";
import {Info} from "@azure-tools/codemodel";

export class CodeModelGroup {
    private _swagger: any = null;
    public models: CodeModel[] = [];
    private _log: LogCallback;
    constructor(swagger: any, log: LogCallback) {
        this._swagger = swagger;
        this._log = log;
    }
    public Init(){
        for (let m of this._swagger.operationGroups){
            let mainCodeModel = new CodeModel(m["$key"], false);
            mainCodeModel.BasicURL = this.GetBasicCRUDUrl(m.operations);
            mainCodeModel.ModuleApiVersion = m.operations[0].apiVersions[0].version;

            let infoCodeModel = new CodeModel(m["$key"], true);
            infoCodeModel.BasicURL = this.GetBasicCRUDUrl(m.operations);
            infoCodeModel.ModuleApiVersion = m.operations[0].apiVersions[0].version;
            this._log("===============Module:"+infoCodeModel.ModuleName+"=====================");
            for (let method of m.operations){
                if( method.requests[0].protocol.http.method == "get"){
                    this.AddMethod(method, infoCodeModel);
                }

                // else
                //     this.AddMethod(method, mainCodeModel);
            }
            for (let method of infoCodeModel.ModuleMethods){
                for (let option of method.Options)
                    infoCodeModel.ModuleOptions.push(option);
            }
            for (let option of infoCodeModel.ModuleOptions)
                this._log("     Moduleoption: " + option.Name)
            this.models.push(mainCodeModel);
            this.models.push(infoCodeModel);
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
        // this._log("     method" + name );
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
                // this._log("             add option:" + option.NameAnsible );
                if (option.Kind === ModuleOptionKind.MODULE_OPTION_PATH)
                {
                    // let splittedId: string[] = moduleMethod.Url.split("/{" + option.NameSwagger + '}');
                    //
                    // if (splittedId.length == 2)
                    // {
                    //     option.IdPortion = splittedId[0].split('/').pop();
                    // }
                    // else
                    // {
                    //     this._log("ERROR: COULDN'T EXTRACT ID PORTION");
                    //     splittedId.forEach(element => {
                    //         this._log(" ... part: " + element);
                    //     });
                    //     this._log(" ... {" + option.NameSwagger + "}");
                    //     this._log(" ... " + moduleMethod.Url);
                    // }

                    // /* ajust path option schema name. */
                    // let name = option.NameSwagger;
                    // if (this.needTrimPackageName(option, moduleMethod.Url, codeModel)) {
                    //     name = TrimPackageName(TrimPackageName(pascalCase(option.NameSwagger), this._cliName.toLowerCase()), TrimPluralName(codeModel.NameSwagger));
                    // }
                    // if (this._validMethodKind.has(moduleMethod.Kind)) {
                    //     /* ajust it to resource name if it is the last part of the url. */
                    //     if (moduleMethod.Url.endsWith("/{" + option.NameSwagger + '}')) {
                    //         name = "name";
                    //     }
                    //
                    // }
                    option.NameSwagger = Uncapitalize(name);
                    option.SwaggerPath[0] = option.NameSwagger;

                    // option.SetSchemaName(ToSnakeCase(name));
                }
                moduleMethod.Options.push(option);
                if (option.Required)
                {
                    moduleMethod.RequiredOptions.push(option.Name);
                }
            }

        }

        /* load body requests. */
        if (method.requests[0].parameters !== undefined) {
            for (var p of method.requests[0].parameters) {
                let option: ModuleOption = this.LoadModuleOption(p);
                moduleMethod.Options.push(option);
                if (option.Required)
                {
                    moduleMethod.RequiredOptions.push(option.Name);
                }

            }
        }
        /* sort the request option according to the type: in-path, in-body, in-header */
        //moduleMethod.Options.sort((n1, n2) => n1.Kind - n2.Kind);
        // moduleMethod.Options.sort((n1, n2) => ((n1.Required ? 1 : 0) - (n2.Required ? 1:0)));

        // moduleMethod.IsAsync = false; //Get the value from model 4.
        // if (method.extensions !== undefined && method.extensions["x-ms-long-running-operation"] !== undefined) {
        //     moduleMethod.IsAsync = method.extensions["x-ms-long-running-operation"];
        // }
        // moduleMethod.Documentation = (method.language.default.description != undefined) ? method.language.default.description: "";
        //
        // for (var p of method.responses) {
        //     if (p.schema == undefined) continue;
        //     if (!ContainOptionByName(p.language.default.name,p.schema.language.default.name, moduleMethod.RequiredOptions)) {
        //         let responseoption :TFModuleOption = this.LoadModuleOption(p, true);
        //         if (responseoption != undefined) {
        //             moduleMethod.ResponseOptions.push(responseoption);
        //         }
        //     }
        // }
        //
        // moduleMethod.Timeout = this.GetMethodDefaultTimeout(moduleMethod.Kind);
        //
        // this.ClassifyComputed(moduleMethod);
        //
        // /* add examples. */
        // if (method.extensions !== undefined && method.extensions["x-ms-examples"] !== undefined) {
        //     this._log("add examples");
        //     for (let key in method.extensions["x-ms-examples"]) {
        //         moduleMethod.Examples.push(method.extensions["x-ms-examples"][key]);
        //     }
        // }
        //
        // moduleMethod.SetDiscriminateBaseOptions();
        // if (moduleMethod.Kind === TFModuleMethodKind.MODULE_METHOD_CREATE) {
        //     let containedBase:Set<string> = new Set<string>();
        //     for (let base of moduleMethod.DiscriminatorBaseOptions) {
        //         if (containedBase.has(base.NameInModelSchema)) continue;
        //         let moduleDiscriminateConfig = new TFModuleDiscriminateConfig(base.NameInModelSchema);
        //         for (let dis of base.Discriminator.EnumValues) {
        //             if (base.GetChild(dis.Value) !== null) {
        //                 moduleDiscriminateConfig.DiscriminatorValues.push(dis.Value);
        //                 this._log("add discriminator value " + dis.Key + " of base " + base.NameInModelSchema + " to " + codeModel.NameSwagger);
        //             }
        //         }
        //         base.NeedSeparated = codeModel.NeedSeparated;
        //         codeModel.Discrminates.push(moduleDiscriminateConfig);
        //         containedBase.add(base.NameInModelSchema);
        //     }
        //     if (moduleMethod.DiscriminatorBaseOptions.length > 0) codeModel.Polymorphism = true;
        // }

        codeModel.ModuleMethods.push(moduleMethod);
    }

    private LoadModuleOption(p: any, isResponse:boolean = false): ModuleOption {
        return this.LoadTopLevelOption(p, isResponse, this.IsAnsibleIgnoredOption);
    }

    private LoadTopLevelOption(p: any, isResponse:boolean = false, filterFunction: (name: string) => (boolean)): ModuleOption {
        let option = this.LoadOption(p, isResponse, filterFunction);
        if (option === undefined) return undefined;
        return option;
    }

    private LoadOption(p: any, isResponse:boolean = false, filterFunction: (name: string) => (boolean), parent: ModuleOption = null): ModuleOption {
        let name = p.language.default.name;
        // this._log("load option:" + name);
        if (filterFunction(name)) return undefined;
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
        option.NameAnsible = ToSnakeCase(name);
        // if (targetschema !== undefined && targetschema.discriminator !== undefined) {
        //     option = new TFDiscriminatorBaseOption(name);
        //     this._log("create TFDiscriminatorBaseOption " + name);
        // } else {
        //     option = new TFModuleOption(name);
        // }

        option.Required = required;
        option.Documentation = description;
        if (parent !== null) {
            option.SwaggerPath = option.SwaggerPath.concat(parent.SwaggerPath);
        }
        option.SwaggerPath.push(name);

        if (p.readOnly != undefined) {
            option.Readonly = p.readOnly;
            option.Computed = option.Readonly;
        }
        if (isResponse) {
            option.Kind = ModuleOptionKind.MODULE_OPTION_RESPONSE;
        } else {
            if (p.protocol != undefined && p.protocol.http != undefined && p.protocol.http.in != undefined) {
                let location = p.protocol.http.in;
                if (location == "url") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                } else if (location == "path") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                    option.IncludeInArgSpec = true;
                } else if (location == "body") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
                    option.IncludeInArgSpec = true;
                } else if (location == "header") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_HEADER;
                } else if (location === "query") {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_QUERY;
                } else {
                    option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                    option.IncludeInArgSpec = true;
                }
            } else {
                option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
                option.IncludeInArgSpec = true;
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

    private IsAnsibleIgnoredOption(name: string) : boolean
    {
        let ignoreOptions = new Set([]);
        return name.indexOf('$') != -1 ||name.indexOf('-') != -1 || ignoreOptions.has(name);
    }

    // private needTrimPackageName(option: ModuleOption, url: string, module: CodeModel): boolean {
    //     if (TrimPackageName(TrimPackageName(pascalCase(option.NameSwagger), this._cliName.toLowerCase()), TrimPluralName(module.NameSwagger)).toLowerCase() === 'name'.toLowerCase()
    //         && !url.endsWith('/{' + option.NameSwagger + '}')) {
    //         return false;
    //     }
    //     return true;
    // }
    // private LoadSchema(schema: any, option:any, filterFunction: (name: string) => (boolean), isResponse:boolean = false) {
    //     let type = schema.type;
    //     let itemtype = "";
    //     let precision = null;
    //     if (schema.precision != undefined) {
    //         precision = schema.precision;
    //     }
    //
    //     if (type === SwaggerModelType.SWAGGER_MODEL_ARRAY) {
    //         if (schema.elementType.type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    //             itemtype = schema.elementType.choiceType.type;
    //         } else {
    //             itemtype = schema.elementType.type;
    //         }
    //         // if (schema.elementType.precision != undefined) {
    //         //     precision = schema.precision;
    //         // }
    //         if (itemtype === SwaggerModelType.SWAGGER_MODEL_OBJECT) {
    //             if (this._compositeTypes != null) this._compositeTypes.push(option);
    //         } else if (itemtype === SwaggerModelType.SWAGGER_MODEL_ENUM) {
    //             if (this._enumTypes !== null ) this._enumTypes.push(option);
    //         }
    //         option.IsList = true;
    //     }
    //     else if (type === SwaggerModelType.SWAGGER_MODEL_DICTIONARY) {
    //         itemtype = schema.elementType.type;
    //         // if (schema.elementType.precision != undefined) {
    //         //     precision = schema.precision;
    //         // }
    //         option.IsMap = true;
    //     } else if (type === SwaggerModelType.SWAGGER_MODEL_CONSTENT) {
    //         itemtype = schema.valueType.type;
    //         // treat string constant as enum
    //         if (itemtype === SwaggerModelType.SWAGGER_MODEL_STRING) {
    //             type = SwaggerModelType.SWAGGER_MODEL_ENUM;
    //             option.EnumValues = this.TF_Type_EnumValues(schema);
    //             if (this._enumTypes !== null ) this._enumTypes.push(option);
    //         }
    //     } else if ( type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    //         // enum type
    //         option.EnumValues = this.TF_Type_EnumValues(schema);
    //         itemtype = schema.choiceType.type;
    //         if (this._enumTypes !== null ) this._enumTypes.push(option);
    //     } else if (type === SwaggerModelType.SWAGGER_MODEL_OBJECT) {
    //         if (this._compositeTypes != null) this._compositeTypes.push(option);
    //     }
    //
    //     if (this.IsNumber(type)) {
    //         let precision = schema.precision;
    //         type = this.GetNumberType(type, precision);
    //     }
    //     if (this.IsNumber(itemtype)) {
    //         itemtype = this.GetNumberType(schema.elementType.type, schema.elementType.precious);;
    //     }
    //
    //     option.Type = type;
    //     option.ItemType = itemtype;
    //     option.precision = precision;
    //     option.NameInModelSchema = schema.language.default.name;
    //
    //     if (schema.defaultValue != undefined) {
    //         option.DefaultValue = schema.defaultValue;
    //         if (type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    //             for (let ev of option.EnumValues) {
    //                 if (ev.Value === option.DefaultValue) {
    //                     option.DefaultValue = ev.GoEnumMemberName;
    //                 }
    //             }
    //         }
    //     }
    //
    //     /*Get constrains */
    //     if (schema.maxLength !== undefined || schema.minLength !== undefined || schema.pattern !== undefined ||
    //         schema.maximum !== undefined || schema.minimum !== undefined) {
    //         option.HasConstrains = true;
    //
    //         if (schema.maxLength !== undefined) option.MaxLength = schema.maxLength;
    //         if (schema.minLength !== undefined) option.MinLength = schema.minLength;
    //         if (schema.maximum !== undefined) option.MaxValue = schema.maximum;
    //         if (schema.minimum !== undefined) option.MinValue = schema.minimum;
    //         if (schema.pattern !== undefined) option.Patten = schema.pattern;
    //
    //         /*insert the option to the validation list. */
    //         //PutToList(option, validate_option_list, validate_option_go_type_name_set);
    //     }
    //     if (type === SwaggerModelType.SWAGGER_MODEL_OBJECT || ((option.IsList || option.IsMap) && option.ItemType == SwaggerModelType.SWAGGER_MODEL_OBJECT)) {
    //         /* add sub options. */
    //         option.SubOptions = [];
    //         let targetschema = schema;
    //         if (option.IsList || option.IsMap) {
    //             targetschema = schema.elementType;
    //         }
    //         /*add object parent. */
    //         let parents = targetschema.parents;
    //         this.LoadParent(parents, option, filterFunction);
    //         this.LoadSubOptions(targetschema, option, filterFunction);
    //
    //         /*pop-up readonly metadata up. */
    //         let popup:boolean = true;
    //         for (let sub of option.SubOptions) {
    //             if (!sub.Readonly) {
    //                 popup = false;
    //                 break;
    //             }
    //         }
    //         if (popup && !option.IsBase) {
    //             option.Readonly = true;
    //         }
    //     }
    //
    //     /* load Discriminator if any */
    //     let targetschema = schema;
    //     if (option.IsList || option.IsMap) {
    //         targetschema = schema.elementType;
    //     }
    //     if (targetschema.discriminator !== undefined && targetschema.discriminator.all !== undefined) {
    //         /* load discriminator. */
    //         option.Discriminator = option.GetSubOption(targetschema.discriminator.property.language.default.name) as TFModuleOption;
    //         option.Discriminator.Required = true;
    //         option.Children = [];
    //         let allderived = targetschema.discriminator.all;
    //         let deriveds = Object.keys(allderived);
    //         if (option.Discriminator as TFModuleOption && !option.Discriminator.Type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    //             /*retrieve discriminator value from discriminator block. */
    //             option.Discriminator.Type = SwaggerModelType.SWAGGER_MODEL_ENUM;
    //             option.Discriminator.ItemType = SwaggerModelType.SWAGGER_MODEL_STRING;
    //             option.Discriminator.ItemGoTypeName = ToGoCase(option.Discriminator.NameSwagger);
    //             option.Discriminator.ItemSchemaType = this.GetOptionType(SwaggerModelType.SWAGGER_MODEL_STRING, "", TFModuleOptionTypeKind.MODULE_OPTION_TYPE_SCHEMA);
    //             option.Discriminator.ExpandFunc = this.GetOptionExpandFunc(option.Discriminator.Type);
    //             option.Discriminator.ValidateFunc = this.GetOptionValidateFunc(option.Discriminator.Type);
    //             option.Discriminator.EnumValues = [];
    //             for (let derivedName of deriveds) {
    //                 let ev:EnumValue = new EnumValue();
    //                 ev.Key = derivedName;
    //                 ev.GoEnumMemberName =ToGoCase(derivedName);
    //                 ev.Value = derivedName;
    //                 option.Discriminator.EnumValues.push(ev);
    //             }
    //             if (this._enumTypes !== null ) this._enumTypes.push(option.Discriminator);
    //         }
    //
    //
    //         for (let derivedName of deriveds) {
    //             if (option instanceof TFDiscriminatorBaseOption) {
    //                 let derivedOption = this.LoadDerivedOption(allderived[derivedName], option, filterFunction);
    //                 if (derivedOption !== null) {
    //                     option.Children.push(derivedOption);
    //                 }
    //             }
    //         }
    //     }
    // }
}
