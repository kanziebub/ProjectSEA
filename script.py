# Imports
import pandas as pd
import math

def set_df(id, name, source):
    url = f'https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={name}'
    df = pd.read_csv(url, encoding='latin')
    df = df.iloc[1:19 , 1:9]

    columns = {
            'Unnamed: 1':'Rank',
            'Unnamed: 2':'Name',
            'Unnamed: 3':'Total Point',
            'Unnamed: 4':'Total Team Kill',
            'Unnamed: 5':'Avg. Team Kill',
            'Unnamed: 6':'Avg. Placement',
            'Unnamed: 7':'Avg. Placement Point',
            'Unnamed: 8':'Games Played',
            }
    
    col_shuvi = {
            'Unnamed: 1':'Rank',
            'Unnamed: 2':'Name',
            'Unnamed: 3':'Checkpoint',
            'Unnamed: 4':'Total Point',
            'Unnamed: 5':'Total TK',
            'Unnamed: 6':'',
            'Unnamed: 7':'',
            'Unnamed: 8':'',
            }
    
    if (source!='carrot'):
        columns=col_shuvi


    df.rename(
        columns = columns, 
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
def set_leaderboard_with_cp(df, teams):
    leaderboard_md = ("### Games Played = " 
                      + str(int(check_int(get_games_played(df)))) 
                      + "\n")
    
    # ---------------------------------
    lbtable = """
|  Rank  | Team Name             | Total Kill | **Points** | Checkpoint |
|:-------|:----------------------|:-----------|:-----------|:-----------|
"""
    rows = ""
    for i in range (teams):
        rank = i+1
        rows+= get_data_by_rank_with_cp(df, rank)

    lbtable = lbtable + rows
    page_md  = leaderboard_md + lbtable

    return page_md

def get_data_by_rank_with_cp(df, rank):
    team = get_by_rank(df, rank, "Name")
    kill = get_by_rank(df, rank, "Total Team Kill")
    poin = get_by_rank(df, rank, "Total Point")
    chkp = get_by_rank(df, rank, "Checkpoint")
    row = ""
    if (rank==1 or rank==2 or rank==3):
        row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(check_int(kill))+ " | **" +str(check_int(poin))+ "** | " +str(chkp)+ " | \n"
    else:
        row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(check_int(kill))+ " | " +str(check_int(poin))+ " | " +str(chkp)+" | \n"
    return row
# =====================================================
def set_penalty(game, team, penalty, reason):
    row = "| " + game + " | " + team + " | " + penalty + " | " + reason + " | \n"
    return row

def set_leaderboard(df, teams):
    leaderboard_md = ("### Games Played = " 
                      + str(int(check_int(get_games_played(df)))) 
                      + "\n")
    
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

def check_int(value):
    return 0 if math.isnan(value) else int(value)

def check_str(value):
    return '' if math.isnan(value) else str(value)

def get_data_by_rank(df, rank):
    team = get_by_rank(df, rank, "Name")
    kill = get_by_rank(df, rank, "Total Team Kill")
    poin = get_by_rank(df, rank, "Total Point")
    row = ""
    if (rank==1 or rank==2 or rank==3):
        row += "| #**"+str(rank)+"** | **" +str(team)+ "** | " +str(check_int(kill))+ " | **" +str(check_int(poin))+ "** | \n"
    else:
        row += "| #**"+str(rank)+"** | " +str(team)+ " | " +str(check_int(kill))+ " | " +str(check_int(poin))+ " | \n"
    return row

def get_custom_information():
    return (
"""
\n
### Bracket 1
- Group 1.1
  - T1
  - T2
  - T3
  - T4
- Group 1.2
  - T5
  - T6
  - T7
  - T8
- Group 1.3
  - T9
  - T10
  - T11
  - T12
- Group 1.4
  - T13
  - T14
  - T15
  - T16
\n
```
- Round 1 
  - Lobby A: Group 1.1 + Group 1.2
  - Lobby B: Group 1.3 + Group 1.4
- Round 2
  - Lobby A: Group 1.1 + Group 1.3
  - Lobby B: Group 1.2 + Group 1.4
- Round 3 
  - Lobby A: Group 1.1 + Group 1.4
  - Lobby B: Group 1.2 + Group 1.3
```
\n
### Bracket 2
- Group 2.1
  - ???
  - ???
  - ???
  - ???
- Group 2.2
  - ???
  - ???
  - ???
  - ???
- Group 2.3
  - ???
  - ???
  - ???
  - ???
\n
```
- Round 1: Group 2.1 + Group 2.2
- Round 2: Group 2.2 + Group 2.3
- Round 3: Group 2.1 + Group 2.3
```
\n
""")
# =====================================================

def write_page(target, page_md):
    with open(target, 'w') as f:
        f.write(page_md)
       
def single():
    target = "./season/01/qualifiers.md"
    sheetID = "12pQ9xl-9M7xOaBndxB8c8cWKKmNO1ARbesSdr7XhR-0"
    sheetName = "ERCT"
    penalty_placeholder = "|        |           |         |                       | \n"

    df = set_df(sheetID, sheetName, 'carrot')
    # print(df)
    leaderboard = ("""
# **Leaderboard**

""" + set_leaderboard(df, 16) 
    + get_penalty_table() 
    + penalty_placeholder
    # + set_penalty("a", "a", "aa", "otp") 
    + " \n \n")

    page_md = (  get_header() 
               + leaderboard
               + get_custom_information()
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
