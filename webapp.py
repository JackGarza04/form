from flask import Flask, url_for, render_template, request
import datetime
from datetime import timedelta

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    #if(request.args['pastRaceHr2'] == "" and request.args['pastRaceMin2'] == "" and request.args['pastRaceSec2'] == ""):
    target = request.args['targetRace']
    race1 = request.args['pastRace']
    r1Hr = int(request.args['pastRaceHr'])
    r1Min = int(request.args['pastRaceMin'])
    r1Sec = int(request.args['pastRaceSec'])
    t1 = r1Sec + (r1Min * 60) + (r1Hr * 3600)
    t2 = 0
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
    #else:
        # target = request.args['targetRace']
        # race1 = request.args['pastRace']
        # r1Hr = int(request.args['pastRaceHr'])
        # r1Min = int(request.args['pastRaceMin'])
        # r1Sec = int(request.args['pastRaceSec'])
        # race2 = request.args['pastRace2']
        # r2Hr = int(request.args['pastRaceHr2'])
        # r2Min = int(request.args['pastRaceMin2'])
        # r2Sec = int(request.args['pastRaceSec2'])
    
    return render_template('response.html', racePrediction = prediction, targetRace = target)
    
if __name__=="__main__":
    app.run(debug=False)