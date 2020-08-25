import {ModuleOption} from "./ModuleOption";

export class ModuleMethod {
    public Name: string = null;
    public NameSwagger: string = null;
    public Options: ModuleOption[] = [];
    public RequiredOptions: ModuleOption[] = [];
    public ResponseOptions: ModuleOption[] = [];
    public Url: string = "";
    public HttpMethod: string = "";
    public ApiVersion: string = "";
    public HasBody: boolean = true;
}
