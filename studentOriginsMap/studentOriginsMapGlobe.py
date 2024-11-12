import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter


def create_student_origin_globe(file_path):
    """
    Creates an interactive globe showing student origins

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

    # Create the base choropleth map
    fig = go.Figure()

    # Add choropleth layer
    fig.add_trace(go.Choropleth(
        locations=map_data['Country'],
        locationmode='country names',
        z=map_data['Students'],
        colorscale='Viridis',
        marker_line_color='white',
        marker_line_width=0.5,
        colorbar_title='Number of Students',
        hovertemplate="<b>%{location}</b><br>" +
                      "Students: %{z}<br>" +
                      "<extra></extra>"
    ))

    # Update the layout for globe projection
    fig.update_layout(
        title=dict(
            text='Student Origins - Berea College Fall 2023',
            x=0.5,
            y=0.95
        ),
        geo=dict(
            projection=dict(
                type='orthographic',
                rotation=dict(
                    lon=-100,
                    lat=40,
                    roll=0
                )
            ),
            showcoastlines=True,
            coastlinecolor='white',
            showocean=True,
            oceancolor='rgb(28, 107, 160)',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            showcountries=True,
            countrycolor='white',
            showframe=False,
            bgcolor='rgba(0,0,0,0)'
        ),
        width=800,
        height=800,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )

    # Add buttons to rotate the globe
    def create_rotation_buttons():
        buttons = []
        views = [
            ('North America', -100, 40),
            ('South America', -60, -15),
            ('Europe', 15, 50),
            ('Africa', 20, 0),
            ('Asia', 100, 30),
            ('Oceania', 150, -20),
        ]

        for name, lon, lat in views:
            buttons.append(
                dict(
                    args=[{
                        'geo.projection.rotation': dict(lon=lon, lat=lat, roll=0)
                    }],
                    label=name,
                    method='relayout'
                )
            )

        return buttons

    fig.update_layout(
        updatemenus=[dict(
            type='buttons',
            showactive=False,
            buttons=create_rotation_buttons(),
            direction='down',
            x=0.1,
            y=1,
            xanchor='left',
            yanchor='bottom'
        )]
    )

    # Save the plot as an HTML file
    fig.write_html(
        "student_origins_globe.html",
        include_plotlyjs=True,
        full_html=True,
        config={'displayModeBar': False}  # Hide the modebar for cleaner look
    )

    # Show the plot in a browser
    fig.show(config={'displayModeBar': False})


# Usage
if __name__ == "__main__":
    file_path = "Fall2023GeographicalReportBereaCollege.xlsx"
    create_student_origin_globe(file_path)