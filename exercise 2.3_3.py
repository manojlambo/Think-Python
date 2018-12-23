"""
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast
"""
start=(6*60+52)*60
easy_pace=(8*60+15)*2
tempo=(7*60+12)*3
hr=(start+easy_pace+tempo)/(60*60)
hr_round=int(hr)
mins=(hr-hr_round)*60
print("Get home for breakfast is %d:%d"%(hr_round,mins))
