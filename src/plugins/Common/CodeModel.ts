import {MapModuleGroup, ModuleMethod, ModuleOption} from "./ModuleMap";
import {LogCallback} from "../../index";

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
    constructor() {
    }
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

    public HasCreateOrUpdate(): boolean{
        return true;
    }

    public HasResourceGroup(): boolean{
        return true;
    }
    public ModuleObjectName(): string
    {
        // XXX - handle following rules
        // Nat --> NAT
        // I P --> IP
        // Sql --> SQL

        let name: string = this.ModuleName;

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
        return null;
    }
    public GetModuleClassName(){
        return "AzureRM" + this.ObjectName;
    }
}


