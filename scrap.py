from cricguru import team

team = team.Team()
query_params = {
    "class": "3",
    "filter": "advanced",
    "opposition": "",
    "orderby": "batted_score",
    "team": "7",
    "template": "results",
    "type": "batting",
    "view": "innings"
}

cric_data = team.inn_by_inn(query_params, 2500)


columns_to_drop = ["Mins", "BF", "4s", "6s", "SR", "Start Date"]

cric_data = cric_data.drop(columns=columns_to_drop)
columns_order = ["Player", "Opposition", "Ground", "Inns", "Runs"]
cric_data = cric_data[columns_order]
file_path = './csv/batting.csv'

cric_data.to_csv(file_path, index=False, index_label="#")

# print(cric_data)

query_params2 = {
    "class": "3",
    "filter": "advanced",
    "opposition": "",
    "orderby": "wickets",
    "team": "7",
    "template": "results",
    "type": "bowling",
    "view": "innings"
}
bowling_data = team.inn_by_inn(query_params2, 2500)
bowling_cols_to_drop = ["Mdns", "Econ", "Runs"]

bowling_data = bowling_data.drop(columns=bowling_cols_to_drop)
bowling_data_columns_order = [
    "Player", "Opposition", "Ground", "Inns", "Overs", "Wkts"]
bowling_data = bowling_data[bowling_data_columns_order]
bowling_data_file_path = "./csv/bowling.csv"
bowling_data.to_csv(bowling_data_file_path, index=False)
