from flask import Flask, url_for, render_template, request
import datetime
from datetime import timedelta

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    #Store possible races in the race dictionary
    races = {
        "fifteenHundred": 1500,
        "1Mile": 1609,
        "threeK": 3000,
        "3mile": 4828,
        "fiveK": 5000,
        "tenK": 10000,
        "halfMarathon": 21097,
        "Marathon": 42195
    }
    #Store readable string equivalent names for the races
    raceResponse = {
        "fifteenHundred": "1500M",
        "1Mile": "1 Mile",
        "threeK": "3K",
        "3mile": "3 Mile",
        "fiveK": "5K",
        "tenK": "10K",
        "halfMarathon": "Half Marathon",
        "Marathon": "Marathon"
    }

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
                
        for i in races: #Loop through to find target race
            if target == i: #If the target race matches key \/
                d2 = races[i] #set the value of d2 as the target race 
                for j in races: #Then loop through races again to find the matching user entered race
                    if race1 == j: #If the race is found
                        t2 = t1 * ((d2 / races[j]) * 1.06) #Calculate using the value of the selected key
                        prediction = str(datetime.timedelta(seconds=t2)) #Set prediction as the time converted to a string in HH:MM::SS
            else:
                pass #Do nothing

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
        t1 = r1Sec + (r1Min * 60) + (r1Hr * 3600) #Convert the entered time to seconds stored as t1
        t2 = r2Sec + (r2Min * 60) + (r2Hr * 3600) #Convert the entered time for race 2 to seconds stored as t2
        d2 = 0
        t3 = 0
        t4 = 0
        tFinal = 0
        
        for i in races: #Loop through races to find target race
            if target == i: #If the target race matches the key \/
                d2 = races[i] #set d2 equal to the matching value of the key
                for j in races: #Loop through races again to find race 1
                    if race1 == j: #If race 1 is found \/
                        t3 = t1 * ((d2 / races[j]) * 1.06) #Calculate the predicted time based off of race 1 time and distance
                        for k in races: #Loop through races again to find race 2
                            if race2 == k: #If race 2 is found \/
                                t4 = t2 * ((d2 / races[k]) * 1.06) #Calculate the prediction based off of race 2 time and distance
                                tFinal = (t3 + t4) / 2 #Average the two predictions 
                                prediction = str(datetime.timedelta(seconds=tFinal)) #Set prediction to the predicted times as a string in HH:MM:SS
            else:
                pass #Do nothing

    
    #Convert the name of the race to a readable version which is returned
    for x in raceResponse:
        if target == x:
            targetRace = raceResponse[x]
        else:
            pass

    return render_template('response.html', response1 = prediction, response2 = targetRace)
    
if __name__=="__main__":
    app.run(debug=False)