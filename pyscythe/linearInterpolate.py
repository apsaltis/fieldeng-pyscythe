
# _______           _______  _______          _________          _______
#(  ____ )|\     /|(  ____ \(  ____ \|\     /|\__   __/|\     /|(  ____ \
#| (    )|( \   / )| (    \/| (    \/( \   / )   ) (   | )   ( || (    \/
#| (____)| \ (_) / | (_____ | |       \ (_) /    | |   | (___) || (__
#|  _____)  \   /  (_____  )| |        \   /     | |   |  ___  ||  __)
#| (         ) (         ) || |         ) (      | |   | (   ) || (
#| )         | |   /\____) || (____/\   | |      | |   | )   ( || (____/\
#|/          \_/   \_______)(_______/   \_/      )_(   |/     \|(_______/
#



import pandas as pd

# takes the name of signal1 and a list of signals to interpolate , the name of the signal columnName and a dataFrame

def interpolate(signalName, list, columnName, dataFrame):

    dataFrame['time'] = pd.to_datetime(dataFrame['time'])
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    joinY = pd.DataFrame()
    joinX = pd.DataFrame()
    listX = []
    listY = []
    dictMap = {}
    listAll = [df1, df2, joinY, joinX]


    #dev prints
    #print('interpolating ..........')
    #print(signalName + ' ,' + str(list) + ' ,' + columnName)

    if signalName in list:
        list.remove(signalName)

    index = 0

    if len(list) < 2:

        # create seperate dataframes of the 2 signals ... Only 2 signals are supported in the incoming dataframe
        for i in dataFrame[columnName]:
            if i == signalName:
                df1 = df1.append(dataFrame.iloc[[index]])
                index = index + 1
            else:
                df2 = df2.append(dataFrame.iloc[[index]])
                index = index + 1

        index = 0
        #left,right specify may not be needed. Holding as comment for now
        #joinResult = df1.merge(df2, left_on=df1['time'], right_on=df2['time'], how='left')
        joinResult = df1.merge(df2, on='time', how='left')
        #interpolate values
        interpResult = joinResult.interpolate()

        # X is the signalName and the Left side of our Join as it is longest
        joinX[columnName] = signalName
        joinX['time'] = interpResult['time']
        joinX['value'] = interpResult['value_x']
        joinX[columnName] = str(signalName)

        #set signal name based on value in the passed list ... Limited... Still needs to be expanded to longer lists...
        joinY[columnName] = list[0]
        joinY['time'] = interpResult['time']
        joinY['value'] = interpResult['value_y']
        joinY[columnName] = str(list[0])

        for i in joinX['time']:
            listX.append(joinX.iloc[[index]].values.tolist())
            index = index + 1

        index = 0

        for i in joinY['time']:
            listY.append(joinY.iloc[[index]].values.tolist())
            index = index + 1

        #create map/dictionary of signals and interpolated results.
        dictMap[signalName]=listX
        dictMap[list[0]]=listY

        #dev prints check results debug
        #print('interpolated......')
        #print(dictMap)

        #clean up memory
        listAll.append(joinResult)
        listAll.append(interpResult)
        del(df1, df2, dataFrame, joinX, joinY, joinResult, interpResult)
        del listAll

    #TODO Handle larger lists of signals
    #else:

    #Return result ...

    return dictMap



def interpolateN(signalName, list, columnName, dataFrame):

    print('TODO not yet implemented')