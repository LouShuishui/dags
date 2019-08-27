import requests
import json
submit_url = "http://dltshub.redmond.corp.microsoft.com/api/dlws/postJob?cluster=Azure-EastUS-V100-LowPriority&Team=ads&Email=weouyan@microsoft.com&Key=871c0ee3"
jobParams = {
    "cmd" : "sleep infinity",
    "dataPath" : "",
    "enabledatapath" : True,
    "enablejobpath" : True,
    "enableworkpath" : True,
    "env" : "[ ]",
    "gpuType" : "V100",
    "hostNetwork" : False,
    "image": "indexserveregistry.azurecr.io/zhrui/horizon",
    "is_interactive": True,
    "interactivePorts" : "[40001]",
    "ipython" : True,
    "isParent" : 1,
    "isPrivileged" : False,
    "jobName" : "TestAPISubmission",
    "jobType" : "training",
    "jobtrainingtype" : "RegularJob",
    "preemptionAllowed" : False,
    "resourcegpu": 0,
    "runningasroot": True,
    "ssh" : True,
    "tensorboard" : True,
    "userName" : "weouyan@microsoft.com",
    "vcName" : "ads",
    "workPath" : "weouyan"
}
payload = {}
payload["Json"] = json.dumps(jobParams)
print('url = {}'.format(submit_url))
print('jobparams: type={} value = {}'.format(type(jobParams), jobParams))
print('payload = {}'.format(payload))
r = requests.post(
    url=submit_url,
    data=payload
)
print(r)
