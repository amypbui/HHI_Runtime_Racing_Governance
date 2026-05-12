import random,time,json
while True:
 data={"lap":random.randint(1,70),"tire_temp":random.randint(70,110),"fuel_level":random.randint(5,100),"weather_risk":round(random.uniform(0,1),2),"confidence":round(random.uniform(0.5,0.99),2)}
 print(json.dumps(data),flush=True)
 time.sleep(2)
