from jq import jq
import json

with open("/home/medhat/temp/asset_1258682.json") as f:
    asset_json = json.load(f)

jq_output = jq(".properties[10].associatedNode.properties[] | select(.id == 3938590526)").transform(asset_json)

# print("#####################################################")
# print("################### Python Object ###################")
# print("#####################################################")
#
# print(jq_output)
#
# print("#####################################################")
# print("################### JSON Object #####################")
# print("#####################################################")

print(json.dumps(jq_output))
