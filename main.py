from flask import Flask, json, request
import requests
from datetime import datetime

app = Flask(__name__)
file_url = 'https://joshuaadeniji.pythonanywhere.com/api/?slack_name=Josh&track=backend/'
response = requests.get(file_url)
today = datetime.now()

@app.route('/api/', methods=['GET'])

def user_page():

    slack_name = str(request.args.get('slack_name'))  # slack_name=Josh
    track = str(request.args.get('track'))  # track=backend

    data_set = {"slack_name": f"{slack_name}",
    "current_day": today.strftime('%A'),
    "utc_time": today.utcnow(),
    "track": f"{track}",
    "github_file_url": "https://github.com/joshuaadeniji/HNG_Internship_X/blob/main/main.py",
    "github_repo_url": "https://github.com/joshuaadeniji/HNG_Internship_X",
    "status_code": response.status_code}

    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7000)