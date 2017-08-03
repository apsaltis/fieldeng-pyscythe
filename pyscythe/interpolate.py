#
#
#
import pandas as pd

# takes the name of signal1 and a list of signals to interpolate , the name of the signal columnName and a dataFrame

def interpolate(signalName, list, columnName, dataFrame):

    dataFrame['time'] = pd.to_datetime(dataFrame['time'])
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    index = 0

    for i in dataFrame['function']:
        if i == signalName:
            df1 = df1.append(dataFrame.iloc[[index]])
            index = index + 1
        else:
            df2 = df2.append(dataFrame.iloc[[index]])
            index = index + 1

    joinResult = df1.merge(df2, left_on=df1['time'], right_on=df2['time'], how='left')

    joinResult.interpolate()



