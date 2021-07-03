import pandas as pd 

ind_cty=pd.read_csv("D:\\BLR10AM\\Assi\\Python Problem Statements\\Python Problem Statements\\Indian_cities.csv")
ind_cty.columns
######a)	Find out top 10 states in female-male sex ratio


group_data1 = ind_cty.groupby('state_name').mean()

f_m_ratio =group_data1[['sex_ratio']].sort_values('sex_ratio', ascending=False).head(10)                                            
f_m_ratio



#######b)	Find out top 10 cities in total number of graduates


top_graduates = ind_cty.sort_values('total_graduates', ascending=False)

top_grad_city = top_graduates['name_of_city'].head(10)

top_grad_city


########c)	Find out top 10 cities and their locations in respect of  total effective_literacy_rate.



top_eff_lit = ind_cty.sort_values('effective_literacy_rate_total',ascending=False)


top_city_loc =top_eff_lit[['name_of_city','location']].head(10)
top_city_loc



###############2

##a)Construct histogram on literates_total and comment about the inferences


import matplotlib.pyplot  as plt

plt.hist(ind_cty['literates_total']);plt.show()  

##b)	Construct scatter  plot between  male graduates and female graduates       


plt.scatter(ind_cty['male_graduates'] ,ind_cty['female_graduates']) 
plt.show()


################3

#a)	Construct Boxplot on total effective literacy rate and draw inferences

plt.boxplot(ind_cty['effective_literacy_rate_total'])


#b)	Find out the number of null values in each column of the dataset and delete them.

ind_cty.isna().sum()





