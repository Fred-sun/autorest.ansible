var url = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/";
var reg = /{([^{}]*)}/g;
var result;
// result = reg.(url);
// console.log(result);
while ((result = reg.exec(url)) != null) {
    console.log(result[1]);
}
