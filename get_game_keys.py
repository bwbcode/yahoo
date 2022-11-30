import os
from pathlib import Path

import json
from dotenv import load_dotenv

from yfpy.query import YahooFantasySportsQuery

# load .env file in order to read local environment variables
load_dotenv()

# set directory location of private.json for authentication
auth_dir = Path(__file__).parent

# set league_id - this value is mandatory for yahoo query
league_id = "13405"

yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    offline=False,
    all_output_as_json_str=False, # change all_output_as_json_str=True if you want to output JSON strings
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=True
)

# Create an array of extracted game dictionaries
games = []
for row in yahoo_query.get_user_games():
    games.append(row['game'].__dict__['extracted_data'])

json_string = json.dumps({
    'games': games
})

with open('json_db/game_keys.json', 'w') as f:
    f.write(json_string)