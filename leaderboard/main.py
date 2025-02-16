import copy
from config import Config
from data import Data, DataTeam, DataPenalty
from page import Page
from utils import add_penalties, create_leaderboard, create_penalty_table


def main():
    init_config = Config("config.yaml")

    config = init_config.config
    page_path = init_config.set_filepath(config["page_filepath"])

    page = Page(page_path)
    data = Data(config["sheetID"], config["sheetName"], config["teams"])
    data_team = DataTeam(
        config["team_sheet_id"],
        config["team_sheet_name"],
        config["team_sheet_total_teams"],
    )

    leaderboard_content = create_scoreboard(data, data_team, config)

    page.set_page(leaderboard_content)


def create_scoreboard(data: Data, data_team: DataTeam, config: Config):
    with_cp = False if config["checkpoint"] == 0 else True
    lobby_number = ""
    is_multiple = True if config["team_sheet_lobby_gid"] else False
    total_lobby, teams = get_total_lobby_and_teams(data_team, config, is_multiple)

    leaderboard = ""
    for i in range(total_lobby):
        temp = copy.deepcopy(data)
        dt = temp
        team_list = []
        total_teams = config["teams"]
        if is_multiple:
            lobby_number = "Lobby " + str(i + 1)
            team_list = teams[lobby_number]
            dt = temp.filter_df(team_list)
            total_teams = len(team_list)

            lobby_number += " "

        leaderboard += f"""
# **{lobby_number}Leaderboard**

{create_leaderboard(dt, total_teams, with_cp=with_cp)} 
{create_penalty_table(f"""{lobby_number}Qualifiers""")} 
{add_penalties(create_penalties_log(), team_list, is_multiple)}
"""
    return leaderboard


def get_total_lobby_and_teams(data_team: DataTeam, config: Config, is_multiple: bool):
    total_lobby = 1
    teams = {}
    if is_multiple:
        df = data_team.set_def_lobby(config["team_sheet_lobby_gid"])
        total_lobby = len(df.columns)

        for i in range(total_lobby):
            lobby_number = f"""Lobby {i+1}"""
            for j in range(len(df)):
                value = df.iloc[j][lobby_number]
                if lobby_number not in teams:
                    teams[lobby_number] = [value]
                else:
                    teams[lobby_number].append(value)

    return total_lobby, teams


def create_penalties_log():
    penalty_list = [
        # example:
        # DataPenalty(game=1, team_name="FizzBuzz", penalty=-1, reason="Killed by Red Zone (fizz)"),
        # DataPenalty(game=2, team_name="FizzBuzz", penalty=-1, reason="Killed by Red Zone (buzz)"),
        # DataPenalty(game=1, team_name="FooBar", penalty=-1, reason="Killed by Wild Animals (Baz)"),
        # DataPenalty(game=4, team_name="LoremIpsum", penalty=-1, reason="Killed by Ego (Lorem)"),
    ]
    return penalty_list


# add_penalty() /no param/ itu untuk filler row ketika belum ada penalty
# {add_penalty(
#     game='x',
#     team='ipsum',
#     penalty='-1',
#     reason='Non Player Death (player)'
# )}

if __name__ == "__main__":
    main()
