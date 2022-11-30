# -*- coding: utf-8 -*-
"""YFPY demo.

"""
__author__ = "Wren J. R. (uberfastman)"
__email__ = "uberfastman@uberfastman.dev"

import os
from pathlib import Path

from dotenv import load_dotenv

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
season = 2021

# set desired week
chosen_week = 1

# set desired date
chosen_date = "2013-04-15"  # NHL - 2013 (for 2012)

# set desired Yahoo Fantasy Sports game code
game_code = "nfl"  # NFL

# set desired Yahoo Fantasy Sports game ID (see the get_all_yahoo_fantasy_game_keys query to retrieve values)
game_id = 406  # NFL - 2021

# set desired Yahoo Fantasy Sports game key (see the get_all_yahoo_fantasy_game_keys query to retrieve values)
game_key = "406"  # NFL - 2021

# set desired league ID (see README.md for finding value) - REQUIRED
league_id = "413954"  # NFL - 2021

# set desired team ID within desired league
team_id = 1  # NFL

# set desired team name within desired league
team_name = "Legion"  # NFL

# set desired team ID within desired league
player_id = 7200  # NFL: Aaron Rodgers - 2020/2021

# set the maximum number players you wish the get_league_players query to retrieve
league_player_limit = 101

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
yahoo_query.league_key = f"{game_id}.l.{league_id}"

# Manually override player key for example code to work
player_key = f"{game_id}.p.{player_id}"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# RUN QUERIES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print(repr(yahoo_query.get_all_yahoo_fantasy_game_keys()))
print(repr(yahoo_query.get_game_key_by_season(season)))
print(repr(yahoo_query.get_current_game_info()))
print(repr(yahoo_query.get_current_game_metadata()))
print(repr(yahoo_query.get_game_info_by_game_id(game_id)))
print(repr(yahoo_query.get_game_metadata_by_game_id(game_id)))
print(repr(yahoo_query.get_game_weeks_by_game_id(game_id)))
print(repr(yahoo_query.get_game_stat_categories_by_game_id(game_id)))
print(repr(yahoo_query.get_game_position_types_by_game_id(game_id)))
print(repr(yahoo_query.get_game_roster_positions_by_game_id(game_id)))
print(repr(yahoo_query.get_league_key(season)))
# Return User guid
print(repr(yahoo_query.get_current_user()))
# Return all user games
print(repr(yahoo_query.get_user_games()))
print(repr(yahoo_query.get_user_leagues_by_game_key(game_key)))
# Return ALL of users past + present teams
print(repr(yahoo_query.get_user_teams()))

print(repr(yahoo_query.get_league_info()))
print(repr(yahoo_query.get_league_metadata()))
print(repr(yahoo_query.get_league_settings()))
print(repr(yahoo_query.get_league_standings()))
print(repr(yahoo_query.get_league_teams()))
print(repr(yahoo_query.get_league_players(player_count_limit=10, player_count_start=0)))
print(repr(yahoo_query.get_league_draft_results()))
print(repr(yahoo_query.get_league_transactions()))

# These two functions appear to return the same thing
print(repr(yahoo_query.get_league_scoreboard_by_week(chosen_week)))
print(repr(yahoo_query.get_league_matchups_by_week(chosen_week)))

print(repr(yahoo_query.get_team_info(team_id)))
print(repr(yahoo_query.get_team_metadata(team_id)))
# Returns season point total for team
print(repr(yahoo_query.get_team_stats(team_id)))
print(repr(yahoo_query.get_team_stats_by_week(team_id, chosen_week))) # Make this work
# Returns season record for team
print(repr(yahoo_query.get_team_standings(team_id)))
print(repr(yahoo_query.get_team_roster_by_week(team_id, chosen_week)))
print(repr(yahoo_query.get_team_roster_player_info_by_week(team_id, chosen_week)))
# print(repr(yahoo_query.get_team_roster_player_info_by_date(team_id, chosen_date)))  # NHL/MLB/NBA
print(repr(yahoo_query.get_team_roster_player_stats(team_id)))
print(repr(yahoo_query.get_team_roster_player_stats_by_week(team_id, chosen_week)))
print(repr(yahoo_query.get_team_draft_results(team_id)))
print(repr(yahoo_query.get_team_matchups(team_id)))
print(repr(yahoo_query.get_player_stats_for_season(player_key)))
print(repr(yahoo_query.get_player_stats_by_week(player_key, chosen_week)))
# print(repr(yahoo_query.get_player_stats_by_date(player_key, chosen_date)))  # NHL/MLB/NBA
print(repr(yahoo_query.get_player_ownership(player_key)))
print(repr(yahoo_query.get_player_percent_owned_by_week(player_key, chosen_week)))
print(repr(yahoo_query.get_player_draft_analysis(player_key)))
