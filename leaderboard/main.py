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
{create_penalty_table('- Wildcard')} 
{add_penalty(
    game='1',
    team='Eclair',
    penalty='-1',
    reason='Non Player Death (Caffeine)'
)}
{add_penalty(
    game='1',
    team='DegaDegi',
    penalty='-1',
    reason='Non Player Death (Azurieru)'
)}
{add_penalty(
    game='1',
    team='HeyTayo',
    penalty='-1',
    reason='Non Player Death (Onryou)'
)}
{add_penalty(
    game='1',
    team='HeyTayo',
    penalty='-1',
    reason='Non Player Death (ZxLaim)'
)}
{add_penalty(
    game='2',
    team='ViciVeni',
    penalty='-1',
    reason='Non Player Death (Iz1Senpai)'
)}
{add_penalty(
    game='2',
    team='CEPU',
    penalty='-1',
    reason='Non Player Death (CEPU-Valsh)'
)}
{add_penalty(
    game='4',
    team='StepuhSons',
    penalty='-1',
    reason='Non Player Death (Saiikyouu)'
)}
{add_penalty(
    game='4',
    team='StepuhSons',
    penalty='-1',
    reason='Non Player Death (Oshunicus)'
)}
{add_penalty(
    game='5',
    team='LastTeam',
    penalty='-1',
    reason='Non Player Death (Gallileo)'
)}
"""

    page.set_header()
    page.add_content(leaderboard)
    page.set_footer()
    page.write()

if __name__ == "__main__":
    main()
