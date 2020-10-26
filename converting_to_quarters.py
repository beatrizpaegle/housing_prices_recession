def convert_housing_data_to_quarters():
    df_houses = pd.read_csv('City_Zhvi_AllHomes.csv')
    df_houses = df_houses.drop(['RegionID', 'Metro','CountyName', 'SizeRank'], axis = 1)
    df_houses
    df_houses['State'] = df_houses['State'].map(states)
    df_houses = df_houses.set_index(['State', 'RegionName'])
    df_houses = df_houses.drop([x for x in df_houses.columns[:45]], axis=1)
    #q2 = df_houses[['1996-04', '1996-05', '1996-06']].mean(axis=1)
    df_houses[[1]]
    len(df_houses.columns)
    list=[]
    for x in range(0, (len(df_houses.columns)-2), 3):
        list.append((df_houses[[x, x+1, x+2]].mean(axis=1)))

    len(list)
    list.append(df_houses[[len(df_houses.columns) - 2,len(df_houses.columns) - 1]].mean(axis=1))
    df_houses.columns
    len(df_houses.columns)
    list_aux =['0' + str(x) if x < 10 else str(x) for x in range (0,16) for y in range (0,4)]
    list_aux.append('16')
    list_aux.append('16')
    list_aux.append('16')
    list_columns = ['20{}q{}'.format(str(x),str(y%4 + 1)) for x,y in zip(list_aux, range(0,67))]
    for y,z in zip(list, list_columns):
        df_houses[str(z)] = y
    df_houses
    list_columns[len(list_columns)-1]
    len(list)
    #print(list_columns)
    df_houses = df_houses.drop([x for x in df_houses.columns[:200]], axis=1)
    
    
    return df_houses
