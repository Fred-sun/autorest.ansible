import { AutoRestExtension, Channel, Host } from "@azure-tools/autorest-extension-base";


export type LogCallback = (message: string) => void;
export type FileCallback = (path: string, rows: string[]) => void;



export async function main() {
    const extension = new AutoRestExtension();
    extension.Add("ansible", async autoRestApi => {
        let log = await autoRestApi.GetValue("log");
        function Info(s: string)
        {
            if (log)
            {
                autoRestApi.Message({
                    Channel: Channel.Information,
                    Text: s
                });
            }
        }

        function WriteFile(path: string, rows: string[])
        {
            autoRestApi.WriteFile(path, rows.join('\r\n'));
        }
        const inputFileUris = await autoRestApi.ListInputs();
        Info("input file:" + inputFileUris);
        const inputFiles: string[] = await Promise.all(inputFileUris.map(uri => autoRestApi.ReadFile(uri)));
        Info("AutoRest offers the following input files: " + inputFiles.join("\n---\n"));
        autoRestApi.WriteFile("concat.txt", inputFiles.join("\n---\n"));
    });
    extension.Run();
}

main();
