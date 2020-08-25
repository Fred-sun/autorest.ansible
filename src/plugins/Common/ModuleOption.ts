import {Dictionary} from "@azure-tools/linq";

export enum ModuleOptionKind{
    MODULE_OPTION_PATH,
    MODULE_OPTION_BODY,
    MODULE_OPTION_PLACEHOLDER,
    MODULE_OPTION_HEADER,
    MODULE_OPTION_QUERY,
    MODULE_OPTION_RESPONSE
}


export class ModuleOption {
    constructor(name: string, type:string="", required:boolean=false) {
        this.NameSwagger = name;
        this.Name = this.NameSwagger;
        this.Type = type;
        this.Required = required;
        this.SubOptions = [];
        this.IsList = false;
        this.DefaultValue = null;
        this.NoLog = false;
        this.IncludeInDocumentation = true;
        this.IncludeInArgSpec = true;
    }
    public NameSwagger: string = null;
    public Name: string = null;

    //Model type name.
    public NameInModelSchema: string = null;

    public IdPortion: string = null;
    public Type: string = null;
    public ItemType: string = null;

    //indicate if the option is an arry
    public IsList: boolean = false;
    //indicate if the option is a map
    public IsMap: boolean = false;

    public Required: boolean = false;
    public ReadOnly: boolean = false;
    public Documentation: string = null;
    public DefaultValue: string = null;
    public IncludeInDocumentation: boolean = false;
    public IncludeInArgSpec: boolean = false;
    public NoLog: boolean = false;
    public SubOptions: ModuleOption[] = null;
    public NameAnsible: string = null;
    public ExampleValue: string = null;
    public Hidden: boolean;
    public DispositionSdk: string = null;
    public EnumValues: Dictionary<any>[];
    public Comparison: string = null;
    public Updatable: boolean;
    public DispositionRest: string = null;
    public NamePythonSdk: string = null;
    public Kind:ModuleOptionKind;
    public SwaggerPath: string[]= [];
    public Computed: boolean;


}
