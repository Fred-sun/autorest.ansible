import {ModuleOption} from "./ModuleOption";
import {ModuleMethod} from "./ModuleMethod";
import {ToSnakeCase} from "../../utils/helper";

export class Module {
    constructor(swaggerName:string, isInfoModule:boolean) {
        this.SwaggerName = swaggerName;
        this.IsInfoModule = isInfoModule;
        this.ObjectName = this.GetObjectName();
        this.ModuleClassName = this.GetModuleClassName();
        this.ModuleName = this.GetModuleName();
        this.ModuleOperationName = ToSnakeCase(swaggerName);
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
    public NeedsDeleteBeforeUpdate: boolean = false;
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
        return false;
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
        for (let method of this.ModuleMethods){
            if (method.Name == methodName)
                return method;
        }
    }

    public SupportsTags():boolean{
        return false;
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
