from data import Data
from page import Page
from utils import (
    add_penalty,
    create_leaderboard, 
    create_penalty_table, 
    read_yaml
)

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.yaml")
config = read_yaml(config_path) 
with_cp = False if config['checkpoint']==0 else True

def main():  
    page_path = os.path.join(current_dir, config["page_filepath"])
    page = Page(page_path)

    if config['lobby']==1:
        leaderboard = single_lobby()
    else:
        leaderboard = multi_lobby()

    page.set_header()
    page.add_content(leaderboard)
    page.set_footer()
    page.write()
    
def single_lobby():
    data = Data(config["sheetID"], config["sheetName"], config["teams"])
    leaderboard = f"""
# **Leaderboard**

{create_leaderboard(data, config["teams"], with_cp=with_cp)} 
{create_penalty_table('Qualifiers')} 
{add_penalty()}
""" 
    return leaderboard

def multi_lobby():
    data_1 = Data(config["sheetID"], config["sheetName"], config["teams"])
    data_2 = Data(config["sheetID"], config["sheetName"], config["teams"])

    data_1.filter_df(config["lobby1"])
    data_2.filter_df(config["lobby2"])
    leaderboard = f"""
# **Lobby 1 Leaderboard**

{create_leaderboard(data_1, len(config["lobby1"]), with_cp=with_cp)} 
{create_penalty_table('- Lobby 1 Qualifiers')} 
{add_penalty()}

# **Lobby 2 Leaderboard**

{create_leaderboard(data_2, len(config["lobby2"]), with_cp=with_cp)} 
{create_penalty_table('- Lobby 2 Qualifiers')} 
{add_penalty()}
""" 
    return leaderboard
    
# add_penalty() /no param/ itu untuk filler row ketika belum ada penalty
# {add_penalty(
#     game='x',
#     team='ipsum',
#     penalty='-1',
#     reason='Non Player Death (player)'
# )}

if __name__ == "__main__":
    main()
