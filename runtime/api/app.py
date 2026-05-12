from flask import Flask, jsonify
app=Flask(__name__)
state={"status":"STABLE","decision_boundary":"ENFORCED","behavioral_drift_score":12,"stop_authority":False}
@app.route("/governance")
def governance():
    return jsonify(state)
@app.route("/drift/<int:score>")
def drift(score):
    state["behavioral_drift_score"]=score
    if score >= 75:
        state["status"]="STOP_AUTHORITY"
        state["stop_authority"]=True
    elif score >= 45:
        state["status"]="ESCALATE"
    else:
        state["status"]="MONITOR"
    return jsonify(state)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)
