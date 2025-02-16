import math
import yaml
import pytz

from data import Data, DataTeam, DataPenalty
from datetime import datetime
from typing import List


def read_yaml(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


def check_int(value):
    return 0 if math.isnan(value) else int(value)


def check_str(value):
    return "" if math.isnan(value) else str(value)


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


def add_penalty(game: str = "", team: str = "", penalty: str = "", reason: str = ""):
    row = f"""|  {game}  |  {team}  |  {penalty}  |  {reason}  |
"""
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


def create_leaderboard(df: Data, teams: int, with_cp: bool = False):
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


def create_filtered_leaderboard(df: Data, teams, with_cp=False):
    return ""


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


def create_registration_content(
    title: str, date: datetime, timezone: str = "Asia/Jakarta"
):
    local_tz = pytz.timezone(timezone)
    format = "%Y-%m-%d %H:%M:%S UTC%z"
    date = local_tz.localize(date)
    formatted_date = date.strftime(format)

    return f"""
# **{title}**
Registration opens {formatted_date}

"""


def create_registration_image(src: str, alt: str, style: str = "max-height: 350px;"):
    return f"""
<p align="center">
  <img 
    src={src} 
    alt={alt}
    style={style}>
</p>
"""


def create_lobby_list(df):
    len_row = len(df)
    len_col = len(df.columns)
    header = f"""|"""
    header_slide = f"""|"""
    body = f"""|"""

    for i in range(len_row):
        if i != 0:
            body += f"""
|"""
        for j in range(len_col):
            lobby_number = f"""Lobby {j+1}"""
            value = df.iloc[i][lobby_number]
            if i == 0:
                header += f"""  Lobby {i+1}  |"""
                header_slide += f""":---------|"""
            body += f""" {value} |"""

    return (
        header
        + f"""
"""
        + header_slide
        + f"""
"""
        + body
    )


def create_registered_teams(df: DataTeam, teams: int):
    details = ""
    for i in range(teams):
        details += get_team_details(df, i + 1)

    details += f"""

<br>

"""
    return details


def get_team_details(df: DataTeam, index: int):
    team = df.get_by_index(index, "Team Name")
    member_1 = df.get_by_index(index, "IGN Member 1 (Leader)")
    member_2 = df.get_by_index(index, "IGN Member 2")
    member_3 = df.get_by_index(index, "IGN Member 3")
    member_4 = df.get_by_index(index, "IGN Sub Member (optional)")

    detail = f"""<details>
    <summary>{team}</summary>
    <ul>
        <li>{member_1}</li>
        <li>{member_2}</li>
        <li>{member_3}</li>"""

    if member_4 == member_4:
        detail += f"""
        <li>{member_4}</li>"""

    detail += f"""
    </ul>
</details>
"""

    return detail
