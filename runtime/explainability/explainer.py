def explain(data):
 reasons=[]
 if data["tire_temp"] > 95:
  reasons.append("Tire degradation risk increasing")
 if data["weather_risk"] > 0.7:
  reasons.append("Weather volatility threshold exceeded")
 if data["confidence"] < 0.65:
  reasons.append("AI confidence instability detected")
 status="ESCALATE" if reasons else "STABLE"
 return {"status":status,"reasons":reasons}
