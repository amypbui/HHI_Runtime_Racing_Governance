from flask import Flask, jsonify
from runtime.explainability.explainer import explain
import random,time
app=Flask(__name__)
@app.route("/governance")
def governance():
 telemetry={"lap":random.randint(1,70),"tire_temp":random.randint(70,110),"fuel_level":random.randint(5,100),"weather_risk":round(random.uniform(0,1),2),"confidence":round(random.uniform(0.5,0.99),2)}
 governance_state=explain(telemetry)
 return jsonify({"timestamp":time.time(),"telemetry":telemetry,"governance":governance_state,"decision_boundary":"ENFORCED","human_override":"AVAILABLE"})
if __name__ == "__main__":
 app.run(host="0.0.0.0",port=8000)
