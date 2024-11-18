import pandas as pd
import plotly.express as px
from collections import Counter


def create_student_origin_map(file_path):
    """
    Creates a beautifully styled interactive world map showing student origins
    with a color scale optimized for 1-7 students range
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

    # Create a capped version of student counts for coloring
    map_data['Students_Display'] = map_data['Students'].apply(lambda x: min(x, 7))

    # Custom color scale - using a blue gradient optimized for 1-7 range
    custom_color_scale = [
        [0, 'rgb(240, 249, 255)'],  # 1 student
        [0.17, 'rgb(204, 229, 255)'],  # 2 students
        [0.34, 'rgb(153, 204, 255)'],  # 3 students
        [0.51, 'rgb(102, 178, 255)'],  # 4 students
        [0.68, 'rgb(51, 153, 255)'],  # 5 students
        [0.85, 'rgb(0, 102, 204)'],  # 6 students
        [1, 'rgb(0, 51, 153)']  # 7+ students
    ]

    # Create the choropleth map
    fig = px.choropleth(
        map_data,
        locations='Country',
        locationmode='country names',
        color='Students_Display',
        hover_data={'Country': True, 'Students': True, 'Students_Display': False},
        color_continuous_scale=custom_color_scale,
        range_color=[1, 7],  # Set fixed range for color scale
        title='Global Student Origins at Berea College<br><sup>Fall 2023</sup>',
    )

    # Update the layout for enhanced visualization
    fig.update_layout(
        # Title styling
        title=dict(
            font=dict(
                size=24,
                family='Arial Black',
                color='rgb(51, 51, 51)'
            ),
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        # Overall layout styling
        paper_bgcolor='rgb(248, 249, 250)',
        plot_bgcolor='rgb(248, 249, 250)',
        width=1200,
        height=700,
        margin=dict(t=100, l=0, r=0, b=0),

        # Map styling
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor='rgb(180, 180, 180)',
            coastlinewidth=1,
            showocean=True,
            oceancolor='rgb(240, 249, 255)',
            showland=True,
            landcolor='rgb(250, 250, 250)',
            showcountries=True,
            countrycolor='rgb(180, 180, 180)',
            countrywidth=0.5,
            projection_type='miller',
            showlakes=True,
            lakecolor='rgb(240, 249, 255)',
            showrivers=False,
        ),

        # Hover label styling
        hoverlabel=dict(
            bgcolor='white',
            font_size=14,
            font_family='Arial',
            bordercolor='rgb(200, 200, 200)',
        ),

        # Color axis styling
        coloraxis_colorbar=dict(
            title=dict(
                text='Number of Students',
                font=dict(
                    size=14,
                    family='Arial',
                    color='rgb(51, 51, 51)'
                )
            ),
            ticktext=['1', '2', '3', '4', '5', '6', '7+'],
            tickvals=[1, 2, 3, 4, 5, 6, 7],
            tickfont=dict(
                size=12,
                family='Arial',
                color='rgb(51, 51, 51)'
            ),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgb(200, 200, 200)',
            borderwidth=1,
            len=0.8,
            thickness=20,
            x=0.95
        )
    )

    # Customize hover template with special handling for US
    def get_hover_template(row):
        if row['Country'] == 'United States':
            return f"<b>{row['Country']}</b><br><span style='font-size:1.2em;'>🎓 {row['Students']} Domestic Students</span><br><extra></extra>"
        else:
            return f"<b>{row['Country']}</b><br><span style='font-size:1.2em;'>🎓 {row['Students']} International Students</span><br><extra></extra>"

    map_data['hover_text'] = map_data.apply(get_hover_template, axis=1)
    fig.update_traces(
        hovertemplate="%{customdata[2]}",
        customdata=map_data[['Country', 'Students', 'hover_text']].values
    )

    # Add a subtitle explaining the scale
    # fig.add_annotation(
    #     text="Color scale shows international student distribution (1-7+ students per country)",
    #     xref="paper", yref="paper",
    #     x=0.5, y=0.87,
    #     showarrow=False,
    #     font=dict(
    #         size=12,
    #         color='rgb(100, 100, 100)'
    #     ),
    #     align="center"
    # )

    # Add data source annotation
    fig.add_annotation(
        text="Data source: Berea College Geographical Report Fall 2023",
        xref="paper", yref="paper",
        x=0, y=-0.02,
        showarrow=False,
        font=dict(
            size=10,
            color='rgb(150, 150, 150)'
        ),
        align="left"
    )

    # Save the plot as an HTML file with custom configuration
    fig.write_html(
        "student_origins_map.html",
        config={
            'displayModeBar': True,
            'displaylogo': False,
            'modeBarButtonsToRemove': [
                'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d',
                'autoScale2d', 'resetScale2d'
            ],
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'student_origins_map',
                'height': 700,
                'width': 1200,
                'scale': 2
            }
        }
    )

    # Show the plot in a browser
    fig.show()


# Usage
if __name__ == "__main__":
    file_path = "Fall2023GeographicalReportBereaCollege.xlsx"
    create_student_origin_map(file_path)