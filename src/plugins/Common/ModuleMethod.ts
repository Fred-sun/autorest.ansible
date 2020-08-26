import {ModuleOption, ModuleOptionKind} from "./ModuleOption";

export class ModuleMethod {
    constructor(swaggerMethod: any) {
        this.SwaggerMethod = swaggerMethod;
        this.Init(swaggerMethod);
    }

    private Init(swaggerMethod: any){
        this.Name = swaggerMethod.language.default.name;
        if (swaggerMethod.requests[0].protocol != undefined && swaggerMethod.requests[0].protocol.http != undefined) {
            this.Url = (swaggerMethod.requests[0].protocol.http.path != undefined) ? swaggerMethod.requests[0].protocol.http.path : "";
            this.HttpMethod = (swaggerMethod.requests[0].protocol.http.method != undefined) ? swaggerMethod.requests[0].protocol.http.method : "";
        }
        this.LoadOption(swaggerMethod.parameters);
        if (swaggerMethod.requests[0].parameters !== undefined) {
            this.HasBody = true;
            this.LoadOption(swaggerMethod.requests[0].parameters);
        }else
            this.HasBody = false;

    }

    private LoadOption(parameters: any){
        for (let parameter of parameters){
            let option = new ModuleOption(parameter, null);
            if (option.Name.charAt(0) == '_' && option.Kind == ModuleOptionKind.MODULE_OPTION_BODY){
                this.ParameterName = option.Name.substr(1);
            }
            if (this.IsAnsibleIgnoredOption(option.Name)){
                continue;
            }
            this.Options.push(option);
            if (option.Required){
                this.RequiredOptions.push(option);
            }
        }
    }
    private IsAnsibleIgnoredOption(name: string) : boolean
    {
        let ignoreOptions = new Set(['Apiversion','SubscriptionId', 'ApiVersion','subscriptionId', 'content_type','ContentType']);
        return name.indexOf('$') != -1 || name.indexOf('_') != -1 || ignoreOptions.has(name);
    }
    public Name: string = null;

    public Options: ModuleOption[] = [];
    public RequiredOptions: ModuleOption[] = [];
    public ResponseOptions: ModuleOption[] = [];
    public Url: string = "";
    public SwaggerMethod: any;
    public HttpMethod: string = "";
    public ApiVersion: string = "";
    public HasBody: boolean = false;
    public ParameterName: string = "parameters";
}
