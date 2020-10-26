def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    df_gdp = pd.read_excel(r'gdplev.xls')
    df_gdp = df_gdp.drop([x for x in range (7, 219)])
    df_gdp = df_gdp.drop([x for x in range (0,4)])
    df_gdp = df_gdp.drop([x for x in range (5,7)]).reset_index()
    list_gdp = list(df_gdp['Unnamed: 6'][1:])
    list_quarters = list(df_gdp['Unnamed: 4'][1:])
    for x in range(len(list_gdp)):
        if x>1:
            if list_gdp[x-1] < list_gdp[x-2]:
                    print('0ok')
                    if list_gdp[x] < list_gdp[x-1]:
                        print('1ok')
                        if list_gdp[x] < list_gdp[x+1]:
                            print('2ok')
                            if list_gdp[x+1] < list_gdp[x+2]:
                                print('3ok', x)
                                y=x+2


    
    return list_quarters[y]    
