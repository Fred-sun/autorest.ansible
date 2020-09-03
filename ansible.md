# autorest.ansible doc

## User Guide

### Preparation

#### 1. install the autorest 

```
npm install -g autorest 
```
**ps:** If there is not npm and node installed in your computer, you should first install them. 
	
The node and npm version in my machine:
	
```
node -v
v12.18.3
	
npm -v
6.14.6
```
other versions may work as well, please check  
	```https://github.com/Azure/autorest``` for more information about suppported versions of node 
	
After installation, please check whether the autorest runs well

```
autorest --help 
```

If there is not failure in the console , it is very lucky for you, then you can go to the next step.

But if  something wrong happens, you can first google for some solutions. And if it still doesn't work at the end, maybe you need to launch a virtural machine in the azure( or other cloud service providers) , and set up the environment in it, just like me.
	


	
#### 2. clone the api spec
```
git clone https://github.com/Azure/azure-rest-api-specs.git
```
	
#### 3. install the typescript

```
npm install -g typescript
```


#### 4. clone the ansible repo 
	
``` 
https://github.com/GuopengLin/autorest.ansible.git
```


#### 5. install the module dependence

```
cd [path of autorest.ansible]

npm install 

```
#### 6. compile

```
tsc -p .
```
#### 7. run

```
autorest --ansible --use=./  [path or README.md]   --ansible-output-folder=[output-dir-path]

eg:
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/compute/resource-manager/readme.md  --log --ansible-output-folder=./tmp
```

### Usage

If all the preparations have been done, now you can generate any modules you like.

Eg:
	
1. generate modules of the compute client:
	```
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/compute/resource-manager/readme.md  --log --ansible-output-folder=./tmp
	```
2. generate modules of the authorization client:
	```
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/authorization/resource-manager/readme.md  --log --ansible-output-folder=./tmp
	```
	 
There will be a azure_rm_usage or azure_rm_sku module in the tmp directory which i  think  is unuseful,but i still keep it in the code.You can choose the modules you want and delete the others.

## Developer Guide

### 1. preparation

I have to assume that you have konwn about how to use the autorest.ansible to generate modules.

If so, you can go to the next step.



