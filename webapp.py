from flask import Flask, url_for, render_template, request
from datetime import timedelta

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    if(request.args['pastRaceHr2'] == "" and request.args['pastRaceMin2'] == "" and request.args['pastRaceSec2'] == ""):
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
            

        if(target == "fifteenHundred"):
            t2 = t1 * ((1500 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "1Mile"):
            t2 = t1 * ((1609 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "threeK"):
            t2 = t1 * ((3000 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "3mile"):
            t2 = t1 * ((4828 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "fiveK"):
            t2 = t1 * ((5000 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "tenK"):
            t2 = t1 * ((10000 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "halfMarathon"):
            t2 = t1 * ((21097 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        elif(target == "Marathon"):
            t2 = t1 * ((42195 / d2) * 1.06)
            prediction = str(datetime.timedelta(seconds=t2))
        else:
            prediction = "Unable to predict. Try again."
    else:
        pass
        # target = request.args['targetRace']
        # race1 = request.args['pastRace']
        # r1Hr = int(request.args['pastRaceHr'])
        # r1Min = int(request.args['pastRaceMin'])
        # r1Sec = int(request.args['pastRaceSec'])
        # race2 = request.args['pastRace2']
        # r2Hr = int(request.args['pastRaceHr2'])
        # r2Min = int(request.args['pastRaceMin2'])
        # r2Sec = int(request.args['pastRaceSec2'])
    
    return render_template('response.html', response1 = prediction, response2 = target)
    
if __name__=="__main__":
    app.run(debug=False)