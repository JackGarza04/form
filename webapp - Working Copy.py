from flask import Flask, url_for, render_template, request
import datetime
from datetime import timedelta

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    #If the user does not include a time for the optional field, do not use it to compute
    if(request.args['pastRaceHr2'] == "" and request.args['pastRaceMin2'] == "" and request.args['pastRaceSec2'] == ""):
        #variables assigned to information used for calculations
        target = request.args['targetRace']
        race1 = request.args['pastRace']
        r1Hr = int(request.args['pastRaceHr'])
        r1Min = int(request.args['pastRaceMin'])
        r1Sec = int(request.args['pastRaceSec'])
        t1 = r1Sec + (r1Min * 60) + (r1Hr * 3600)
        d2 = 0
        t2 = 0
        #assigns d2 (desired distance) to equivalent value in meters
        if(target == "fifteenHundred"):
            d2 = 1500
        elif(target == "1Mile"):
            d2 = 1609
        elif(target == "threeK"):
            d2 = 3000
        elif(target == "3mile"):
            d2 = 4828
        elif(target == "fiveK"):
            d2 = 5000
        elif(target == "tenK"):
            d2 = 10000
        elif(target == "halfMarathon"):
            d2 = 21097
        elif(target == "Marathon"):
            d2 = 42195
            
        #checks which race the user selects and proceeds with that distance in mind
        if(race1 == "fifteenHundred"):
            t2 = t1 * ((d2 / 1500) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "1Mile"):
            t2 = t1 * ((d2 / 1609) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "threeK"):
            t2 = t1 * ((d2 / 3000) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "3mile"):
            t2 = t1 * ((d2 / 4828) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "fiveK"):
            t2 = t1 * ((d2 / 5000) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "tenK"):
            t2 = t1 * ((d2 / 10000) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "halfMarathon"):
            t2 = t1 * ((d2 / 21097) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(race1 == "Marathon"):
            t2 = t1 * ((d2 / 42195) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        else:
            prediction = "Unable to predict. Try again."
    #if the user inputs a time for the second data point, calculate including it
    else:
        target = request.args['targetRace']
        race1 = request.args['pastRace']
        r1Hr = int(request.args['pastRaceHr'])
        r1Min = int(request.args['pastRaceMin'])
        r1Sec = int(request.args['pastRaceSec'])
        race2 = request.args['pastRace2']
        r2Hr = int(request.args['pastRaceHr2'])
        r2Min = int(request.args['pastRaceMin2'])
        r2Sec = int(request.args['pastRaceSec2'])
        t1 = r1Sec + (r1Min * 60) + (r1Hr * 3600)
        t2 = r2Sec + (r2Min * 60) + (r2Hr * 3600)
        d2 = 0
        d3 = 0
        t3 = 0
        t4 = 0
        tAvg = 0
        
        #set the desired race as d2
        if(target == "fifteenHundred"):
            d2 = 1500
        elif(target == "1Mile"):
            d2 = 1609
        elif(target == "threeK"):
            d2 = 3000
        elif(target == "3mile"):
            d2 = 4828
        elif(target == "fiveK"):
            d2 = 5000
        elif(target == "tenK"):
            d2 = 10000
        elif(target == "halfMarathon"):
            d2 = 21097
        elif(target == "Marathon"):
            d2 = 42195
            
        #set the second race as d3
        if(race2 == "fifteenHundred"):
            d3 = 1500
        elif(race2 == "1Mile"):
            d3 = 1609
        elif(race2 == "threeK"):
            d3 = 3000
        elif(race2 == "3mile"):
            d3 = 4828
        elif(race2 == "fiveK"):
            d3 = 5000
        elif(race2 == "tenK"):
            d3 = 10000
        elif(race2 == "halfMarathon"):
            d3 = 21097
        elif(race2 == "Marathon"):
            d3 = 42195
            
        #check against the first race given and calculate
        if(race1 == "fifteenHundred"):
            t3 = t1 * ((d2 / 1500) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "1Mile"):
            t3 = t1 * ((d2 / 1609) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "threeK"):
            t3 = t1 * ((d2 / 3000) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "3mile"):
            t3 = t1 * ((d2 / 4828) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "fiveK"):
            t3 = t1 * ((d2 / 5000) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "tenK"):
            t3 = t1 * ((d2 / 10000) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "halfMarathon"):
            t3 = t1 * ((d2 / 21097) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        elif(race1 == "Marathon"):
            t3 = t1 * ((d2 / 42195) * 1.06)
            t4 = t2 * ((d2 / d3) * 1.06)
            tAvg = (t3 + t4) / 2
            prediction = str(datetime.timedelta(seconds=tAvg))
        else:
            prediction = "Unable to predict. Try again."
            
    #Convert the value of the target race to a readable equivalent that displays on the response page
    if(target == "fifteenHundred"):
        targetRace = "1500M"
    elif(target == "1Mile"):
        targetRace = "1 Mile"
    elif(target == "threeK"):
        targetRace = "3K"
    elif(target == "3mile"):
        targetRace = "3 Mile"
    elif(target == "fiveK"):
        targetRace = "5K"
    elif(target == "tenK"):
        targetRace = "10K"
    elif(target == "halfMarathon"):
        targetRace = "Half Marathon"
    elif(target == "Marathon"):
        targetRace = "Marathon"
    
    return render_template('response.html', response1 = prediction, response2 = targetRace)
    
if __name__=="__main__":
    app.run(debug=False)