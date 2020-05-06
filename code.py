# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head())



# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries=pd.DataFrame(data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']])
top_countries.drop(index=146,axis=0,inplace=True)
def top_ten(df,cname):
    country_list=[]
    country_list=list((df.nlargest(10,cname)['Country_Name']))
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=[i for i in top_10 if i in top_10_summer and i in top_10_winter]
print(common)



# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,10))
summer_df.groupby(['Country_Name','Total_Summer']).size().unstack().plot(kind='bar',ax=ax_1)
winter_df.groupby(['Country_Name','Total_Winter']).size().unstack().plot(kind='bar',ax=ax_2)
top_df.groupby(['Country_Name','Total_Medals']).size().unstack().plot(kind='bar',ax=ax_3)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/summer_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio)



# --------------
#Code starts here
data_1=data.iloc[:-1,:]
data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best=pd.DataFrame(data[data['Country_Name']==best_country])
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


