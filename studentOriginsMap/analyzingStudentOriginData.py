import pandas as pd
import plotly.express as px
from collections import Counter


# Read the Excel file
def create_student_origin_map(file_path):
    """
    Creates an interactive world map showing student origins

    Parameters:
    file_path (str): Path to the Excel file containing student origin data
    """
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Count students per country
    country_counts = Counter(df['Country'])

    # Create a DataFrame for plotting
    map_data = pd.DataFrame({
        'Country': list(country_counts.keys()),
        'Students': list(country_counts.values())
    })

    # Create the choropleth map
    fig = px.choropleth(
        map_data,
        locations='Country',
        locationmode='country names',
        color='Students',
        hover_data={'Country': True, 'Students': True},
        color_continuous_scale='Viridis',
        title='Student Origins - Berea College Fall 2023',
    )

    # Update the layout for better visualization
    fig.update_layout(
        title_x=0.5,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
        width=1000,
        height=600,
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )

    # Customize hover template
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br>" +
                      "Students: %{z}<br>" +
                      "<extra></extra>"  # This removes the secondary box
    )

    # Save the plot as an HTML file
    fig.write_html("student_origins_map.html")

    # Show the plot in a browser
    fig.show()


# Usage
if __name__ == "__main__":
    file_path = "Fall2023GeographicalReportBereaCollege.xlsx"
    create_student_origin_map(file_path)