import {ModuleOption} from "./ModuleOption";

export class ModuleExampleParameter {
    constructor(name: string, content: string) {
        this.Name = name;
        this.ParseContent(content);
    }

    private ParseContent(content: any){
        if (content instanceof Array){
            for (let item of content){

            }
        }
    }

    public Name:string = null;
    public Type: string = null;
    public Value: string = null;
    public SubParameters : ModuleExampleParameter[] = [];
}
