import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from streamlit_option_menu import option_menu
from sklearn.linear_model import LinearRegression

df = pd.read_csv("factors_of_women.csv")
st.set_page_config(layout="wide", page_icon= ":bar_chart:", page_title="Crimes Against Women",)
#st.dataframe(df)
st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: #333333 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

selected2 = option_menu(None, ["HOME", "CHARTS", "REASONS", "CHOROPLETH", "PREDICTION"], 
    icons=['house'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": \
            {"padding": "0vw!important",
             "background-color": "#e1e4e6",
             "align-items": "center",
             "justify-content": "center",
             "height": "auto",
             "width" : "100vw",
             "border-radius":"1vw",
             "border":"0.2vw solid #e1e4e6"},\
            
        "icon": \
            {"color": "#a9a9ab",
             "font-size": "1.3vw"},\
             
        "nav-link": \
            {"display" : "flex",
             "font-size": "1.3vw",
             "text-align": "center",
             "align-items": "center",
             "justify-contents": "center",
             "--hover-color": "#282829",
             "width":"15vw",
             "height": "2.5em",
             "margin-right" : "2em",
             "margin-left" : "1em",
             "color":"#818182",
             "box-shadow": "12px 12px 16px #777778, -8px -8px 12px #ffffff ",
             #"box-shadow": " 0 0 30px #595959", 
             #"box-shadow": " 20px 20px 50px #00d2c6, -30px -30px 60px #5e99ff"(only in dark theme this looks good)
             "border-radius":"1vw",
             "margin-bottom": "0",
             "margin-top": "0",
             "font-weight":"650"},\
            
        "nav-link-selected": \
            {"background-color": "#e1e4e6",
             "font-size" : "1.3vw",
             "font-weight":"600",
             "box-shadow": "2px 2px 5px #777778 inset, -3px -3px 5px #ffffff inset, 12px 12px 16px #777778, -8px -8px 12px #ffffff ",
             "color":"#585859",
            
             #"text-shadow": "0px 0px 1px #000000"
             },
        }
    )

 
#combined = df[df["STATES"]]

#selected2 = st.selectbox("Menu", (["Homepage", "Histogram", "Geo Plot", "Reasons Analysis", "Prediction"]))

if selected2 == 'HOME':
    col1, col2 = st.columns([3,1])
    col1.markdown("<h1 style = 'color : #6f6f70;'>Crime Against Females in India: Data Analysis Dashboard</h1>\
    <p style = 'color : #a9a9ab;'>Welcome to this data analysis project, exploring the critical issue of crime against females in India. This project delves into a comprehensive examination of crime statistics spanning a decade, from 2011 to 2021, across all 28 States and 8 Union Territories of India.</p>\
    <h4 style = 'color : #a9a9ab;'><u>Understanding the Issue:</u></h4>\
    <p style = 'color : #a9a9ab;'>Crime against females is a pressing concern in our society, and this project aims to shed light on the trends, patterns, and underlying factors behind these incidents. By harnessing the power of data analysis, we seek to not only visualize the data but also provide valuable insights to raise awareness and inform potential solutions.</p>\
    <h4 style = 'color : #a9a9ab;'><u>Motive :</u></h4>\
    <p style = 'color : #a9a9ab;'>The main motive behind this project is to leverage data to empower informed decisions and foster a safer environment for females across India. By providing a user-friendly interface and rich visualizations, I aim to bridge the gap between data and public awareness.</p>\
    <h4 style = 'color : #a9a9ab;'><u>Key Features Of this Analysis:</u></h4>\
    <p style = 'color : #a9a9ab;'>1. In-Depth Analysis: Dive into the numbers and uncover meaningful patterns, such as regional variations and changes over the years.</p>\
    <p style = 'color : #a9a9ab;'>2. Interactive Visualizations: Engage with interactive plots created using Plotly to grasp the information intuitively</p> <p style = 'color : #a9a9ab;'>3. Data-Driven Insights: Discover key takeaways and actionable insights to address this societal issue.</p>\
    <h4 style = 'color : #a9a9ab;'>Data source:</h4>\
    <p style = 'color : #a9a9ab;'>The dataset for this project on female crime statistics in India (2011-2021) was sourced from Kaggle and National Crime Records Bureau, the Kaggle dataset was contributed by <a href = 'https://www.kaggle.com/datasets/sailajamahapatro/crimes-against-women-from-2011-2021-in-india'>Sailaja Mahpatro</a>. The NCRB data was mostly used to check kaggle dataset's credibility, and to add additional data. </p>", unsafe_allow_html= True)
    
    col2.markdown("<h1> Streamlit App By <a href = 'https://www.linkedin.com/in/shivam-sai-kiran/'>Sai Kiran</a></h1>", unsafe_allow_html= True)

    col2.expander(label="You can click here to have a look at the raw data first :point_down:").dataframe(df)
    
    

elif selected2 == 'CHARTS':
    
    

    # Create a multiselect widget to select states
    radio_options = st.sidebar.radio("zone wise data", options= (["None", "All States  &  UT", "North India", "West India", "South India" , "East India","Union Territories"]))
    
    unique_states =[]
    #unique_data = df[df["YEAR"].unique()]
    #st.write = unique_data
    message = ""
    
    if radio_options == "All States  &  UT" :
        unique_states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
        'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
        'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
        'Uttarakhand', 'West Bengal', 'A & N Islands', 'Chandigarh',
        'D&N Haveli', 'Daman & Diu', 'Delhi UT', 'Lakshadweep',
        'Puducherry', 'Ladakh']
        
        
        
    if radio_options == "North India":
        unique_states = ['Jammu & Kashmir', 'Ladakh', 'Himachal Pradesh', 'Punjab', 'Chandigarh', 'Uttarakhand', 'Haryana', 'Delhi UT', 'Uttar Pradesh']
        
        message = "<h5> Key Takeaways <h5>"+"<p>1. Ladakh was oringnally a Part of Jammu and Kashmir, and it was not until recently (Oct 2019), Ladakh was declared as an official Union Territory. This is the reason why there appears to be no cases of crime against Women until 2020." + "<br><br>" + "2. The reasons why cases in Union Territories are substancially lower compared to different states is because of the population which ranges from 60k to 1M across the Union Territories which when compared to states like Andhra Pradesh or Karnataka, is nearly 1000X lower, resulting in a much lower crime rate. "
        

        
    if radio_options == "West India" :
        unique_states = ['Maharashtra', 'Goa', 'D&N Haveli', 'Daman & Diu', 'Gujarat', 'Madhya Pradesh', 'Rajasthan']

        
    if radio_options== "South India":
        unique_states = ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Puducherry', 'Lakshadweep', 'Tamil Nadu', 'A & N Islands', 'Telangana']


        
        #def line_conditions(radio_options, filtered_data):
        
        message = "<h5> Key Takeaways <h5>"+"<p>1. You will notice how the the state Telangana has 0 cases up till the year 2013, This is somewhat true, because the predominantly Telgu - speaking region was orignally a part of the state Andhra Pradesh, and it was not until june 2014 when the Telangana region was declared as an official state." + "<br><br>" + "2. The reasons why cases in Union Territories are substancially lower compared to different states is because of the population which ranges from 60k to 1M across the Union Territories which when compared to states like Andhra Pradesh or Karnataka, is nearly 1000X lower, resulting in a much lower crime rate. "
        
    if radio_options == "East India":
        unique_states = ['Arunachal Pradesh', 'Assam', 'Bihar', 'Sikkim', 'Nagaland', 'Manipur', 'Meghalaya', 'Mizoram', 'Tripura', 'West Bengal', 'Jharkhand', 'Odisha', 'Chandigarh']
        
    if radio_options == "Union Territories":
        unique_states = ['Puducherry', 'Ladakh', 'A & N Islands', 'Lakshadweep', 'Daman & Diu', 'Delhi UT', 'Chandigarh', 'Jammu & Kashmir']

        
        
        

    selected_states = st.sidebar.multiselect("Select States", df["STATES"].unique(), default = unique_states)
    

    if radio_options == "None" and len(selected_states) == 0:
        st.header("Tips :")
        st.markdown('<p> 1. You can select the zones you want to display using the radio buttons on the left.<br> \
        2. To manually choose the states, you may use the selection tool "Select States" under the radio buttons. Thru this you can chose either single or multiple states.<br> \
        3. When viewing the bar chart, you may click and drag over the desired segment to display a much smaller segment of the entire data. <br> \
        4. To know which contry the bar represents, simply hover over it. <br> 5. Take your time and go through all the zones and states and compare it with each other states for a better unserstanding.', unsafe_allow_html= True)
    else :
        st.title("Interactive Histogram of Total Crimes Against Women by Year")
        
        
    # Filter data based on selected states
    filtered_data = df[df["STATES"].isin(selected_states)]

    # If no states are selected, show a message
    if len(selected_states) == 0:
        st.info("Please select at least one state.")
    else:
        # Create a Plotly histogram using px.histogram
        fig = px.bar(
            filtered_data,
            x="YEAR",
            y= "Total Crimes Against Women",
            #nbins=20,
            color="STATES",
            title="Histogram of Total Crimes Against Women",
            barmode = 'group',
            height = 500,
            width = 1200,
            hover_name= "STATES",
            hover_data= "Total Crimes Against Women"
        )
        
        # Display the Plotly chart using st.plotly_chart
        st.plotly_chart(fig)
        

        
        if radio_options != "None" and radio_options != "All States  &  UT":
            #filtered_data = df[df["STATES"].isin(unique_states)]
            if len(message) != 0:
                st.expander("See explanation", expanded = True).markdown(message, unsafe_allow_html=True)
            line = px.line(
                filtered_data,
                x = "YEAR",
                y = "Total Crimes Against Women",
                color = "STATES",
                width= 1200,
                height = 500,
                render_mode="svg",
                line_shape="spline"
                
            )
            st.plotly_chart(line)
        
        elif radio_options =="All States  &  UT":
            consolidated = df.groupby('YEAR')['Total Crimes Against Women'].sum().reset_index()
            state_consolidated = df.groupby("STATES")["Total Crimes Against Women"].sum().reset_index()

            ################################################################
            bar_desc = px.bar(
                state_consolidated,
                x = 'Total Crimes Against Women', 
                y='STATES',
                height= 900,
                width= 800,
                orientation='h')
            bar_desc.update_layout(yaxis={'categoryorder':'total ascending'})
            
            
            line2 = px.line(
                consolidated, 
                x='YEAR', y='Total Crimes Against Women', 
                title='Crimes Against Women in India with Rangeslider',
                height= 650,
                width = 800,
                
                )
            

            line2.update_xaxes(rangeslider_visible=True)
            col1, col2 = st.columns([3,1])
            
            col1.plotly_chart(line2)
            with col2:
                with st.expander(label="Explaination", expanded = True):
                    st.write("From 2011 - 2021 the crime rates have gradually gone up, In 2011 the total crime against Females were 228k and by the end of 2021 the cases have rose up to 428k, That is almost double the cases since 2011")
            col3, col4 = st.columns([5,2])   
            col3.plotly_chart(bar_desc)
            with col4:
                with st.expander(label="Explaination", expanded = True):
                    st.write("\n * This desending bar chart is the visualisation of 10 yrs worth data, totaling the crime rates for each states. \n * Here we can notice that Uttar Pradesh has the Highest number of crimes against Women totaling to 482k ")
                
                
                        
    ################################################
    
    #################################################
    
    # This section is for the Choropleth maps for 
    
    ################################################
elif selected2 == "CHOROPLETH" :
    
    indian_states = json.load(open('india_states.geojson', 'r'))
        
    selected_year = st.sidebar.selectbox("Select year", df["YEAR"].unique())

    #state_id_map = {json.load(open('state_id_map.json', 'r'))}
    state_id_map = {}

    #state_id_map = json.load(open('state_id_map.json','r'))
    for feature in indian_states['features']:
        feature['id'] = feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']] = feature['id']
    #def yearMap(year):
        # Filter data based on selected Years
    filter_df = df[df["YEAR"] == selected_year] #filtered_data = filter_df
    
    if selected_year == 2020 or selected_year == 2021:
        filter_df = df[df["STATES"] != "Ladakh"]
        
    filter_df['id'] = filter_df['STATES'].apply(lambda x : state_id_map[x])

        
    filter_df["text"] = df['STATES'].astype(str) + "<br>" + \
        "Crimes Against Women : " + df['Total Crimes Against Women'].astype(str)
    
    
    st.title("Crime Against Women Intensity Map")
    

        
        
    fig2 = px.choropleth(
        filter_df, 
        locations= 'id', 
        geojson= indian_states,
        title = selected_year.astype(str),
        color = 'Total Crimes Against Women', 
        scope = "asia",
        hover_name = filter_df["STATES"],
        #hover_data= ["Total Crimes Against Women"]
        color_continuous_scale="OrRd",
        width = 900,
        height = 700,
            
        )
    fig2.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
    fig2.update_traces(hovertemplate = filter_df["text"], marker_line_color='black')

    fig2.update_geos(fitbounds = 'locations', visible = False)
    
    col1, col2 = st.columns([4,1])
    
    col1.plotly_chart(fig2)
    
    col2.markdown("<h5>Tips :</h5><br>1. This crime intensity map is used for a more insightful observation on the spread of cases across different states <br><br> 2. Hover over the states to view its total cases on 'Crimes Against Women' for that year <br><br> 3. Intensity map of each year is available, select the years using selection tool on the sidebar, however, the map may take time loading. ", unsafe_allow_html=True)
    
    
    ############################################################################
    # The Reasons why it happened
    
    ############################################################################
    
    
elif selected2 =="REASONS":
    reason_radio = st.sidebar.radio(label ="Selection:", options=(["None","All Years","Individual Year Charts"]))
    
    if reason_radio == "None":
        
        st.header("Tips :")
        st.markdown('<p> 1. The Analysis on the "Reasons" are 100% genuine and the data has been cross verfied by using the official data from National Crime Records Bureau (govt agency).<br> \
        <br>2. There are 2 sections, All Years and Individual Years, and their contents are as follows :\
        <li> The "All Years" section will allow you to see the analytical visuals for the combined 10 year dataframe.</li>\
        <li> The "Individual Years" section will allow you to select individual years form 2011 to 2021 and display their charts.</li><br>\
        3. Take your time and go through all the provided selections to get the most of this Project.<br><br>', unsafe_allow_html= True)
        
        st.info("Use the radio buttons to display the analysis of reasons across states and years.")
    
    ###################################################################
    
    def consolidated(column):
        consolidated_data = df.groupby(column)[["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"]].sum().reset_index()
        
        return consolidated_data
        

    
    #consolidated_year = df.groupby('STATES')[["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"]].sum().reset_index()
    
    #consolidated_states = df.groupby('YEAR')[["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"]].sum().reset_index()
    #consolidated(df["STATES"])
    
    df_melted = pd.melt(consolidated("STATES"), id_vars=['STATES'], value_vars=["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"], var_name='CRIME TYPE', value_name='VALUE')
    

    crime_type_total = df_melted.groupby('STATES')['VALUE'].sum().reset_index()


    df_combined = df_melted.merge(crime_type_total, on='STATES', how='left')
    df_melted['PERCENTAGE'] = ((df_combined['VALUE_x'] / df_combined['VALUE_y'])*100).round(1)
    
    #df_melted['PERCENTAGE'] = (df_melted['VALUE'] / df_melted['VALUE_TOTAL']) * 100
    if reason_radio == "All Years":
        
        #c = st.container()#############################

        melted = pd.melt(consolidated("YEAR"), id_vars=['YEAR'], value_vars=["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"], var_name='CRIME TYPE', value_name='VALUE')

        desc_crime = melted.groupby("CRIME TYPE")["VALUE"].sum().reset_index()
        
        sunburst = px.sunburst(
            df_melted, 
            path=['STATES', 'CRIME TYPE'], 
            values='PERCENTAGE', 
            title='Crime Data Sunburst Chart',
            height= 600,
            width= 700
            )
        
        col1, col2 = st.columns([4,2])
        col1.plotly_chart(sunburst)
        
        with col2:
                with st.expander(label="Explaination", expanded = True):
                    st.write("\n * This is a SunBurst chart, it displays all the states & UTs with its corresponding crime types and its percentage \n * If you wish to see the spread of crime type according to their precentages, simply click on the state/UT. \n * The total values and percentages displayed is the concatination of the data from year 2011 to 2021. \n * Hope you don't get overwhelmed by the sunburst chart.  ")
            
        bar_desc = px.bar(
            desc_crime,
            x = 'VALUE', 
            y= 'CRIME TYPE',
            height= 500,
            width= 700,
            orientation='h')
        bar_desc.update_layout(yaxis={'categoryorder':'total ascending'})
        
        with st.expander(label= "Pie Chart", expanded= True):
            pie = px.pie(
                desc_crime,
                values= "VALUE",
                names= "CRIME TYPE",
                width = 600,
                height = 500
                )
            col1, col2 = st.columns([3,2])
            col1.plotly_chart(pie) 
            col2.write("\n * As you can see the highest cases on crimes against Females in these 10 years are registered under Domestic violence\n * Domestic violence alone contributes 37% to the entire cases. \n * Human trafficking has the lowest percentage of 0.15% which is 250x lower than Domestic violence. \n * The total values and percentages displayed is the concatination of the data from year 2011 to 2021  ")
                          
        
        col3, col4 = st.columns([4,2])
        
        col3.plotly_chart(bar_desc)
        
        with col4:
            with st.expander(label="Explaination", expanded = True):
                st.write("\n * This Descending Bar chart represents the highest to lowest crime types, the highest being on top and the subsequent lower ones under it \n * The total values and percentages displayed is the concanitation of the data from year 2011 to 2021.")
            
        
    if reason_radio == "Individual Year Charts":
        
        st.expander(label= "Notes", expanded= True).write("* The Bar graph displays only the maximum occured crime type for that particular state. \n * The pie chart uses the consolidated total crime cases for each type of crime for that year.\n \n_")
        selected_year2 = st.sidebar.selectbox("Select year", df["YEAR"].unique())
        
        filter_df = df[df["YEAR"] == selected_year2] #filtered_data = filter_df
        
        df_melted = pd.melt(filter_df, id_vars=['STATES',"YEAR"], value_vars=["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"], var_name='CRIME TYPE', value_name='VALUE')

        #pie = px.pie(df, values='pop', names='country', title='Population of European continent')
        max_crm = df_melted.groupby(["STATES"])['VALUE'].idxmax()
        crm_typ = df_melted.loc[max_crm].reset_index(drop=True)
        

        
        bar2 = px.bar(
            crm_typ,
            x="STATES",
            y= "VALUE",
            #nbins=20,
            color="CRIME TYPE",
            title="Reasons Behind Crimes Against Women :",
            #text= "CRIME TYPE",
            height = 500,
            width = 1300,
            hover_name= "CRIME TYPE" 
        )
        bar2.update_traces(textposition = "outside", textangle = -90)
        
        st.plotly_chart(bar2)
        
        df_melted2 = pd.melt(consolidated("YEAR"), id_vars=['YEAR'], value_vars=["RAPE","KIDNAP & ABDUCTION","DOWRY DEATHS","CRUETLY BY HUSBAND OR HIS RELATIVES","HUMAN TRAFFICKING","ASSAULT ON MODESTY","SEXUAL HARRASSMENT","OTHERS"], var_name='CRIME TYPE', value_name='VALUE')
        
        filter2 = df_melted2[df_melted2["YEAR"] == selected_year2]
        
        pie = px.pie(
            filter2,
            values= "VALUE",
            names= "CRIME TYPE",
            width = 600
            )
    
        st.plotly_chart(pie)
        
        
        
        #pie = px.pie(df, values='pop', names='country', title='Population of European continent')
    
    
    
    
    
    
    ##############################################################
    # Prediction Section
    # This is the prediction section where we gonna be using a simple regression model to predict the crimes against women in coming years
    
    ##############################################################
    
    
elif selected2 == "PREDICTION" : 
    
    st.sidebar.write("REGRESSION TRAINING")
    disp_typ = st.sidebar.toggle("Individual States")
    
    pre_df = df.groupby('YEAR')['Total Crimes Against Women'].sum().reset_index()
    
    if disp_typ == True:
        
        selected_state = st.sidebar.selectbox("Select year", df["STATES"].unique())
        pre_df = df[df["STATES"]==selected_state][["YEAR","Total Crimes Against Women"]]
        st.expander(label="Note:", expanded=True).write("* There are outliers in the individual state charts so you have to select a year range for training which excludes the outliers.\n")
    
    
    st.title("Prediction of Crime Against Women For The Coming Years")
    
    #pre_df = df[["STATES", "YEAR", "Total Crimes Against Women"]]
    start_yr, end_yr = st.sidebar.select_slider('Select the range of Years for training', options=pre_df["YEAR"], value=(2016, 2021))
    
    
    future_years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
    
    
    
    slider_years = future_years[future_years.index(start_yr)::]
    
    slider_df = pre_df[(pre_df['YEAR'] >= start_yr) & (pre_df['YEAR'] <= end_yr)]
    
    x2 = slider_df["YEAR"].values.reshape(-1, 1)
    y2 = slider_df["Total Crimes Against Women"]
    
    model2 = LinearRegression()
    model2.fit(x2, y2)

    # Split the data into features (X) and target (y)
    x = pre_df['YEAR'].values.reshape(-1, 1)
    y = pre_df["Total Crimes Against Women"]

    # Train a Linear Regression Model
    model = LinearRegression()
    model.fit(x, y)

    # Make Predictions for Future Years
    
    def prediction(future_years, model):
        
        predicted_rates = model.predict(np.array(future_years).reshape(-1, 1))

        # Create a DataFrame with predicted data
        predicted_data = pd.DataFrame({'Year': future_years, 'PredictedCrimeRate': predicted_rates})

        return predicted_data
    
    # Concatenate the original data and predicted data
    predicted_data = prediction(future_years, model)
    combined_data = pd.concat([pre_df, predicted_data])

    predicted_data2 = prediction(slider_years, model2)
    # Create a scatterplot with Plotly Express
    
    # function for the linear regression chart and the trend lines
    def plotRegress(c_data, c_data2, p_data, p_data2, p2_data, p2_data2):
    
        regr = go.Figure()
        regr.add_trace(go.Scatter(
            x = c_data,        #x=combined_data["YEAR"],
            y = c_data2,       #y=combined_data["Total Crimes Against Women"],
            mode='markers',
            name='Total Cases',
            marker_size = 15
        ))
        if disp_typ == False:
            
            regr.add_trace(go.Scatter(
                x = p_data,          #x=predicted_data["Year"],
                y = p_data2,         #y=predicted_data['PredictedCrimeRate'],
                mode='lines',
                name='Best Fit for the entire dataset',
                line=dict(color='red'),
            )).update_traces(line = {'width' : 4})

        # Add the regression line to the scatterplot
        regr.add_trace(go.Scatter(
            x = p2_data,            #x=predicted_data2["Year"],
            y = p2_data2,           #y=predicted_data2['PredictedCrimeRate'],
            mode='lines',
            name='Best fit for the custom years data',
            line=dict(color='green')
        )).update_traces(line = {'width' : 4})
        
        return regr
    
    c_data = combined_data["YEAR"]
    c_data2 = combined_data["Total Crimes Against Women"]
    
    p_data = predicted_data["Year"]
    p_data2 = predicted_data['PredictedCrimeRate']
    
    p2_data = predicted_data2["Year"]
    p2_data2 = predicted_data2['PredictedCrimeRate']
    
    
    regr = plotRegress(c_data, c_data2, p_data, p_data2, p2_data, p2_data2)
    
    regr.update_layout(
        title='Crime Rate Over Time with Linear Regression Prediction',
        xaxis_title='Year',
        yaxis_title='Total Crimes Against Women',
        width=1150,
        height=700,
    )
    st.plotly_chart(regr)
    
    def prd_value(year):
        values = (predicted_data2.loc[predicted_data2['Year'] == year, 'PredictedCrimeRate'].values[0]).round(1)
        
        res = '{:,}'.format(values)
        return res
        
    st.markdown(f"<h3 style='text-align: center;'> Crime cases for the coming years are as follows :</h3><br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"<h5 style='text-align: left;'>Cases in 2024 :</h5><h2 style='text-align: left; color: red;color: red;'>{prd_value(2024)}</h2>", unsafe_allow_html=True)
    
    col2.markdown(f" <h5 style='text-align: center;'>Cases in 2025 :</h5> <h2 style='text-align: center; color: red;'>{prd_value(2025)}</h2>", unsafe_allow_html=True)
    col3.markdown(f"<h5 style='text-align: right;'>Cases in 2026 :</h5><h2 style='text-align: right; color: red;'>{prd_value(2026)}</h2> ", unsafe_allow_html=True)
    

    ######################################################################
    #fig.add_trace(px.line(predicted_data2, x='Year', y='PredictedCrimeRate').data[0], )
    
    #fig.update_traces(marker_size = 20, line=dict(color='green'), name = "green line")
    

    # Show the plot
    
    
    
    
    