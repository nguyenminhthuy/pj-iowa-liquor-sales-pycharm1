import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def plot_Overall_Sale_Inv(df):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=df['Year'], y=df["Total Sales (USD)"], name="Total Sales (USD)"),
        secondary_y=False)

    fig.add_trace(
        go.Scatter(x=df['Year'], y=df["No. of Invoices"], line_color="#00008B",
                   name="Number of invoices", mode="lines"), secondary_y=True)

    fig.update_xaxes(title_text="Year")

    # Set y-axes titles
    fig.update_yaxes(title_text="Total Sales (USD)", secondary_y=False)
    fig.update_yaxes(title_text="Number of invoices", secondary_y=True)

    fig.update_traces(marker_color='#FF7F50', opacity=1)
    fig.update_layout(legend=dict(orientation="h",
                                  yanchor="top", xanchor="left",
                                  y=1, x=0.01
                                  ))
    fig.update_layout(margin=dict(r=0, l=0, t=50, b=10))
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

def table_diffSales_previousYear(df):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise'),
        cells=dict(values=[df['Year'],
                           df['Total Sales (USD)'],
                           df['Sales Variance'],
                           df['No. of Invoices'],
                           df['Invoices Variance']],
                   fill_color='lavender'))
    ])
    fig.update_layout(height=250, margin=dict(r=0, l=0, t=5, b=0))
    return fig

def plot_Overall_Cost_Profit(df):
    fig = go.Figure(data=[
        go.Bar(name='Total Cost (USD)',
               x=df['Year'],
               y=df['Total Cost (USD)']),
        go.Bar(name='Gross Profit (USD)',
               x=df['Year'],
               y=df['Gross Profit (USD)'])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(legend=dict(orientation="h",
                                 yanchor="top", xanchor="left",
                                 y=1, x=0.01
                ))
    fig.update_layout(margin=dict(r=0, l=0, t=50, b=10))
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

def table_cost_profit(df):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise'),
        cells=dict(values=[df['Year'],
                           df['Total Sales (USD)'],
                           df['Total Cost (USD)'],
                           df['Gross Profit (USD)']],
                   fill_color='lavender'))
    ])
    fig.update_layout(height=250, margin=dict(r=0, l=0, t=5, b=0))
    return fig

def plot_monthly_sales_bydf(sale, inv):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=sale.index, y=sale.values,
               name="Total Sales (USD)"), secondary_y=False)

    fig.add_trace(
        go.Scatter(x=inv.index, y=inv.values,
                   line_color="#00008B", name="Number of invoices", mode="lines"), secondary_y=True)

    fig.update_xaxes(title_text="Month")

    # Set y-axes titles
    fig.update_yaxes(title_text="Total Sales (USD)", secondary_y=False)
    fig.update_yaxes(title_text="Number of invoices", secondary_y=True)

    fig.update_traces(marker_color='#FF69B4', opacity=1)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(title="SALES MONTHLY TREND",
                     legend=dict(
                     orientation="h",
                     yanchor="top",
                     y=1,
                     xanchor="left",
                     x=0.01
                ))
    fig.update_layout(margin=dict(r=0, l=0, t=50, b=10))
    return fig

def plot_dow_sales_bydf(sale, inv):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=sale.index, y=sale.values,
               name="Total Sales (USD)"), secondary_y=False)

    fig.add_trace(
        go.Scatter(x=inv.index, y=inv.values,
                   line_color="#00008B", name="Number of invoices", mode="lines"), secondary_y=True)

    fig.update_xaxes(title_text="Day of Week")

    # Set y-axes titles
    fig.update_yaxes(title_text="Total Sales (USD)", secondary_y=False)
    fig.update_yaxes(title_text="Number of invoices", secondary_y=True)

    fig.update_traces(marker_color='#FF69B4', opacity=1)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                       'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(title="SALES DAY OF WEEK TREND",
                     legend=dict(
                     orientation="h",
                     yanchor="top",
                     y=1,
                     xanchor="left",
                     x=0.01
                ))
    fig.update_layout(margin=dict(r=0, l=0, t=50, b=10))
    return fig

def plot_heatmap_month_dow(m_dow_df):
    fig = px.imshow(m_dow_df,
                    labels = dict(x = "Day of Week", y = "Month", color = "Sale (Dollars)"),
                    x = m_dow_df.columns, y = m_dow_df.index,
                    aspect = "auto")
    fig.update_xaxes(side = "top")
    fig.update_layout(margin=dict(r=0, l=0, t=50, b=10))

    return fig

def plot_topGrossing(df_top10, df_title):
    y_sales = df_top10['sum']
    y_inv = df_top10['count']
    x = df_top10.index

    # Creating two subplots
    fig = make_subplots(rows = 1, cols = 2,
                        specs = [[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)

    fig.add_trace(go.Bar(x = y_sales, y = x,
                         marker = dict(color = 'rgba(50, 171, 96, 0.6)',
                                     line = dict(color = 'rgba(50, 171, 96, 1.0)', width = 1)),
                         texttemplate = "%{x:,.0f}", name = 'Sales (USD)',
                         orientation = 'h'), 1, 1)

    fig.add_trace(go.Scatter(x = y_inv, y = x,
                             mode='lines+markers', line_color='rgb(128, 0, 128)',
                             name='Number of invoices'), 1, 2)

    fig.update_layout(title = df_title,
                      yaxis = dict(autorange="reversed", showgrid = False, showline=False, showticklabels=True,
                                 domain=[0, 0.85]),

                      yaxis2 = dict(autorange="reversed", showgrid=False, showline=True, showticklabels=False,
                                  linecolor='rgba(102, 102, 102, 0.8)', linewidth=2,
                                  domain=[0, 0.85]),

                      xaxis = dict(zeroline=False, showline=False, showticklabels=True, showgrid=True,
                                 domain=[0, 0.42]),

                      xaxis2 = dict(zeroline=False, showline=False, showticklabels=True, showgrid=True,
                                  domain=[0.47, 1], side='top'),

                      legend = dict(x=0.029, y=1.038, font_size=10),
                      margin = dict(l=100, r=20, t=70, b=70),
                      paper_bgcolor = 'rgb(248, 248, 255)',
                      plot_bgcolor = 'rgb(248, 248, 255)')

    annotations = []

    y_s = np.round(y_sales, decimals=0)
    y_nw = np.rint(y_inv)

    # Adding labels
    for ydn, yd, xd in zip(y_nw, y_s, x):
        # labeling the scatter savings
        annotations.append(dict(xref='x2', yref='y2',
                                y=xd, x=ydn - 10000,
                                text='{:,}'.format(ydn),
                                font=dict(family='Arial', size=12, color='rgb(128, 0, 128)'),
                                showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper',
                            x=-0.2, y=-0.109,
                            text='Data Provided by Iowa Department of Commerce, Alcoholic Beverages Division',
                            font=dict(family='Arial', size=10, color='rgb(150,150,150)'), showarrow=False))

    fig.update_layout(annotations=annotations)
    return fig


def plot_topConsuming(df_top10, df_title):
    y_sales = df_top10['count']
    y_inv = df_top10['sum']
    x = df_top10.index

    # Creating two subplots
    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)

    fig.add_trace(go.Bar(x=y_sales, y=x,
                         marker=dict(color='rgba(50, 171, 96, 0.6)',
                                     line=dict(color='rgba(50, 171, 96, 1.0)', width=1)),
                         texttemplate="%{x:,.0f}", name='Number of invoices',
                         orientation='h'), 1, 1)

    fig.add_trace(go.Scatter(x=y_inv, y=x,
                             mode='lines+markers', line_color='rgb(128, 0, 128)',
                             name='Sales (USD)'), 1, 2)

    fig.update_layout(title=df_title,
                      yaxis=dict(autorange="reversed", showgrid=False, showline=False, showticklabels=True,
                                 domain=[0, 0.85]),

                      yaxis2=dict(autorange="reversed", showgrid=False, showline=True, showticklabels=False,
                                  linecolor='rgba(102, 102, 102, 0.8)', linewidth=2,
                                  domain=[0, 0.85]),

                      xaxis=dict(zeroline=False, showline=False, showticklabels=True, showgrid=True,
                                 domain=[0, 0.42]),

                      xaxis2=dict(zeroline=False, showline=False, showticklabels=True, showgrid=True,
                                  domain=[0.47, 1], side='top'),

                      legend=dict(x=0.029, y=1.038, font_size=10),
                      margin=dict(l=100, r=20, t=70, b=70),
                      paper_bgcolor='rgb(248, 248, 255)',
                      plot_bgcolor='rgb(248, 248, 255)')

    annotations = []

    y_s = np.round(y_sales, decimals=0)
    y_nw = np.rint(y_inv)

    # Adding labels
    for ydn, yd, xd in zip(y_nw, y_s, x):
        # labeling the scatter savings
        annotations.append(dict(xref='x2', yref='y2',
                                y=xd, x=ydn - 10000,
                                text='{:,}'.format(ydn),
                                font=dict(family='Arial', size=12, color='rgb(128, 0, 128)'),
                                showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper',
                            x=-0.2, y=-0.109,
                            text='Data Provided by Iowa Department of Commerce, Alcoholic Beverages Division',
                            font=dict(family='Arial', size=10, color='rgb(150,150,150)'), showarrow=False))

    fig.update_layout(annotations=annotations)
    return fig
