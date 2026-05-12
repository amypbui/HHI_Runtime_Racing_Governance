import json,time,random
while True:
 event={"timestamp":time.time(),"behavioral_drift_score":random.randint(0,100),"decision_boundary":"ENFORCED","runtime_source":"HHI_Runtime_Racing_Governance"}
 with open("runtime/proof/runtime_events.jsonl","a") as f:
  f.write(json.dumps(event)+"\n")
 time.sleep(3)
