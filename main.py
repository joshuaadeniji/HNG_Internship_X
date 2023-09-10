from flask import Flask, json, request
import requests
from datetime import datetime

app = Flask(__name__)
file_url = 'https://joshuaadeniji.pythonanywhere.com/user/?user=Joshua%20Adeniji&track=backend/'
response = requests.get(file_url)
today = datetime.now()

@app.route('/user/', methods=['GET'])

def user_page():

    slack_username = str(request.args.get('user'))  # user=Joshua Adeniji
    track = str(request.args.get('track'))  # track=backend

    data_set = {"slack_name": f"{slack_username}",
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