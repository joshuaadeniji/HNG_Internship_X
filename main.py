from flask import *
import requests
from datetime import datetime

app = Flask(__name__)
repo_url = 'https://github.com/joshuaadeniji/hngx_zuri/blob/main/README.md'
response = requests.get(repo_url)
today = datetime.now()

@app.route('/user/', methods=['GET'])
def user_page():

    slack_username = str(request.args.get('user'))  #/username/?user='Joshua_Adeniji'
    track = str(request.args.get('track'))  #/track/?track=backend

    data_set = {"slack_name": f"{slack_username}",
    "current_day": today.strftime('%A'),
    "utc_time": today.utcnow(),
    "track": f"{track}",
    "github_file_url": "https://github.com/joshuaadeniji/hngx_zuri/blob/main/README.md",
    "github_repo_url": "https://github.com/joshuaadeniji/hngx_zuri",
    "status_code": response.status_code}
    
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(debug=1)
