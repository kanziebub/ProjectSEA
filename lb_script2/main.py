from config import Config
from data import Data, DataTeam, DataPenalty
from typing import List
from page import Page
from util.scoreboard_utils import create_scoreboard


def main(
    penalty_list: List[DataPenalty] = [],
):
    init_config = Config("config.yaml")

    config = init_config.config
    page_path = init_config.set_filepath(config["page_filepath"])

    page = Page(page_path)
    data = Data(config["sheetID"], config["sheetName"], config["teams"])
    data_team = DataTeam(
        config["team_sheet_id"],
        config["team_sheet_name"],
        config["team_sheet_total_teams"],
    )

    leaderboard_content = create_scoreboard(data, data_team, config, penalty_list)

    page.set_page(leaderboard_content)


if __name__ == "__main__":
    # NOTE: Make sure the team_name is exactly the same as the one in the registered teams
    penalty_list = [
        # example:
        # DataPenalty(game=1, team_name="FizzBuzz", penalty=-1, reason="Killed by Red Zone (fizz)"),
        # DataPenalty(game=2, team_name="FizzBuzz", penalty=-1, reason="Killed by Red Zone (buzz)"),
        # DataPenalty(game=1, team_name="FooBar", penalty=-1, reason="Killed by Wild Animals (Baz)"),
        # DataPenalty(game=1, team_name="LoremIpsum", penalty=-1, reason="Killed by Wild Animals (Lorem)"),
    ]

    main(penalty_list)
