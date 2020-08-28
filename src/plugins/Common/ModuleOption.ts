import {Dictionary} from "@azure-tools/linq";
import {ParseType, SwaggerModelType, ToSnakeCase} from "../../utils/helper";

export enum ModuleOptionKind{
    MODULE_OPTION_PATH,
    MODULE_OPTION_BODY,
    MODULE_OPTION_PLACEHOLDER,
    MODULE_OPTION_HEADER,
    MODULE_OPTION_QUERY,
    MODULE_OPTION_RESPONSE
}


export class ModuleOption {
    // constructor(name: string, type:string="", required:boolean=false) {
    //     this.NameSwagger = name;
    //     this.Name = this.NameSwagger;
    //     this.Type = type;
    //     this.Required = required;
    //     this.SubOptions = [];
    //     this.IsList = false;
    //     this.DefaultValue = null;
    //     this.NoLog = false;
    //     this.IncludeInDocumentation = true;
    //     this.IncludeInArgSpec = true;
    // }
    constructor(swaggerOption:any, parent: ModuleOption) {
        this.SwaggerOption = swaggerOption;
        this.Parent = parent;
        this.Init(swaggerOption);
    }
    private Init(swaggerOption:any){
        this.Name = swaggerOption.language.default.name;
        this.NameAnsible = ToSnakeCase(this.Name);
        this.NameSwagger = this.Name;
        this.Required = swaggerOption.required != undefined ? swaggerOption.required : false;
        this.Documentation = swaggerOption.language.default.description;
        this.IncludeInDocumentation = true;
        this.IncludeInArgSpec = true;
        this.ReadOnly = swaggerOption.readOnly == undefined ? false: swaggerOption.readOnly;
        // this.Updatable = swaggerOption.readOnly == undefined ? true: !swaggerOption.readOnly;
        this.LoadSchema(swaggerOption.schema);
        this.LoadProtocal(swaggerOption.protocol);
    }
    private LoadSchema(schema:any){
        this.Type = ParseType(schema.type);
        if (schema.properties != undefined){
            for (let subParameter of schema.properties){
                let subOption = new ModuleOption(subParameter,this);
                this.SubOptions.push(subOption);
            }
        }

        if (schema.type == SwaggerModelType.SWAGGER_MODEL_ARRAY){
            this.ElementType = ParseType(schema.elementType.type);
            if (schema.elementType.type == SwaggerModelType.SWAGGER_MODEL_OBJECT){
                for (let subParameter of schema.elementType.properties){
                    let subOption = new ModuleOption(subParameter,this);
                    this.SubOptions.push(subOption);
                }
            }
        }
    }

    private LoadProtocal(protocol:any){
        if (protocol == undefined)
            return;
        if ( protocol.http != undefined && protocol.http.in != undefined) {
            let location = protocol.http.in;
            if (location == "url") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
            } else if (location == "path") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                this.IncludeInArgSpec = true;
            } else if (location == "body") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
                this.GetDisposition();
                this.IncludeInArgSpec = true;
            } else if (location == "header") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_HEADER;
            } else if (location === "query") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_QUERY;
            } else {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                this.IncludeInArgSpec = true;
            }
        } else {
            this.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
            this.GetDisposition();
            this.IncludeInArgSpec = true;
        }
    }

    private GetDisposition(){
        if (this.Parent == null || this.Parent == undefined){
            if (this.NameSwagger == 'location' || this.NameSwagger =='tags' ||
                this.NameSwagger == 'identity' ||  this.NameSwagger == 'sku'){
                this.DispositionRest =  "/"+this.NameSwagger;
            }
            else
                this.DispositionRest =  "/properties/"+this.NameSwagger;
            this.DispositionSdk = "/"+ToSnakeCase(this.NameSwagger);
        }else {
            this.DispositionSdk = ToSnakeCase(this.NameSwagger);
            this.DispositionRest =   this.NameSwagger;
        }
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
    public SubOptions: ModuleOption[] = [];
    public NameAnsible: string = null;
    public ExampleValue: string = null;
    public Hidden: boolean;
    public DispositionSdk: string = null;
    public EnumValues: Dictionary<any>[];
    public Comparison: string = null;
    public Updatable: boolean = true;
    public DispositionRest: string = null;
    public NamePythonSdk: string = null;
    public Kind:ModuleOptionKind;
    public SwaggerPath: string[]= [];
    public Computed: boolean;
    public ElementType: string = null;
    public SwaggerOption: any;
    public Parent: ModuleOption;

}
