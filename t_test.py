def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    from scipy import stats
    df_houses = convert_housing_data_to_quarters()
    recession_start = get_recession_start()
    recession_bottom = get_recession_bottom()
    df_houses['change_recession'] = df_houses[recession_bottom]/df_houses[recession_start]
    #df_houses[recession_bottom]
    df_houses
    university_towns = get_list_of_university_towns()
    df_houses
    df_houses[df_houses.index.isin(university_towns['RegionName'])]
    df_houses_dif = df_houses.reset_index()
    df_houses_dif = df_houses_dif.set_index('RegionName')

    s2 = list(university_towns['RegionName'])
    df_houses_dif
    #print(df_houses_dif.index.isin(s2))
    for answer in  df_houses_dif.index.isin(s2):
        #print(answer)
        y=answer

    df_houses_univ = df_houses_dif[df_houses_dif.index.isin(s2)]
    df_houses_not_univ = df_houses_dif[~(df_houses_dif.index.isin(s2))]
    df_houses_univ['change_recession']
    (s,p) = stats.ttest_ind(df_houses_univ['change_recession'], df_houses_not_univ['change_recession'], nan_policy='omit')
    if max(df_houses_univ['change_recession'].mean(), df_houses_not_univ['change_recession'].mean()) == df_houses_univ['change_recession'].mean():
        better = 'university town'
    else:
        better = 'non-university town'

                                                                                                        
   
    
    return (True, p, better)
