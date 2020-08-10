
export class ModuleMap {
    constructor() {

    }
    public ModuleName: string = null;
    public NameSwagger: string = null;
    public Methods: ModuleMethod[] = null;

    public ObjectName: string = null;
}
export class ModuleMethod {
    public Name: string = null;
    public NameSwagger: string = null;
    public Options: ModuleOption[] = [];
    public RequiredOptions: ModuleOption[] = [];
    public ResponseOptions: ModuleOption[] = [];
    public Url: string = "";
    public HttpMethod: string = "";
}

export class ModuleOption {
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
    public Readonly: boolean = false;
    public Documentation: string = null;
    public DefaultValue: string = null;
    public IncludeInDocumentation: boolean = false;
    public IncludeInArgSpec: boolean = false;
    public NoLog: boolean = false;
    public SubOptions: ModuleOption[] = null;
}
export class MapModuleGroup {
    public Modules: ModuleMap[] = [];
}
