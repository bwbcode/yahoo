# -*- coding: utf-8 -*-

import os
from pathlib import Path

from dotenv import load_dotenv

import json
import pandas as pd
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

team_id = 1
# set desired week
chosen_week = 13

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


#print(repr(yahoo_query.get_current_game_info()))
#print(repr(yahoo_query.get_current_game_metadata()))

#print(repr(yahoo_query.get_game_info_by_game_id(game_id)))
#print(repr(yahoo_query.get_game_metadata_by_game_id(game_id)))
#print(repr(yahoo_query.get_game_stat_categories_by_game_id(game_id)))
#print(repr(yahoo_query.get_game_position_types_by_game_id(game_id)))
#print(repr(yahoo_query.get_game_roster_positions_by_game_id(game_id)))

# print(repr(yahoo_query.get_league_key(season)))
# print(repr(yahoo_query.get_user_teams()))

#print(repr(yahoo_query.get_league_info()))

# print(repr(yahoo_query.get_league_settings()))
# print(repr(yahoo_query.get_league_standings()))
# print(repr(yahoo_query.get_league_teams()))

#data = yahoo_query.get_league_scoreboard_by_week(chosen_week)
#print(repr(yahoo_query.get_league_matchups_by_week(chosen_week)))

# print(repr(yahoo_query.get_team_info(team_id)))

# # print(repr(yahoo_query.get_team_roster_player_info_by_date(team_id, chosen_date)))  # NHL/MLB/NBA


# print(repr(yahoo_query.get_team_draft_results(team_id)))
# print(repr(yahoo_query.get_team_matchups(team_id)))

# print(repr(yahoo_query.get_player_stats_for_season(player_key)))
#print(repr(yahoo_query.get_player_stats_by_week(player_key, chosen_week)))
# # print(repr(yahoo_query.get_player_stats_by_date(player_key, chosen_date)))  # NHL/MLB/NBA
# print(repr(yahoo_query.get_player_ownership(player_key)))
# print(repr(yahoo_query.get_player_percent_owned_by_week(player_key, chosen_week)))
# print(repr(yahoo_query.get_player_draft_analysis(player_key)))

weeks = yahoo_query.get_game_weeks_by_game_id(game_id)
weekBoundDict = {}
for i in weeks:
    weekBoundDict[i['game_week'].week] = list(pd.date_range(start=i['game_week'].start,end=i['game_week'].end))

dailyDataDict = {}
for day in weekBoundDict[chosen_week]:
    data = yahoo_query.get_team_roster_player_stats_by_date(team_id, day.strftime('%Y-%m-%d'))
    filteredData = []
    for i in data:
        statDict = {}
        for j in i['player'].player_stats.stats:
            statDict[j['stat'].stat_id] = j['stat'].value
        filteredData.append({
            'name': i['player'].name.full,
            'team': i['player'].editorial_team_abbr,
            'position': i['player'].selected_position.position,
            'stats': statDict
        })
    dailyDataDict[day.strftime('%Y-%m-%d')] = filteredData

print(dailyDataDict)
#print(dailyDataDict[weekBoundDict[chosen_week][-1].strftime('%Y-%m-%d')])

#data = yahoo_query.get_team_roster_player_stats_by_week(team_id, chosen_week)

# stat_dict = {}
# for player in yahoo_query.get_team_roster_player_stats_by_week(team_id, chosen_week):
#     for category in player['player'].player_stats.stats:
#         try:
#             stat_dict[category['stat'].stat_id] = stat_dict[category['stat'].stat_id]  + category['stat'].value
#         except:
#             stat_dict[category['stat'].stat_id]  = 0
#             stat_dict[category['stat'].stat_id] = stat_dict[category['stat'].stat_id]  + category['stat'].value

# print(stat_dict)

# GP: 3
# GS: 4
# PPP: 14

# data = yahoo_query.get_team_roster_player_info_by_week(team_id, chosen_week)

# print(data)

# for i in data:
#     print(
#         i['player'].display_position,
#         i['player'].player_key,
#         i['player'].name.full,
#         i['player'].player_stats.stats,
#     )
