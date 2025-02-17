import copy
from util.utils import check_int
from config import Config
from data import Data, DataTeam, DataPenalty
from typing import List


def create_scoreboard(
    data: Data,
    data_team: DataTeam,
    config: Config,
    penalty_list: List[DataPenalty] = [],
):
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

{create_leaderboard_table(dt, total_teams, with_cp=with_cp)} 
{create_penalty_table(f"""{lobby_number}Qualifiers""")} 
{add_penalties(penalty_list, team_list, is_multiple)}
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


def create_leaderboard_table(df: Data, teams: int, with_cp: bool = False):
    leaderboard_md = f"### Games Played = {check_int(df.get_games_played())}\n"

    lbtable = (
        """
|  Rank  | Team Name             | Total Kill | **Points** | CP |
|:-------|:----------------------|:-----------|:-----------|:---|
"""
        if with_cp
        else """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""
    )

    rows = ""
    for i in range(teams):
        rows += get_data_by_rank(df, i + 1, with_cp)

    return leaderboard_md + lbtable + rows


def get_data_by_rank(df: Data, rank, with_cp=False):
    team = df.get_by_rank(rank, "Name")
    kill = df.get_by_rank(rank, "Total Team Kill")
    poin = df.get_by_rank(rank, "Total Point")
    if with_cp:
        chkp = True if (poin >= 55) else False

        row = ""
        if rank == 1 or rank == 2 or rank == 3:
            row += (
                "| #**"
                + str(rank)
                + "** | **"
                + str(team)
                + "** | "
                + str(check_int(kill))
                + " | **"
                + str(check_int(poin))
                + "** | "
                + str(chkp)
                + " | \n"
            )
        else:
            row += (
                "| #**"
                + str(rank)
                + "** | "
                + str(team)
                + " | "
                + str(check_int(kill))
                + " | "
                + str(check_int(poin))
                + " | "
                + str(chkp)
                + " | \n"
            )
        return row
    else:
        row = ""
        if rank == 1 or rank == 2 or rank == 3 or rank == 4:
            row += (
                "| #**"
                + str(rank)
                + "** | **"
                + str(team)
                + "** | "
                + str(check_int(kill))
                + " | **"
                + str(check_int(poin))
                + "** | \n"
            )
        else:
            row += (
                "| #**"
                + str(rank)
                + "** | "
                + str(team)
                + " | "
                + str(check_int(kill))
                + " | "
                + str(check_int(poin))
                + " | \n"
            )
        return row


def add_penalties(
    data_penalties: List[DataPenalty] = [],
    team_list: list = [],
    is_multiple: bool = False,
):
    rows = ""
    for penalty in data_penalties:
        game = penalty.game
        team_name = penalty.team_name
        penalty_point = penalty.penalty
        reason = penalty.reason

        if is_multiple:
            if team_name in team_list:
                rows += add_penalty(game, team_name, penalty_point, reason)
        else:
            rows += add_penalty(game, team_name, penalty_point, reason)

    return rows if rows != "" else add_penalty()


def add_penalty(game: str = "", team: str = "", penalty: str = "", reason: str = ""):
    row = f"""|  {game}  |  {team}  |  {penalty}  |  {reason}  |
"""
    return row


def create_penalty_table(header):

    penalty = (
        """
## Penalty Log """
        + header
        + """

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|"""
    )
    return penalty
