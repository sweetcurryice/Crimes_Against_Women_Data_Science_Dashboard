# Crimes Against Women in India (2011 - 2021) - A Data Science Project

------------------------------------------------------------------------

## Project Description

Welcome to this data Science project, exploring the critical issue of crime against females in India. This project delves into a comprehensive examination of crime statistics spanning a decade, from 2011 to 2021, across all 28 States and 8 Union Territories of India. It aims to leverage data to empower informed decisions and foster a safer environment for females across India. By providing a user-friendly interface and rich visualizations, The motive is to bridge the gap between data and public awareness.

--------------------------------------------------------------------------------

## Getting Started

To run this project on your local machine, follow these steps:

1. Clone this repository: `git clone https://github.com/sweetcurryice/Crimes_Against_Women_Data_Science_Dashboard`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run this code on the treminal : `streamlit run streamlit_app.py`
4. Or if you simply want to view this project on your browser : [`https://crimes.streamlit.app/`](https://crimes.streamlit.app/)

------------------------------------------------------

## Data Sources

- [Dataset 1](https://www.kaggle.com/datasets/sailajamahapatro/crimes-against-women-from-2011-2021-in-india): This was sourced from Kaggle and was  contributed by Sailaja Mahpatro.
- [Dataset 2](https://data.gov.in/resource/stateuts-wise-indian-penal-code-ipc-crimes-special-local-laws-sll-crimes-against-women): This Dataset was sourced from data.gov.in. which is owned and managed by the Government of India

--------------------------------------------------------------------------

## Data Preprocessing

- **Data cleaning :** The main dataset in use was rigged with misplaced values, and to fix this i used additional dataset sourced by the [Dataset 2].
- **Data Transformation :** Used Pandas for the transformation of data to fit its values in the Linear Regression Model and analytics charts.
- **Data validation :** The already prepared dataset from kaggle was verfied using the data from the National Crime Records Bureau website.

-----------------------------------------------------------------

## Data Analysis

1.  **Exploratory Data Analysis (EDA):**
    - **Data Selection:** Allowing users to choose between viewing data for individual states or the entire dataset. This interactive feature can help users focus on specific aspects of the data.
    - **Data Range Selection:** Users can select a range of years for training the linear regression model. This interactive feature provides flexibility for exploring the impact of different timeframes on model performance.
    - **Visualization:** Created multiple visualizations using charts such as bar, line, sunburst, choropleth, pie, and also integrated scatterplot with linear regression trend lines to visualize the crime rate over time .
<br>

2.  **Modeling**:

    - **Linear Regression:** I have used the LinearRegression model from scikit-learn to perform linear regression. This model aims to establish a linear relationship between the year (independent variable) and the total crimes against women (dependent variable).

    - **Custom Year Selection:** Users can select a specific range of years for training the model. This approach allows for personalized analysis, as users can focus on different timeframes based on their interests.

    - **Prediction:** predictions for future years are made based on the trained model. These predictions provide insights into the expected crime rates for the selected timeframe.
<br>

3. **Results:**

    - **Interactive Data Exploration:** Users can interactively explore the data by selecting individual states, choosing a training year range, and visualizing trends. This interactivity enhances user engagement and allows for a more in-depth analysis.

    - **Linear Regression Trend Lines:** The application provides linear regression trend lines for both the entire dataset and the custom years. These trend lines visually represent the model's predictions and allow users to assess the fit of the model.

    - **Outlier Handling:** This application displays the presence of outliers in the data, and gives control to the users to exclude them when selecting a training year range. This suggests an awareness of data quality and the importance of outlier detection and handling.

-----------------------------------------------------------------------------------------

## Results

1. Where there dorps in cases for any particular year, if yes then what caused the overall crime rates to drop in that year?
    
    - Yes, and I found out that in the year 2020, the cases had dropped by **8.5%** compared to 2019, and this kinda drop has not been witnessed elsewhere in this data, the reason behind this drastic drop was because of the Tragic **COVID-19** Pandemic, Lockdown had caused cases to drop, though the drop in just a particular type of crime is unseen, implying that all of the types of crime were decreased somewhat equally.
<br>

2. What would the total cases in 2024, 2025, 2026 be?

    - The prediction for future year cases were done using Linear regression model, and they are as follows:

        - cases in **2024** = **478,622.6**
        - cases in **2025** = **496,153.5**
        - cases in **2026** = **513,684.5**
<br>

3. What are the Highest and Lowest crime types, and how much do they deffer from each other?

    - The Highest crime type in these past 10 yrs is ***Domestic Violence***, accounting upto **1.25 Million cases**
    - The Lowest is ***Human Trafficking*** with **5,067 cases**
    - Domestic violence is **250x** (24,610%) greater than Human Trafficking, and Domestic violence alone contributes **37%** to the total crimes commited against women.
------------------------------------------------------

## Conclusion

The findings of this data science project paint a sobering picture of safety and security for females within the confines of their own homes. It is evident from the comprehensive analysis of crime data that domestic violence emerges as the most prevalent and alarming crime type, surpassing all other categories.

What is even more concerning is that this data reveals an unsettling trend: crime cases against women in India are not only persisting but also on a distressing upward trajectory. Each year, the numbers break their own records, serving as a stark reminder of the magnitude of this issue.

The data unequivocally underscores the urgent need for societal awareness, policy reform, and support systems to address the deeply concerning issue of domestic violence and other crimes against women. While the project focused on data analysis and presentation, it is crucial to remember that behind these statistics lie the lives of countless women who experience physical, emotional, and psychological harm within their own households.

To truly make progress and enhance the safety of females, it is imperative to translate these data-driven insights into concrete actions. This may include strengthened legal frameworks, increased access to support services, and widespread educational campaigns to challenge and change prevailing societal norms.

In conclusion, the data leaves us with an undeniable truth: females are not as safe as they should be in their own homes, and it is a collective responsibility to work towards a future where every woman can live without fear, free from the threat of domestic violence. This project serves as a call to action, emphasizing the urgency of addressing this critical issue and safeguarding the well-being of women across our society.

-----------------------------------------------------------

## Contact Information

Feel free to reach out to me via [Email](mailto:shivamsaikiran111@gmail.com) or on [LinkedIn](https://www.linkedin.com/in/shivam-sai-kiran-030745210/).

----------------------------



© 2023 Shivam Sai Kiran. This project is licensed under the [MIT License](License.txt).
