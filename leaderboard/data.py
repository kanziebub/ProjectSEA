import pandas as pd


class Data:
    def __init__(self, sheetID: str, name: str, teams: int):
        self.sheetID = sheetID
        self.name = name
        self.url = f"https://docs.google.com/spreadsheets/d/{sheetID}/gviz/tq?tqx=out:csv&sheet={name}"
        self.df = self.set_df(teams)

    def get_by_team(self, team, column):
        row = self.df.loc[self.df["Name"] == team]
        return row[column].values[0]

    def get_by_rank(self, rank, column):
        row = self.df.iloc[rank - 1 : rank]
        return row[column].values[0]

    def get_games_played(self):
        return max(self.df["Games Played"].values)

    def get_df(self):
        return self.df

    def set_df(self, teams):
        columns = {
            "Unnamed: 1": "Rank",
            "Unnamed: 2": "Name",
            "Unnamed: 3": "Total Point",
            "Unnamed: 4": "Total Team Kill",
            "Unnamed: 5": "Avg. Team Kill",
            "Unnamed: 6": "Avg. Placement",
            "Unnamed: 7": "Avg. Placement Point",
            "Unnamed: 8": "Games Played",
        }

        df = pd.read_csv(self.url, encoding="latin")
        df = df.iloc[1 : teams + 1, 1:9]
        df.rename(columns=columns, inplace=True)
        return df

    def filter_df(self, team_list):
        prev_df = self.df
        filtered_df = prev_df[prev_df["Name"].isin(team_list)]
        self.df = filtered_df


class DataTeam:
    def __init__(self, sheetID: str, name: str, teams: int):
        self.sheetID = sheetID
        self.name = name
        self.url = f"https://docs.google.com/spreadsheets/d/{sheetID}/gviz/tq?tqx=out:csv&sheet={name}"
        self.df = self.set_df(teams)

    def set_df(self, teams: int):
        df = pd.read_csv(self.url, encoding="utf-8")
        df = df.iloc[0 : teams + 1]

        return df

    def set_def_lobby(self, gid: str):
        url_gid = self.url + f"&gid={gid}"
        df = pd.read_csv(url_gid, encoding="utf-8")

        return df

    def get_by_index(self, index, column):
        row = self.df.iloc[index - 1 : index]
        return row[column].values[0]
