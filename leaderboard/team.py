from data import DataTeam
from config import Config
from page import Page
from datetime import datetime
from util.team_utils import (
    create_registration_content,
    create_registration_image,
    create_registered_teams,
    create_lobby_list,
)


def main(registration_title_content: str, registration_image_content: str):
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
        registration_title_content
        + registration_image_content
        + lobby_content
        + create_registered_teams(data, config["team_sheet_total_teams"])
    )

    page.set_page(registration_content)


if __name__ == "__main__":
    registration_title = "ER Project:SEA S2 Registered Teams"
    registration_date = datetime(
        year=2025,
        month=2,
        day=12,
        hour=13,
    )

    registration_title_content = create_registration_content(
        title=registration_title,
        date=registration_date,
    )

    # WARNING: xss and css attack may happened if it's publicly exposed
    image_source = "https://kanziebub.github.io/ProjectSEA/assets/images/ProjectSEA_S3_OpenRegis.png"
    image_alt = "S2OpenReg"
    image_style = "max-height: 350px;"

    registration_image_content = create_registration_image(
        src=image_source,
        alt=image_alt,
        style=image_style,
    )

    main(registration_title_content, registration_image_content)
