from data import Data
from page import Page
from utils import (
    create_leaderboard, 
    create_penalty_table, 
    read_yaml
)

def main():
    config = read_yaml("config.yaml")
    page = Page(config["page_filepath"])
    sheetID = config["sheetID"]
    sheetName = config["sheetName"]
    df = Data(sheetID, sheetName)
    
    leaderboard = f"""
# **Leaderboard**

{create_leaderboard(df, 8, with_cp=True)} 
{create_penalty_table('')} 
|        |           |         |                       | \n
"""

    page.set_header()
    page.add_content(leaderboard)
    page.set_footer()
    page.write()

if __name__ == "__main__":
    main()
