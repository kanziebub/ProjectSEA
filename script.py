# Imports
import pandas as pd

def set_df(id, name):
    url = f'https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}'
    df = pd.read_csv(url, encoding='latin')
    df = df.iloc[1:19 , 1:9]

    df.rename(
        columns = {
            'Unnamed: 1':'Rank',
            'Unnamed: 2':'Name',
            'Unnamed: 3':'Total Point',
            'Unnamed: 4':'Total TK',
            'Unnamed: 5':'Avg TK',
            'Unnamed: 6':'Avg Placement',
            'Unnamed: 7':'Avg Placement Point',
            'Unnamed: 8':'Games Played',
            }, 
        inplace = True)

    return df

def get_by_team(df, team, field):
    row = df.loc[df['Name'] == team]
    return row[field].values[0]

def get_by_rank(df, rank, field):
    row = df.iloc[rank-1:rank]
    return row[field].values[0]

def get_games_played(df):
    num = max(df['Games Played'].values)
    return num

def get_header():
    head = """---
layout: default
---

[< Home](https://kanziebub.github.io/SurvivalProtocol/)

"""
    return head
    
def get_footer():
    home = """
[< Home](https://kanziebub.github.io/SurvivalProtocol/)
    """
    return home

def get_penalty_table():
    
    penalty = """
### Penalty Log

|  Game  | Team Name | Penalty | Reason                |
|:-------|:----------|:--------|:----------------------|
"""
    return penalty

# =====================================================
def set_penalty(game, team, penalty, reason):
    row = "| " + game + " | " + team + " | " + penalty + " | " + reason + " | \n"
    return row

def set_leaderboard(df, teams):
    leaderboard_md = "### Games Played = " + str(int(get_games_played(df))) + "\n"
    
    # ---------------------------------
    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** |
|:-------|:----------------------|:-----------|:-----------|
"""
    rows = ""
    for i in range (teams):
        rank = i+1
        rows+= get_data_by_rank(df, rank)

    lbtable = lbtable + rows
    page_md  = leaderboard_md + lbtable

    return page_md

    # ---------------------------------

def get_data_by_rank(df, rank):
    team = get_by_rank(df, rank, "Name")
    kill = get_by_rank(df, rank, "Total TK")
    poin = get_by_rank(df, rank, "Total Point")
    row = ""
    if (rank==1 or rank==2 or rank==3):
        row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(int(kill))+ " | **" +str(int(poin))+ "** | \n"
    else:
        row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(int(kill))+ " | " +str(int(poin))+ " | \n"
    return row

def get_custom_information():
    return (
"""
\n
### Bracket
- Group A
  - NANYA
  - Melon
  - Eclair
  - HnS
- Group B
  - Ijat
  - SIAPA
  - EzWins
  - GG
- Group C
  - BlmTau
  - YOLO
  - 66%ptk
  - NTR185
\n
### Match-up
```
Round 1: BC 
Round 2: AB 
Round 3: AC 
Round 4: BC 
Round 5: AB 
Round 6: AC
```
\n
""")
# =====================================================

def write_page(target, page_md):
    with open(target, 'w') as f:
        f.write(page_md)
       
def single():
    target = "./season/01/qualifiers.md"
    sheetID = ""
    sheetName = "ERCT"
    penalty_placeholder = "|        |           |         |                       | \n"

    df = set_df(sheetID, sheetName)
    leaderboard = ("""
# **Leaderboard**

""" + set_leaderboard(df, 16) 
    + get_penalty_table() 
    + penalty_placeholder
    # + set_penalty("a", "a", "aa", "otp") 
    + " \n \n")

    page_md = (  get_header() 
               + leaderboard
               #+ get_custom_information()
               + get_footer()
               )
    write_page(target, page_md)
    
def double():
    target = ""
    sheetA = ""
    sheetB = ""
    sheetName = "ERCT"
    penalty_placeholder = "|        |           |         |                       | \n"

    df_A = set_df(sheetA, sheetName)
    df_B = set_df(sheetB, sheetName)

    leaderboard_A = ("""
# **Lobby A Leaderboard**

""" + set_leaderboard(df_A, 7) 
    + get_penalty_table() 
    + penalty_placeholder
    # + set_penalty("", "", "", "") 
    + " \n \n")
    leaderboard_B = ("""
# **Lobby B Leaderboard**

""" + set_leaderboard(df_B, 7) 
    + get_penalty_table() 
    # + penalty_placeholder 
    + " \n \n")

    page_md = (get_header() 
               + leaderboard_A
               + leaderboard_B
               + get_footer())
    write_page(target, page_md)

def main():
    single()

main()
