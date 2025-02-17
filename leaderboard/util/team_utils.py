import pytz
from datetime import datetime
from data import DataTeam


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
