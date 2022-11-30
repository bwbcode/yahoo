# -*- coding: utf-8 -*-

import os
from pathlib import Path

from dotenv import load_dotenv

import json

from yfpy import Data
from yfpy.query import YahooFantasySportsQuery

"""
Example public Yahoo league URL: "https://archive.fantasysports.yahoo.com/nfl/2014/729259"

Example vars using public Yahoo leagues still require auth through a personal Yahoo account: see README.md
"""



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ENVIRONMENT SETUP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# load .env file in order to read local environment variables
load_dotenv()

# set directory location of private.json for authentication
auth_dir = Path(__file__).parent

# set target directory for data output
data_dir = Path(__file__).parent / "output"

# create YFPY Data instance for saving/loading data
data = Data(data_dir)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# VARIABLE SETUP  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# set desired season year
season = 2022

# set desired week
# chosen_week = 1

# set desired Yahoo Fantasy Sports game code
# game_code = "nfl"  # NFL
game_code = "nhl"  # NHL

# set desired league ID (see README.md for finding value)
league_id = "3712"

# set desired date
# chosen_date = "2013-04-15"  # NHL - 2013 (for 2012)
# chosen_date = "2013-04-16"  # NHL - 2013
# chosen_date = "2021-10-25"  # NHL - 2021
# chosen_date = "2021-04-01"  # MLB - 2021
# chosen_date = "2022-04-10"  # MLB - 2022

# set desired Yahoo Fantasy Sports game ID (see the get_all_yahoo_fantasy_game_keys query to retrieve values)
game_id = 419  # NFL - 2014


# set desired Yahoo Fantasy Sports game key (see the get_all_yahoo_fantasy_game_keys query to retrieve values)
game_key = "419"  # NFL - 2014


# set desired team ID within desired league
# team_id = 1  # NFL

# set desired team name within desired league
# team_name = "Legion"  # NFL

# set desired team ID within desired league
# player_id = 7200  # NFL: Aaron Rodgers - 2020/2021

# set the maximum number players you wish the get_league_players query to retrieve
#league_player_limit = 101
# league_player_limit = 2610

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# QUERY SETUP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# configure the Yahoo Fantasy Sports query (change all_output_as_json_str=True if you want to output JSON strings)
yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_id=game_id,
    game_code=game_code,
    offline=False,
    all_output_as_json_str=False,
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=True
)

# Manually override league key for example code to work
# yahoo_query.league_key = f"{game_id}.l.{league_id}"

# Manually override player key for example code to work
# player_key = f"{game_id}.p.{player_id}"

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