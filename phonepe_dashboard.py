import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="PhonePe Dashboard",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for PhonePe theme
st.markdown("""
<style>
    .main {
        background-color: #e1e6eb;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #e1e6eb;
        border: 2px solid #259f35;
        border-radius: 8px;
        color: #259f35;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #259f35;
        color: white;
    }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #259f35 0%, #001a66 100%);
        padding: 20px;
        border-radius: 8px;
        color: white;
    }
    div[data-testid="metric-container"] label {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Chart data
charts_data = {
    "chart1_user_trend": {
        "labels": ["2022-Q1", "2022-Q2", "2022-Q3", "2022-Q4", "2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4", "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"],
        "users": [372.9, 393.4, 414.3, 433.9, 453.9, 472.4, 491.4, 509.4, 530.1, 550.3, 568.0, 586.8],
        "app_opens": [15.72, 17.79, 19.22, 21.26, 22.93, 24.93, 27.22, 29.94, 32.63, 35.41, 38.13, 40.42]
    },
    "chart2_top_states_users": {
        "labels": ["Haryana", "Madhya Pradesh", "Tamil Nadu", "Telangana", "West Bengal", "Rajasthan", "Andhra Pradesh", "Karnataka", "Uttar Pradesh", "Maharashtra"],
        "values": [368.1, 470.7, 506.5, 524.6, 525.0, 555.8, 556.7, 733.7, 942.3, 1140.1]
    },
    "chart3_trans_treemap": {
        "labels": ["Financial Services", "Merchant payments", "Others", "Peer-to-peer payments", "Recharge & bill payments"],
        "values": [14.2, 6533.99, 17.43, 26652.74, 1333.88]
    },
    "chart4_top_states_trans": {
        "labels": ["Odisha", "West Bengal", "Bihar", "Madhya Pradesh", "Rajasthan", "Uttar Pradesh", "Andhra Pradesh", "Maharashtra", "Karnataka", "Telangana"],
        "values": [1226.4, 1558.42, 1790.13, 1912.53, 2634.32, 2688.52, 3466.91, 4037.42, 4067.87, 4165.6]
    },
    "chart5_trans_pie": {
        "labels": ["Financial Services", "Merchant payments", "Others", "Peer-to-peer payments", "Recharge & bill payments"],
        "values": [142018823748.86, 65339877098473.63, 174280662903.38, 266527358952424.06, 13338759427748.797]
    },
    "chart6_quarterly_trend": {
        "labels": ["2022-Q1", "2022-Q2", "2022-Q3", "2022-Q4", "2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4", "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"],
        "values": [1323.96, 1550.42, 1660.76, 1891.49, 2051.4, 2291.85, 2401.21, 2704.72, 2945.84, 3182.04, 3234.7, 3599.88]
    },
    "chart7_top_districts": {
        "labels": ["Bengaluru Urban District", "Hyderabad District", "Pune District", "Jaipur District", "Rangareddy District", "Medchal Malkajgiri District", "Visakhapatnam District", "Guntur District", "Krishna District", "Patna District"],
        "values": [1993.78, 1190.69, 973.02, 785.41, 715.51, 575.89, 419.86, 317.45, 314.29, 311.08]
    },
    "chart8_state_heatmap": {
        "labels": ["Telangana", "Karnataka", "Maharashtra", "Andhra Pradesh", "Uttar Pradesh", "Rajasthan", "Madhya Pradesh", "Bihar", "West Bengal", "Odisha", "Tamil Nadu", "Delhi", "Gujarat", "Haryana", "Jharkhand", "Chhattisgarh", "Kerala", "Punjab", "Assam", "Uttarakhand"],
        "values": [4165.6, 4067.87, 4037.42, 3466.91, 2688.52, 2634.32, 1912.53, 1790.13, 1558.42, 1226.4, 1193.62, 1163.75, 1019.29, 964.5, 590.66, 554.49, 377.83, 295.69, 197.16, 182.91]
    },
    "chart9_top_pincodes": {
        "labels": ["560001", "500001", "400001", "110001", "600001", "700001", "380001", "500081", "560050", "201301"],
        "values": [7577.33, 6661.46, 4697.84, 4548.08, 4447.47, 4217.71, 4047.79, 3899.8, 3846.44, 3735.17]
    },
    "chart10_district_treemap": {
        "labels": ["Bengaluru Urban District", "Hyderabad District", "Pune District", "Jaipur District", "Rangareddy District", "Medchal Malkajgiri District", "Visakhapatnam District", "Guntur District", "Krishna District", "Patna District", "Thane District", "Mumbai District", "Lucknow District", "Ghaziabad District", "East Godavari District"],
        "values": [1993.78, 1190.69, 973.02, 785.41, 715.51, 575.89, 419.86, 317.45, 314.29, 311.08, 256.14, 243.67, 242.24, 222.27, 218.16]
    },
    "chart11_yearly_growth": {
        "labels": ["2018", "2019", "2020", "2021", "2022", "2023", "2024"],
        "values": [162.3, 627.67, 1464.12, 3459.87, 6426.63, 9449.18, 12962.46]
    },
    "chart12_scatter": {
        "states": ["Telangana", "Karnataka", "Maharashtra", "Andhra Pradesh", "Uttar Pradesh", "Rajasthan", "Madhya Pradesh", "Bihar", "West Bengal", "Odisha", "Tamil Nadu", "Delhi", "Gujarat", "Haryana", "Jharkhand", "Chhattisgarh", "Kerala", "Punjab", "Assam", "Uttarakhand"],
        "counts": [12.49, 9.44, 11.0, 13.75, 16.82, 14.38, 11.54, 10.94, 10.02, 8.45, 7.06, 1.95, 6.31, 5.03, 5.02, 4.26, 3.08, 2.5, 2.27, 1.77],
        "amounts": [4165.6, 4067.87, 4037.42, 3466.91, 2688.52, 2634.32, 1912.53, 1790.13, 1558.42, 1226.4, 1193.62, 1163.75, 1019.29, 964.5, 590.66, 554.49, 377.83, 295.69, 197.16, 182.91]
    },
    "chart13_app_opens": {
        "labels": ["2022-Q1", "2022-Q2", "2022-Q3", "2022-Q4", "2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4", "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"],
        "values": [15.72, 17.79, 19.22, 21.26, 22.93, 24.93, 27.22, 29.94, 32.63, 35.41, 38.13, 40.42]
    }
}

# PhonePe colors
PURPLE = '#5f259f'
PURPLE_LIGHT = '#8a4ac8'
GREEN = '#259f35'

# Header
st.markdown("""
<div style='background: linear-gradient(135deg, #259f35 0%, #001a66 100%); 
            padding: 2rem; text-align: center; border-radius: 10px; margin-bottom: 2rem;'>
    <h1 style='color: white; font-size: 2.5rem; margin-bottom: 0.5rem;'>💳 PhonePe Transaction Insights Dashboard</h1>
    <p style='color: white; font-size: 1.2rem;'>All 13 Interactive Charts with Real Data</p>
</div>
""", unsafe_allow_html=True)

# Stats cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Users", "587M")
with col2:
    st.metric("Total Transactions", "₹345L Cr")
with col3:
    st.metric("States Covered", "36")
with col4:
    st.metric("Charts", "13")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "💰 Transactions", "👥 Users", "🌍 Geographic", "📈 Trends"])

# Overview Tab
with tab1:
    # Chart 11: Year-over-Year Growth
    fig11 = go.Figure()
    fig11.add_trace(go.Bar(
        x=charts_data["chart11_yearly_growth"]["labels"],
        y=charts_data["chart11_yearly_growth"]["values"],
        marker_color=[PURPLE, PURPLE_LIGHT, '#764ba2', '#8a5dc7', '#9e6dd0', '#b285d9', '#c69de2'],
        name='Transaction Amount'
    ))
    fig11.update_layout(
        title="📈 Year-over-Year Transaction Growth",
        xaxis_title="Year",
        yaxis_title="Transaction Amount (₹ Billions)",
        height=450
    )
    st.plotly_chart(fig11, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart 3: Transaction Type Distribution
        fig3 = go.Figure(data=[go.Pie(
            labels=charts_data["chart3_trans_treemap"]["labels"],
            values=charts_data["chart3_trans_treemap"]["values"],
            hole=0.4,
            marker_colors=[PURPLE, PURPLE_LIGHT, '#764ba2', '#8a5dc7', '#9e6dd0']
        )])
        fig3.update_layout(title="🔄 Transaction Type Distribution", height=350)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Chart 5: Transaction Category Breakdown
        fig5 = go.Figure(data=[go.Pie(
            labels=charts_data["chart5_trans_pie"]["labels"],
            values=charts_data["chart5_trans_pie"]["values"],
            marker_colors=[PURPLE, PURPLE_LIGHT, '#764ba2', '#8a5dc7', '#9e6dd0']
        )])
        fig5.update_layout(title="🥧 Transaction Category Breakdown", height=350)
        st.plotly_chart(fig5, use_container_width=True)

# Transactions Tab
with tab2:
    # Chart 4: Top States by Transaction
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        y=charts_data["chart4_top_states_trans"]["labels"],
        x=charts_data["chart4_top_states_trans"]["values"],
        orientation='h',
        marker_color=[PURPLE, PURPLE_LIGHT, '#764ba2'],
        name='Amount'
    ))
    fig4.update_layout(
        title="📊 Top 10 States by Transaction Amount",
        xaxis_title="Amount (₹ Billions)",
        yaxis_title="State",
        height=400
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart 6: Quarterly Trends
        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(
            x=charts_data["chart6_quarterly_trend"]["labels"],
            y=charts_data["chart6_quarterly_trend"]["values"],
            mode='lines+markers',
            line=dict(color=PURPLE, width=3),
            fill='tozeroy',
            fillcolor='rgba(95, 37, 159, 0.2)',
            name='Transaction Amount'
        ))
        fig6.update_layout(
            title="📈 Quarterly Transaction Trends",
            xaxis_title="Quarter",
            yaxis_title="Amount (₹ Billions)",
            height=350
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    with col2:
        # Chart 12: Scatter Plot
        fig12 = go.Figure()
        fig12.add_trace(go.Scatter(
            x=charts_data["chart12_scatter"]["counts"],
            y=charts_data["chart12_scatter"]["amounts"],
            mode='markers',
            marker=dict(size=12, color=PURPLE, opacity=0.7),
            text=charts_data["chart12_scatter"]["states"],
            name='States'
        ))
        fig12.update_layout(
            title="🔵 Transaction Count vs Amount",
            xaxis_title="Transaction Count (Billions)",
            yaxis_title="Transaction Amount (₹ Billions)",
            height=350
        )
        st.plotly_chart(fig12, use_container_width=True)

# Users Tab
with tab3:
    # Chart 1: User Registration Growth
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=charts_data["chart1_user_trend"]["labels"],
        y=charts_data["chart1_user_trend"]["users"],
        mode='lines+markers',
        line=dict(color=PURPLE, width=3),
        fill='tozeroy',
        fillcolor='rgba(95, 37, 159, 0.1)',
        name='Registered Users'
    ))
    fig1.update_layout(
        title="📈 User Registration Growth Trend",
        xaxis_title="Quarter",
        yaxis_title="Users (Millions)",
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart 2: Top States by Users
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            y=charts_data["chart2_top_states_users"]["labels"],
            x=charts_data["chart2_top_states_users"]["values"],
            orientation='h',
            marker_color=[PURPLE, PURPLE_LIGHT, '#764ba2'],
            name='Users'
        ))
        fig2.update_layout(
            title="📊 Top 10 States by Registered Users",
            xaxis_title="Users (Millions)",
            yaxis_title="State",
            height=350
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Chart 13: App Opens
        fig13 = go.Figure()
        fig13.add_trace(go.Scatter(
            x=charts_data["chart13_app_opens"]["labels"],
            y=charts_data["chart13_app_opens"]["values"],
            mode='lines+markers',
            line=dict(color=PURPLE_LIGHT, width=3),
            fill='tozeroy',
            fillcolor='rgba(138, 74, 200, 0.2)',
            name='App Opens'
        ))
        fig13.update_layout(
            title="📱 App Opens Trend",
            xaxis_title="Quarter",
            yaxis_title="App Opens (Billions)",
            height=350
        )
        st.plotly_chart(fig13, use_container_width=True)

# Geographic Tab
with tab4:
    # Chart 8: State Heatmap
    fig8 = go.Figure()
    fig8.add_trace(go.Bar(
        y=charts_data["chart8_state_heatmap"]["labels"],
        x=charts_data["chart8_state_heatmap"]["values"],
        orientation='h',
        marker=dict(
            color=charts_data["chart8_state_heatmap"]["values"],
            colorscale=[[0, '#b285d9'], [0.5, PURPLE_LIGHT], [1, PURPLE]],
            showscale=True
        ),
        name='Amount'
    ))
    fig8.update_layout(
        title="🗺️ State-wise Transaction Heatmap (Top 20)",
        xaxis_title="Transaction Amount (₹ Billions)",
        yaxis_title="State",
        height=500
    )
    st.plotly_chart(fig8, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart 7: Top Districts
        fig7 = go.Figure()
        fig7.add_trace(go.Bar(
            x=charts_data["chart7_top_districts"]["labels"],
            y=charts_data["chart7_top_districts"]["values"],
            marker_color=PURPLE,
            name='Amount'
        ))
        fig7.update_layout(
            title="🏙️ Top 10 Districts by Transaction Amount",
            xaxis_title="District",
            yaxis_title="Amount (₹ Billions)",
            height=350,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        # Chart 9: Top Pincodes
        fig9 = go.Figure()
        fig9.add_trace(go.Bar(
            x=charts_data["chart9_top_pincodes"]["labels"],
            y=charts_data["chart9_top_pincodes"]["values"],
            marker_color=PURPLE_LIGHT,
            name='Amount'
        ))
        fig9.update_layout(
            title="📢 Top 10 Pincodes by Transaction Amount",
            xaxis_title="Pincode",
            yaxis_title="Amount (₹ Millions)",
            height=350
        )
        st.plotly_chart(fig9, use_container_width=True)
    
    # Chart 10: District Treemap
    fig10 = go.Figure()
    fig10.add_trace(go.Bar(
        y=charts_data["chart10_district_treemap"]["labels"],
        x=charts_data["chart10_district_treemap"]["values"],
        orientation='h',
        marker_color=[PURPLE, PURPLE_LIGHT, '#764ba2', '#8a5dc7', '#9e6dd0', '#b285d9'],
        name='Amount'
    ))
    fig10.update_layout(
        title="🌳 District Transaction Distribution",
        xaxis_title="Amount (₹ Billions)",
        yaxis_title="District",
        height=500
    )
    st.plotly_chart(fig10, use_container_width=True)

# Trends Tab
with tab5:
    # Chart 11b: Yearly Growth (Line)
    fig11b = go.Figure()
    fig11b.add_trace(go.Scatter(
        x=charts_data["chart11_yearly_growth"]["labels"],
        y=charts_data["chart11_yearly_growth"]["values"],
        mode='lines+markers',
        line=dict(color=PURPLE, width=4),
        fill='tozeroy',
        fillcolor='rgba(95, 37, 159, 0.2)',
        marker=dict(size=10),
        name='Transaction Amount'
    ))
    fig11b.update_layout(
        title="📈 Year-over-Year Growth Analysis",
        xaxis_title="Year",
        yaxis_title="Transaction Amount (₹ Billions)",
        height=450
    )
    st.plotly_chart(fig11b, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Chart 6b: Quarterly Patterns
        fig6b = go.Figure()
        fig6b.add_trace(go.Bar(
            x=charts_data["chart6_quarterly_trend"]["labels"],
            y=charts_data["chart6_quarterly_trend"]["values"],
            marker_color=PURPLE,
            name='Transaction Amount'
        ))
        fig6b.update_layout(
            title="📊 Quarterly Patterns (2022-2024)",
            xaxis_title="Quarter",
            yaxis_title="Amount (₹ Billions)",
            height=350
        )
        st.plotly_chart(fig6b, use_container_width=True)
    
    with col2:
        # Chart 1b: User Growth
        fig1b = go.Figure()
        fig1b.add_trace(go.Scatter(
            x=charts_data["chart1_user_trend"]["labels"],
            y=charts_data["chart1_user_trend"]["users"],
            mode='lines+markers',
            line=dict(color=PURPLE, width=3),
            fill='tozeroy',
            fillcolor='rgba(95, 37, 159, 0.1)',
            name='Users'
        ))
        fig1b.update_layout(
            title="👥 User Growth Trajectory",
            xaxis_title="Quarter",
            yaxis_title="Users (Millions)",
            height=350
        )
        st.plotly_chart(fig1b, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>PhonePe Transaction Insights Dashboard | Data-driven insights for digital payments</p>
</div>
""", unsafe_allow_html=True)