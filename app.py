from flask import Flask, jsonify
from InformationPrinting import *
app = Flask(__name__)

@app.route('/')
def cricgfg():
    try:
        result = {
            "Description": description,
            "Location": location,
            "Status": status,
            "Current": current,
            "Team A": team1_name,
            "Team A Score": team1_score,
            "Team B": team2_name,
            "Team B Score": team2_score,
            "Full Score Board": link,
            "Credits": "NDTV Sports News"
            }
    except:
        pass
    return jsonify(result)



if __name__ == "__main__":

    app.run(debug=True)



