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

def main():   
    config = read_yaml(config_path) 
    page_path = os.path.join(current_dir, config["page_filepath"])

    with_cp = False if config['checkpoint']==0 else True

    page = Page(page_path)
    data = Data(config["sheetID"], config["sheetName"], config["teams"])
    
    leaderboard = f"""
# **Leaderboard**

{create_leaderboard(data, config["teams"], with_cp=with_cp)} 
{create_penalty_table('- Qualifiers')} 
{add_penalty(
    game='2',
    team='NaRoRe',
    penalty='-1',
    reason='Non Player Death (Rooper)'
)}
{add_penalty(
    game='2',
    team='LastTeam',
    penalty='-1',
    reason='Non Player Death (Renal)'
)}
{add_penalty(
    game='3',
    team='VisCa',
    penalty='-1',
    reason='Non Player Death (Fee)'
)}
"""

    page.set_header()
    page.add_content(leaderboard)
    page.set_footer()
    page.write()

if __name__ == "__main__":
    main()
