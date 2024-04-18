import pandas as pd
import pickle
from scipy.stats import poisson

# READ & LOAD
dict_groups = pickle.load(open('Dictionaries/dict_groups', 'rb'))
df_clean_worldcups = pd.read_csv('Database/df_clean_worldcups.csv')
df_clean_worldcup_2022 = pd.read_csv('Database/df_clean_worldcup_2022.csv')

# DF DE LOCAL TEAM & AWAY TEAM
df_local_team = df_clean_worldcups[['Local_Team', 'Local_Goals', 'Away_Goals']]
df_away_team = df_clean_worldcups[['Away_Team', 'Local_Goals', 'Away_Goals']]

# RENOMBRAR COLUMNAS
df_local_team = df_local_team.rename(columns={
    'Local_Team': 'Team', 'Local_Goals': 'Goals_Scored', 'Away_Goals': 'Goals_Conceded'})
df_away_team = df_away_team.rename(columns={
    'Away_Team': 'Team', 'Local_Goals': 'Goals_Conceded', 'Away_Goals': 'Goals_Scored'})

# CONCATEANR COLUMNAS
df_average_goal = pd.concat([df_local_team, df_away_team],
                            ignore_index=True).groupby('Team').mean()

# # TEST
# print(df_average_goal)


def prediction_points(local, away):
    if local in df_average_goal.index and away in df_average_goal.index:
        # MULTICPLICAMOS Goals_Scored * Goals_Conceded
        lamb_local = df_average_goal.at[local, 'Goals_Scored'] * \
            df_average_goal.at[away, 'Goals_Conceded']
        lamb_away = df_average_goal.at[away, 'Goals_Scored'] * \
            df_average_goal.at[local, 'Goals_Conceded']

        prob_local, prob_away, prob_draw = 0, 0, 0

        for x in range(0, 11):  # Número de goles 'local_team0
            for y in range(0, 11):  # Número de goles 'away_team'
                p = poisson.pmf(x, lamb_local) * poisson.pmf(y, lamb_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_local += p
                else:
                    prob_away += p

        points_local = 3 * prob_local + prob_draw
        points_away = 3 * prob_away + prob_draw
        return (points_local, points_away)

    else:
        return (0, 0)

# reste
# print(prediction_points('Argentina', 'Mexico'))


# DIVIDIR WORLDCUP2022 en grupos, oct, curt, semi, final..
df_wc2022_group_48 = df_clean_worldcup_2022[:48].copy()
df_wc2022_knockout = df_clean_worldcup_2022[48:56].copy()
df_wc2022_quater = df_clean_worldcup_2022[56:60].copy()
df_wc2022_semi = df_clean_worldcup_2022[60:62].copy()
df_wc2022_final = df_clean_worldcup_2022[62:].copy()

# ITERAR TODOS LOS PARTIDOS DE LA FASE GRUPOS Y ACTULIZAR LAS TABLAS POSTERIORES
for group in dict_groups:
    teams_in_group = dict_groups[group]['Team'].values
    df_fix_group_6 = df_wc2022_group_48[df_wc2022_group_48['local_teams'].isin(
        teams_in_group)]
    for index, row in df_fix_group_6.iterrows():
        local, away = row['local_teams'], row['away_teams']
        points_local, points_away = prediction_points(local, away)

        dict_groups[group].loc[dict_groups[group]
                               ['Team'] == local, 'Pts'] += points_local
        dict_groups[group].loc[dict_groups[group]
                               ['Team'] == away, 'Pts'] += points_away

    dict_groups[group] = dict_groups[group].sort_values(
        'Pts', ascending=False).reset_index()
    dict_groups[group] = dict_groups[group][['Team', 'Pts']]
    dict_groups[group] = dict_groups[group].round(0)

# print(dict_groups['Group A'])
# REEMPLAZAR GANADORES EN DICT
for group in dict_groups:
    group_winner = dict_groups[group].loc[0, 'Team']
    runners_up = dict_groups[group].loc[1, 'Team']

    df_wc2022_knockout.replace({f'Winners {group}': group_winner,
                                f'Runners-up {group}': runners_up}, inplace=True)

df_wc2022_knockout['Winner'] = 'Pending'


# FUNCTION GET_WINNER
def get_winner(df_fix_update):
    for index, row in df_fix_update.iterrows():
        local, away = row['local_teams'], row['away_teams']
        points_local, points_away = prediction_points(local, away)
        if points_local > points_away:
            winner = local
        else:
            winner = away
        df_fix_update.loc[index, 'Winner'] = winner
    return df_fix_update


# CREAR TABLA DE ACTUALIZACION
def update_table(df_fix_1, df_fix_2):
    for index, row in df_fix_1.iterrows():
        winner = df_fix_1.loc[index, 'Winner']
        match = df_fix_1.loc[index, 'score']
        df_fix_2.replace({f'Winners {match}': winner}, inplace=True)
    df_fix_2['Winner'] = "Pending"
    return df_fix_2


# IMPRIMIR PREDICTIONS
print("OCTAVOS DE FINAL")
print(get_winner(df_wc2022_knockout), "\n CUARTOS DE FINAL")
update_table(df_wc2022_knockout, df_wc2022_quater)
print(get_winner(df_wc2022_quater), '\n SEMI FINAL')
update_table(df_wc2022_quater, df_wc2022_semi)
print(get_winner(df_wc2022_semi), '\n FINAL')
update_table(df_wc2022_semi, df_wc2022_final)
print(get_winner(df_wc2022_final), '\n GANADOR')
