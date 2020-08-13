import {MapModuleGroup, ModuleMethod, ModuleOption} from "./ModuleMap";
import {LogCallback} from "../../index";
import {ToSnakeCase} from "../../utils/helper";

export enum SwaggerModelType {
    SWAGGER_MODEL_ANY = "any",
    SWAGGER_MODEL_OBJECT = "object",
    SWAGGER_MODEL_ARRAY = "array",
    SWAGGER_MODEL_ENUM = "choice",
    SWAGGER_MODEL_CONSTENT = "constant",
    SWAGGER_MODEL_DICTIONARY = "dictionary",
    SWAGGER_MODEL_DATETIEM = "date-time",
    SWAGGER_MODEL_DURATION = "duration",
    SWAGGER_MODEL_UUID = "uuid",
    SWAGGER_MODEL_BYTE_ARRAY = "byte-array",
    /*number type */
    SWAGGER_MODEL_INTEGER = "integer",
    SWAGGER_MODEL_INTEGER_32 = "integer32",
    SWAGGER_MODEL_INTEGER_64 = "integer64",
    SWAGGER_MODEL_FLOAT = "float",
    SWAGGER_MODEL_DOUBLE = "double",
    SWAGGER_MODEL_STRING = "string",
    SWAGGER_MODEL_BOOLEAN = "boolean",
    SWAGGER_MODEL_NUMBER = "number"
}


export class CodeModel {
    constructor(swaggerName:string, isInfoModule:boolean) {
        this.SwaggerName = swaggerName;
        this.IsInfoModule = isInfoModule;
        this.ObjectName = this.GetObjectName();
        this.ModuleClassName = this.GetModuleClassName();
        this.ModuleName = this.GetModuleName();
        this.ModuleOperationName = swaggerName.toLowerCase();
    }
    public SwaggerName: string = null;
    public ModuleName: string = null;
    public PythonNamespace: string = null;
    public PythonMgmtClient: string = null;
    public ModuleClassName: string = null;
    public ModuleOptions: ModuleOption[] = [];
    public ModuleApiVersion: string = null;
    public MgmtClientName: string = null;
    public ModuleMethods: ModuleMethod[] = [];
    public ObjectName: string = null;
    public BasicURL: string = null;
    public LocationDisposition: string = null;
    public DeleteResponseNoLogFields: string[] = [];
    public ResponseFieldStatements: string[] = [];
    public NeedsDeleteBeforeUpdate: boolean;
    public NeedsForceUpdate: boolean;
    public ModuleOperationName: string = null;
    public ModuleUrl: string = null;
    public ObjectNamePythonized: string = null;
    public ModuleResponseFields: ModuleOption[] = [];
    public IsInfoModule: boolean = false;
    public HasCreateOrUpdate(): boolean{
        return true;
    }

    public HasResourceGroup(): boolean{
        return true;
    }
    public GetObjectName(): string
    {
        // XXX - handle following rules
        // Nat --> NAT
        // I P --> IP
        // Sql --> SQL

        let name: string = this.SwaggerName;

        if (name.endsWith("ies"))
        {
            name = name.substring(0, name.length - 3) + "y";
        }
        else if (name.toLowerCase().endsWith("xes"))
        {
            name = name.substring(0, name.length - 2);
        }
        else if (name.endsWith('s'))
        {
            name = name.substring(0, name.length - 1);
        }

        return name;
    }

    public GetMethod(methodName:string): ModuleMethod{
        return null;
    }

    public SupportsTags():boolean{
        return true;
    }

    public GetMethodOptions(methodName:string, bo:boolean):ModuleOption[]{
        for (let method of this.ModuleMethods){
            if (methodName == method.Name)
                return method.Options;
        }
        return null;
    }
    public GetModuleClassName(){
        if (this.IsInfoModule)
            return "AzureRM" + this.ObjectName +"Info";
        else
            return "AzureRM" + this.ObjectName;
    }

    public GetModuleName(){
        if (this.IsInfoModule)
            return "azure_rm_"+this.ObjectName.toLowerCase()+"_info";
        else
            return "azure_rm_"+this.ObjectName.toLowerCase();
    }

    public ModuleOptionExist(name: string):boolean{
        for (let option of this.ModuleOptions){
            if (option.Name == name)
                return true;
        }
        return false;
    }
}


