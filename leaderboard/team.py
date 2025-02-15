from data import DataTeam
from config import Config
from page import Page
from datetime import datetime
from utils import (
    create_registration_content,
    create_registration_image,
    create_registered_teams,
    create_lobby_list,
)


def main():
    init_config = Config("config.yaml")

    config = init_config.config
    page_path = init_config.set_filepath(config["team_sheet_file_path"])
    page = Page(page_path)
    lobby_content = ""

    data = DataTeam(
        config["team_sheet_id"],
        config["team_sheet_name"],
        config["team_sheet_total_teams"],
    )
    if config["team_sheet_lobby_gid"]:
        lobby_df = data.set_def_lobby(config["team_sheet_lobby_gid"])
        lobby_content = f"""
{create_lobby_list(lobby_df)}

"""

    registration_content = (
        create_registration_header_content()
        + lobby_content
        + create_registered_teams(data, config["team_sheet_total_teams"])
    )

    page.set_page(registration_content)


def create_registration_header_content():
    registration_title_content = create_registration_content(
        title="ER Project:SEA S2 Registered Teams",
        date=datetime(year=2025, month=2, day=12, hour=13),
    )
    # WARNING: xss and css attack may happened if it's publicly exposed
    registration_image_content = create_registration_image(
        src="https://kanziebub.github.io/ProjectSEA/assets/images/ProjectSEA_S3_OpenRegis.png",
        alt="S2OpenReg",
        style="max-height: 350px;",
    )

    return registration_title_content + registration_image_content


if __name__ == "__main__":
    main()
