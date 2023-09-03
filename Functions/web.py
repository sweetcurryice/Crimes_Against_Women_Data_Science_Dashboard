import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json

df = pd.read_csv(r"../Functions/factors_of_women.csv")
st.set_page_config(layout="wide", page_icon="penguin", page_title="Crimes Against Women")
#st.dataframe(df)
st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: #7bbcd4 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

#combined = df[df["STATES"]]

menu_selection = st.selectbox("Menu", (["Homepage", "Histogram", "Geo Plot", "Reasons Analysis", "Prediction"]))

if menu_selection == 'Homepage':
    
    st.markdown("<h3> Hello, Welcome to my data analysis dashboard<h3>", unsafe_allow_html= True)
    st.dataframe(df)
    

elif menu_selection == 'Histogram':
    
    

    # Create a multiselect widget to select states
    radio_options = st.sidebar.radio("zone wise data", options= (["None", "All States", "North India", "West India", "South India" , "East India"]))
    
    unique_states =[]
    
    
    if radio_options == "All States" :
        unique_states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
        'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
        'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
        'Uttarakhand', 'West Bengal', 'A & N Islands', 'Chandigarh',
        'D&N Haveli', 'Daman & Diu', 'Delhi UT', 'Lakshadweep',
        'Puducherry']
    if radio_options == "North India":
        unique_states = ['Jammu & Kashmir', 'Himachal Pradesh', 'Punjab', 'Chandigarh', 'Uttarakhand', 'Haryana', 'Delhi UT', 'Uttar Pradesh']
        
    if radio_options == "West India" :
        unique_states = ['Maharashtra', 'Goa', 'D&N Haveli', 'Daman & Diu', 'Gujarat', 'Madhya Pradesh', 'Rajasthan']
        
    if radio_options== "South India":
        unique_states = ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Puducherry', 'Lakshadweep', 'Tamil Nadu', 'A & N Islands', 'Telangana']
        
        with st.expander("See explanation"):
            st.markdown("<h5> Key Takeaways <h5>"+"<p>1). You will notice how the the state Telangana has 0 cases up till the year 2013, This is somewhat true, because the predominantly Telgu - speaking region was orignally a part of the state Andhra Pradesh, and it was not until june 2014 when the Telangana region was declared as an official state." + "<br><br>" + "2). The reasons why cases in Union territories are substancially lower compared to different states is because of the population which ranges from 60k to 1M across the Union Territories which when compared to states like Andhra Pradesh or Karnataka, its nearly 1000X lower, resulting in a much lower crime rate. ", unsafe_allow_html= True)
        
    if radio_options == "East India":
        unique_states = ['Arunachal Pradesh', 'Assam', 'Bihar', 'Sikkim', 'Nagaland', 'Manipur', 'Meghalaya', 'Mizoram', 'Tripura', 'West Bengal', 'Jharkhand', 'Odisha', 'Chandigarh']
        
        
        

    selected_states = st.sidebar.multiselect("Select States", df["STATES"].unique(), default = unique_states)
    

    if radio_options == "None" and len(selected_states) == 0:
        st.header("Tips :")
        st.markdown('<p> 1. You can select the zones you want to display using the radio buttons on the right.<br> \
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
            width = 1300,
            hover_name= filtered_data["STATES"],
            hover_data= filtered_data.rename(columns = {"tot": "Total Crimes Against Women"}, inplace = True)
        )
        
        # Display the Plotly chart using st.plotly_chart
        st.plotly_chart(fig)
    
    ################################################
    
    #################################################
    
    # This section is for the Choropleth maps for 
    
    ################################################
elif menu_selection == "Geo Plot" :
    
    indian_states = json.load(open('india_states.geojson', 'r'))
        
    selected_year = st.sidebar.selectbox("Select year", df["YEAR"].unique())

    state_id_map = {}
    for feature in indian_states['features']:
        feature['id'] = feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']] = feature['id']
        
    #def yearMap(year):
        # Filter data based on selected Years
    filter_df = df[df["YEAR"] == selected_year] #filtered_data = filter_df
    filter_df['id'] = filter_df['STATES'].apply(lambda x : state_id_map[x])

        
        
    filter_df["text"] = df['STATES'].astype(str) + "<br>" + \
        "Crimes Against Women : " + df['tot'].astype(str)
    
    filter_df.rename(columns = {"tot": "Total Crimes Against Women"}, inplace = True)
    
    
    st.title("Crime Against Women Intensity Map")
        
        
    fig2 = px.choropleth(
        filter_df, 
        locations= 'id', 
        geojson= indian_states,
        title = selected_year.astype(str),
        color = 'Total Crimes Against Women', 
        scope = "asia",
        hover_name = filter_df["STATES"],
        #hover_data = ["Total Crimes Against Women"],
        height = 800,
        width = 1000,
        color_continuous_scale="OrRd",
            
        )
    fig2.update_traces(hovertemplate = filter_df["text"])

    fig2.update_geos(fitbounds = 'locations', visible = False)
    st.plotly_chart(fig2)
    
    
    ############################################################################
    # The Reasons why it happened
    
    ############################################################################
    
    
elif menu_selection =="Reasons Analysis":
    st.header("You would be wondering what are the reasons and motive behind these criminal cases, here we will list out and analyse the the criminal acts which lead to these cases")
    
    
    
    
    
    ##############################################################
    # Prediction Section
    # This is the prediction section where we gonna be using a simple regression model to predict the crimes against women in coming years
    
    ##############################################################
    
    
elif menu_selection == "Prediction" : 
    st.title("Prediction of Crime Against Women For The Coming Years")
    
    
    
    
    