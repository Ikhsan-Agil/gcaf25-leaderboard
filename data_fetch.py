import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import math

load_dotenv()

df = pd.read_csv(os.getenv("FILEPATH"))
#print(df.info())

badgesSum=df["# Jumlah Skill Badge yang Diselesaikan"]+df["# Jumlah Game Arcade yang Diselesaikan"]+df["# Jumlah Game Trivia yang Diselesaikan"]

# Logic for count the points

# pointsGet=np.floor(df["# Jumlah Skill Badge yang Diselesaikan"]/2)+df["# Jumlah Game Arcade yang Diselesaikan"]+df["# Jumlah Game Trivia yang Diselesaikan"]

totalPoints = []
for i in range(0, len(df)):
    if df["# Jumlah Game Arcade yang Diselesaikan"][i] >= 10 and df["# Jumlah Game Trivia yang Diselesaikan"][i] >= 8 and df["# Jumlah Skill Badge yang Diselesaikan"][i] >= 44 :
        points=math.floor(df["# Jumlah Skill Badge yang Diselesaikan"][i]/2) + df["# Jumlah Game Arcade yang Diselesaikan"][i] + df["# Jumlah Game Trivia yang Diselesaikan"][i] + 28
        totalPoints.append(points)

    elif df["# Jumlah Game Arcade yang Diselesaikan"][i] >= 8 and df["# Jumlah Game Trivia yang Diselesaikan"][i] >= 7 and df["# Jumlah Skill Badge yang Diselesaikan"][i] >= 30 :
        points=math.floor(df["# Jumlah Skill Badge yang Diselesaikan"][i]/2) + df["# Jumlah Game Arcade yang Diselesaikan"][i] + df["# Jumlah Game Trivia yang Diselesaikan"][i] + 19
        totalPoints.append(points)

    elif df["# Jumlah Game Arcade yang Diselesaikan"][i] >= 6 and df["# Jumlah Game Trivia yang Diselesaikan"][i] >= 6 and df["# Jumlah Skill Badge yang Diselesaikan"][i] >= 20 :
        points=math.floor(df["# Jumlah Skill Badge yang Diselesaikan"]/2)[i] + df["# Jumlah Game Arcade yang Diselesaikan"][i] + df["# Jumlah Game Trivia yang Diselesaikan"][i] + 14
        totalPoints.append(points)

    elif df["# Jumlah Game Arcade yang Diselesaikan"][i] >= 4 and df["# Jumlah Game Trivia yang Diselesaikan"][i] >= 4 and df["# Jumlah Skill Badge yang Diselesaikan"][i] >= 10 :
        points=math.floor(df["# Jumlah Skill Badge yang Diselesaikan"][i]/2) + df["# Jumlah Game Arcade yang Diselesaikan"][i] + df["# Jumlah Game Trivia yang Diselesaikan"][i] + 7
        totalPoints.append(points)
        
    else:
        points=math.floor(df["# Jumlah Skill Badge yang Diselesaikan"][i]/2) + df["# Jumlah Game Arcade yang Diselesaikan"][i] + df["# Jumlah Game Trivia yang Diselesaikan"][i]
        totalPoints.append(points)

df.insert(df.shape[1],"points",totalPoints)

# create new dataframe
newDf = pd.DataFrame(
    {
        "student_name": df["Nama Peserta"],
        "skill_badges_completed": df["# Jumlah Skill Badge yang Diselesaikan"],
        "arcade_games_completed": df["# Jumlah Game Arcade yang Diselesaikan"],
        "arcade_trivia_games_completed": df["# Jumlah Game Trivia yang Diselesaikan"],
        "total_badges": badgesSum,
        "milestone_achieved": df["Milestone yang Diselesaikan"],
        "points": df["points"]
    }
)

# Sort Dataframe from points_get
dataframe = newDf.sort_values(by=["points","total_badges"], ascending=False, ignore_index=True)

file_data = []
for x in range(0, len(dataframe)):
    data = {
        "rank": x+1,
        "student_name": dataframe["student_name"][x],
        "skill_badges_completed": dataframe["skill_badges_completed"][x],
        "arcade_games_completed": dataframe["arcade_games_completed"][x],
        "arcade_trivia_games_completed": dataframe["arcade_trivia_games_completed"][x],
        "total_badges": dataframe["total_badges"][x],
        "milestone_achieved": dataframe["milestone_achieved"][x],
        "points": dataframe["points"][x]
    }
    file_data.append(data)

