import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  df['male age'] = None
  df.loc[df["sex"] == 'Male', "male age"] = df["age"]
  average_age_men = round((df["male age"].mean()), 1)

  # What is the percentage of people who have a Bachelor's degree?
  se = df['education'].value_counts()
  sum_bachelors = se.loc['Bachelors']
  sum_high = se.loc['Bachelors'] + se.loc['Masters'] + se.loc['Doctorate']
  tot = len(df) 
  percentage_bachelors = round(((sum_bachelors/tot) *100), 1)

####rich dataframe
  rdf = df[df["salary"] == '>50K']

####rich dataframe

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  rdf['high ed'] = 0
  rdf.loc[rdf["education"] == 'Bachelors', "high ed"] = 1
  rdf.loc[rdf["education"] == 'Masters', "high ed"] = 1
  rdf.loc[rdf["education"] == 'Doctorate', "high ed"] = 1
  
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = rdf["high ed"].sum()
  lower_education = len(rdf) - higher_education

  tot_led = tot - sum_high

  # percentage with salary >50K
  higher_education_rich = round(((higher_education/sum_high) * 100),1)
  lower_education_rich = round(((lower_education/tot_led) * 100),1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df["hours-per-week"].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  df["num_min_workers"] = 0
  df.loc[(df["hours-per-week"] == 1), "num_min_workers"] = 1
  num_min_workers = df["num_min_workers"].sum()
  
  rdf["rich_num_min_workers"] = 0
  rdf.loc[(rdf["hours-per-week"] == 1), "rich_num_min_workers"] = 1
  rich_num_min_workers = rdf["rich_num_min_workers"].sum()
  
  rich_percentage = round(((rich_num_min_workers / num_min_workers) *100), 1)

  # What country has the highest percentage of people that earn >50K?
  
  country_count = df['native-country'].value_counts()
  rich_country_count = rdf['native-country'].value_counts()
  
  cdf = pd.merge(country_count, rich_country_count, left_index=True, right_index=True, how="outer")
  cdf = cdf.drop("?")
  cdf = cdf.rename(columns={"native-country_x": "all salaries", "native-country_y": ">50k"})
  cdf["rich percentage"] = (cdf[">50k"] / cdf["all salaries"]) * 100 

  highest_earning_country = cdf["rich percentage"].idxmax()
  highest_earning_country_percentage = round((cdf["rich percentage"].max()), 1)

  # Identify the most popular occupation for those who earn >50K in India.
  idf = rdf[rdf["native-country"] == 'India']

  occupation_count = idf['occupation'].value_counts()
 
  top_IN_occupation = occupation_count.idxmax()


  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count) 
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage':
      highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
