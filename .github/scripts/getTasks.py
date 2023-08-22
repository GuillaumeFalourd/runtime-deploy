import os
import json

output_file = os.getenv('GITHUB_OUTPUT')
WORKSPACE = os.getenv("WORKSPACE")

file=f"{WORKSPACE}/tasks.json"
# Opening JSON file
f = open('file')
 
# returns JSON object as
# a dictionary
data = json.load(f)

run_task_ids=[]

for task in data["tasks"]:
  run_task_ids.append(task['runTaskId'])
  print("Run Task Ids:", run_task_ids)
    
with open(output_file, "a") as myfile:
    myfile.write(f"tasks={run_task_ids}")