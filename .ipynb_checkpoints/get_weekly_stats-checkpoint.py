import os
from pathlib import Path
from dotenv import load_dotenv

from yfpy.query import YahooFantasySportsQuery


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ENVIRONMENT SETUP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load .env file in order to read local environment variables
load_dotenv()

# set directory location of private.json for authentication
auth_dir = Path(__file__).parent

# set target directory for data output
data_dir = Path(__file__).parent / "output"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# VARIABLE SETUP  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# set desired season year
season = 2022

# set desired Yahoo Fantasy Sports game code
game_code = "nhl"  # NHL

# set desired league ID (see README.md for finding value) - REQUIRED
league_id = "3712"

# set desired Yahoo Fantasy Sports game ID - REQUIRED
game_id = 419 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# QUERY SETUP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# configure the Yahoo Fantasy Sports query (change all_output_as_json_str=True if you want to output JSON strings)
yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_code=game_code,
    game_id=game_id,
    offline=False,
    all_output_as_json_str=False,
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=True
)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# RUN QUERIES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

current_week = yahoo_query.get_league_metadata().current_week

week_array = []
for matchup in yahoo_query.get_league_scoreboard_by_week(current_week).matchups:
    matchup_array = []
    for team in matchup['matchup'].teams:
        # Isolate values we are interested in
        team_dict = {
            'name': team['team'].name.decode(),
            'team_id': team['team'].team_id,
            'score': team['team'].team_points.total
        }
        matchup_array.append(team_dict)
    # Determine winner of the matchup
    winner = max(matchup_array, key=lambda x:x['score'])['team_id']
    for team in matchup_array:
        if team['team_id'] == winner:
            team['result'] = 'W'
        else: 
            team['result'] = 'L'
        week_array.append(team)
print(week_array)