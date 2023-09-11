from flask import Flask, request, jsonify
# import json
import requests
from datetime import datetime

app = Flask(__name__)

file_url = 'https://joshuaadeniji.pythonanywhere.com/api?slack_name=Josh&track=backend/'
response = requests.get(file_url)
today = datetime.now()

@app.route('/api', methods=['GET'])

def user_page():

    slack_name = str(request.args.get('slack_name'))  # slack_name=Josh
    track = str(request.args.get('track'))  # track=backend

    data_set = {
    "slack_name": f"{slack_name}",
    "current_day": today.strftime('%A'),
    "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
    "track": f"{track}",
    "github_file_url": "https://github.com/joshuaadeniji/HNG_Internship_X/blob/main/main.py",
    "github_repo_url": "https://github.com/joshuaadeniji/HNG_Internship_X",
    "status_code": int(response.status_code)
    }

    return jsonify(data_set)

if __name__ == '__main__':
    app.run(port=7070)
