import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("stuff.csv")
electronics=df.loc[df["Mobile Brand"]]
#print(studentDf)
meanOfAttempts=electronics.groupby["Avg Rating"].mean()
print(meanOfAttempts)

figure=ff.create_distplot([meanOfAttempts],["Ratings"])
figure.show()