import math
import yaml

from data import Data

def read_yaml(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data

def check_int(value):
    return 0 if math.isnan(value) else int(value)

def check_str(value):
    return '' if math.isnan(value) else str(value)

def create_penalty_table(header):
    
    penalty = """
## Penalty Log """ +header+ """

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|"""
    return penalty

def add_penalty(
        game:str='',
        team:str='', 
        penalty:str='', 
        reason:str=''
    ):
    row = "| " + game + " | " + team + " | " + penalty + " | " + reason + " |"
    return row

def create_leaderboard(df: Data, teams, with_cp=False):
    leaderboard_md = f"### Games Played = {check_int(df.get_games_played())}\n"
    
    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** | CP |
|:-------|:----------------------|:-----------|:-----------|:---|
""" if with_cp else """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""

    rows = ""
    for i in range(teams):
        rows += get_data_by_rank(df, i+1, with_cp)

    return leaderboard_md + lbtable + rows

def get_data_by_rank(df: Data, rank, with_cp=False):
    team = df.get_by_rank(rank, "Name")
    kill = df.get_by_rank(rank, "Total Team Kill")
    poin = df.get_by_rank(rank, "Total Point")
    if with_cp:
        chkp = True if (poin >= 55) else False
            
        row = ""
        if (rank==1 or rank==2 or rank==3):
            row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(check_int(kill))+ " | **" +str(check_int(poin))+ "** | " +str(chkp)+ " | \n"
        else:
            row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(check_int(kill))+ " | " +str(check_int(poin))+ " | " +str(chkp)+" | \n"
        return row
    else:
        row = ""
        if (rank==1 or rank==2 or rank==3 or rank==4):
            row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(check_int(kill))+ " | **" +str(check_int(poin))+ "** | \n"
        else:
            row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(check_int(kill))+ " | " +str(check_int(poin))+ " | \n"
        return row
    