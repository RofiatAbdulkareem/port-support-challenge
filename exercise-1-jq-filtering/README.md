Based on the Kubernetes and Jira JSON examples shared, i have written the appropriate JQ filters to extract the data.

1. **Current Replica Count**

```bash
.spec.replicas 

```
The above code navigates to the replicas field under the spec section and returns the number of pods, which in our case **1**

2. **The deployment strategy**
```bash
.spec.strategy.type

```
The above code reaches to the deployment's strategy object and pulls out the type which in our case **RollingUpdate**

3. **Service label + environment label**

```bash
.metadata.labels | "\(.service)-\(.environment)"

```
The above code uses JQ interpolation to combine the values of the service and environment labels with an hyphen in between. Result is **authorization-production-gcp-1**

4. **JIRA-API issue response**
```bash
.fields.subtasks[].key
```
The above code loops over all subtasks and grabs their key values, wrapping them in an array. An example will be 
**["SAMPLE-3894","SAMPLE-3895", "SAMPLE-3896""]**