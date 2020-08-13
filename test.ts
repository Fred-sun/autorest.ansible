let url = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/";
let reg = /{([^{}]*)}/g
let result;
// result = reg.(url);
// console.log(result);
while ((result = reg.exec(url)) != null){
    console.log(result[1]);
}
