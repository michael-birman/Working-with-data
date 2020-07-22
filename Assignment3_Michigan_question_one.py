import pandas as pd
import numpy as np
def answer_one():
    
    # data base from http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls

    energy = pd.read_excel('Energy Indicators.xls',skip_footer=38,skip_header=1,skiprows=17)
    energy.drop(energy.columns[[0,1]],axis=1,inplace=True)
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Energy Supply']*=1000000
    for na_value in energy:
        energy[na_value] = energy[na_value].replace('...',np.NaN)
    energy.dropna()
    energy['Country'] =energy['Country'].str.replace("Republic of Korea","South Korea")
    energy['Country'] =energy['Country'].str.replace("United States of America","United States")
    energy['Country'] =energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland","United Kingdom")
    energy['Country'] =energy['Country'].str.replace("China, Hong Kong Special Administrative Region","Hong Kong")
    energy['Country'] =energy['Country'].str.replace('\d+', '') #remove numbers from country name
    energy['Country'] =energy['Country'].str.replace(r'\(.*\)', '') #remove Parenthesis
    energy['Country'] = energy['Country'].str.strip() # remove spaces after we removed parenthesis

    #switch to another data base from world bank gdp 1960 - 2015 http://data.worldbank.org/indicator/NY.GDP.MKTP.CD

    GDP = pd.read_csv('world_bank.csv' , skiprows = 4)
    GDP['Country Name'] = GDP['Country Name'].str.replace("Korea, Rep.", "South Korea")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
    GDP['Country Name'] = GDP['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")
    COLS = list(GDP.columns.values)

    #name change of country name to country
    COLS[0] = 'Country'
    GDP.columns = COLS
    GDP = GDP.drop(GDP.iloc[:,1:50], axis=1)


    # ScimEn data http://www.scimagojr.com/countryrank.php?category=2102

    ScimEn = pd.read_excel('scimagojr-3.xlsx')



    #merge 3 data tables:

    df= pd.merge(ScimEn, energy, how='outer', left_on = 'Country', right_on = 'Country')
    df1 = pd.merge(df,GDP,how='outer', left_on = 'Country', right_on = 'Country')   
    df1 = df1.set_index('Country')
    df1=df1[:15]
    return df1
answer_one()





