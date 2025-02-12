###########################################################################################################################################
import dash_bootstrap_components as dbc
import dash
from dash import dash_table, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os
###########################################################################################################################################
data_path = os.path.join(os.path.dirname(__file__), 'data')
df_trials = pd.read_csv(os.path.join(data_path, 'trials.csv'))
df_mesh = pd.read_csv(os.path.join(data_path, 'mesh.csv'))
df_loc = pd.read_csv(os.path.join(data_path, 'loc.csv'))

###########################################################################################################################################
#creation de l'application dash avec le theme Cerulean 
app = dash.Dash("oncoTrials", external_stylesheets=[dbc.themes.CERULEAN], suppress_callback_exceptions=True) 

#aggregation des dataframes pour les graph


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="https://about.gitlab.com/images/press/logo/png/gitlab-icon-rgb.png",
                    height="30px"
                ),
                href="https://gitlab.com/hajar.abdaoui/oncotrial_tracker",
                target="_blank"  # Ouvre le lien dans un nouvel onglet
            )
        ),
    ],
    brand="📈OncoTrial Tracker",
    color="primary",
    dark=True,
)

# tabs = html.Div(
#     [html.Br(),
#         dbc.Tabs(
#             [
#                 dbc.Tab(
#                     label="Dashboard", activeTabClassName="fw-bold"
#                 ),
#                 dbc.Tab(label="Table", activeLabelClassName="fw-bold"),
#             ]
#         ),
#     ], style={"margin-top": "-20px"}
# )

tabs = html.Div(
    [html.Br(),
        dbc.Tabs(
            id='tabs',
            children=[
                dbc.Tab(label="About", activeTabClassName="fw-bold", tab_id="tab-about"),
                dbc.Tab(label="Dashboard", activeTabClassName="fw-bold", tab_id="tab-dashboard"),
                dbc.Tab(label="Table", activeLabelClassName="fw-bold", tab_id="tab-table"),
            ]
        ),
    ], style={"margin-top": "-20px"}
)

footer = html.Footer(
    dbc.Container([
        html.Hr(),
        html.P("© 2024 Mon Dashboard", className="text-center")
    ]),
    style={"background-color": "#f8f9fa", "padding": "10px"}
)

######################################
study_counts = df_trials.groupby('startYear').size().reset_index(name='count')

fig_year_count = px.line(
    study_counts,
    x='startYear',
    y='count',
    labels={'startYear': 'Year', 'count': 'Studies'},
    title='Studies Started Each Year',
    markers=True,  # Ajoute des points sur la ligne
    color_discrete_sequence=['#007BA7']  # Couleur principale (bleu Bootstrap)
)

fig_year_count.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',   #fond transparent
    paper_bgcolor='rgba(0,0,0,0)',  #fond transparent
    font=dict(family="Arial", size=9, color="#333"),
    title_x=0.5,  #centrage du titre
    margin=dict(l=20, r=20, t=40, b=20),
    hovermode="x unified"  #survol des points
)

fig_year_count.update_xaxes(range=[1990, 2027])

######################################
completed = df_trials[df_trials["status"]=="Completed"]#.dropna(subset=["duration_year"])

fig_box_duration = px.box(
    completed,
    y="duration_year",
    title="Duration of completed studies",
    labels={"Years"},
    color_discrete_sequence=["#007BA7"]  # Couleur principale (bleu Bootstrap)
)

fig_box_duration.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',   # fond transparent
    paper_bgcolor='rgba(0,0,0,0)',  # fond transparent
    font=dict(family="Arial", size=9, color="#333"),
    title_x=0.5,  # centrage du titre
    margin=dict(l=20, r=20, t=40, b=20),  # marges similaires au graphique linéaire
    height=450,
    width=450
)

fig_box_duration.update_yaxes(range=[0, 20], title="Duration in years")  # Plage et titre de l'axe Y
fig_box_duration.update_traces(marker=dict(color='#007BA7'))  # Garde la même couleur bleue que le graphique linéaire

######################################
drug_pourcentage = round(len(df_trials[df_trials.drug_FDA == True])*100/(len(df_trials[df_trials.drug_FDA == True]) + len(df_trials[df_trials.drug_FDA == False])),1)
device_pourcentage = round(len(df_trials[df_trials.device_FDA == True])*100/(len(df_trials[df_trials.device_FDA == True]) + len(df_trials[df_trials.device_FDA == False])),1)

cards_info = [
    {"title": "Total Trials", "content": len(df_trials)},
    {"title": "Completed Trials", "content": len(completed)},
    {"title": "FDA Regulated Drug Product", "content": "{} %".format(drug_pourcentage)},
    {"title": "FDA Regulated Device Product", "content": "{} %".format(device_pourcentage)}
]

card_layout = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5(card["title"], className="card-title"),
                    html.H4(card["content"], className="card-text")
                ])
            ),
            width=3,  # Chaque colonne prendra 3/12 de l'espace (total 4 cases)
        ) for card in cards_info
    ],
    justify="between",  # Espace entre les colonnes
    className="mb-4"
)

######################################

categories = df_mesh['neoplasm_category'].unique()
@app.callback(
    Output('top-neoplasms-graph', 'figure'),
    Input('category-dropdown', 'value')
)
def update_graph(selected_category):
    # Filtrer le DataFrame en fonction de la catégorie sélectionnée
    df_filtered = df_mesh[df_mesh['neoplasm_category'] == selected_category]

    # Compter le nombre d'études par néoplasme
    count_df = df_filtered['neoplasm'].value_counts().reset_index()
    count_df.columns = ['neoplasm', 'count']
    count_df = count_df.sort_values(by='count', ascending=False)

    # Sélectionner les 10 néoplasmes les plus fréquents
    top_10_df = count_df.head(10)

    # Création de la figure harmonisée
    fig = px.bar(
        top_10_df,
        x='neoplasm',
        y='count',
        labels={'neoplasm': 'Classe de Néoplasme', 'count': "Nombre d'Études"},
        title=f"📊 Les 10 Néoplasmes les Plus Étudiés ({selected_category})",
        color_discrete_sequence=["#1f77b4"]  # Même bleu que le boxplot
    )

    # Mise en forme harmonisée
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',    # Fond transparent
        paper_bgcolor='rgba(0,0,0,0)',   # Fond transparent
        font=dict(family="Arial", size=14, color="#333"),  # Police uniforme
        title_x=0.5,                     # Titre centré
        margin=dict(l=40, r=40, t=60, b=120),
        height=550,
        hovermode="x unified"            # Effet de survol unifié
    )

    fig.update_xaxes(tickangle=-45)     # Inclinaison des étiquettes X
    fig.update_yaxes(showgrid=True, gridcolor='lightgrey')  # Grille légère

    return fig
######################################

df=df_trials[df_trials.results==True]
last_results = df[["nctid", "title", "organization", "description", "last_update"]].sort_values(by='last_update', ascending=False).head(5)

study_cards = [
    dbc.Card(
        dbc.CardBody([
            html.A(study["title"], href="https://clinicaltrials.gov/ct2/show/{}".format(study["nctid"]), target="_blank"),
            html.H6(study['organization'], className="card-subtitle mb-2 text-muted"),
            html.P(study["description"], className="card-text", style={"text-align": "justify"}),
            html.Footer(f"Last Update: {study['last_update']}", className="text-end text-secondary")
        ]),
        className="mb-3 shadow-sm p-2 bg-light rounded"
    )
    for _, study in last_results.iterrows()
]
######################################

content = dbc.Container(
    [
        # Section des cartes principales
        card_layout,

        # Section combinée : Encadré + Graphique linéaire + Boxplot
        dbc.Row([
            # Colonne principale (Encadré + Graphique linéaire)
            dbc.Col([
                # Encadré d'information
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Study Trends Over the Years", className="fw-bold text-primary"),
                        html.P(
                            "This graph shows the annual distribution of studies, providing insights into research trends over time.",
                            style={"text-align": "justify"}
                        )
                    ]),
                    className="shadow-sm p-3 mb-3 bg-light rounded"
                ),

                # Graphique linéaire
                dbc.Card(
                    dbc.CardBody(
                        dbc.Spinner(
                            dcc.Graph(id='study-year-graph', figure=fig_year_count,
                                      style={"width": "100%", "height": "300px", "margin": "0"}),
                            color="primary"
                        )
                    ),
                    className="shadow-sm p-3 mb-4 bg-white rounded",
                    style={"width": "100%"}
                )
            ], width=8),

            # Boxplot aligné à droite
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        dbc.Spinner(
                            dcc.Graph(id='study-duration-graph', figure=fig_box_duration,
                                      style={"width": "100%", "height": "459px", "margin": "0"}),
                            color="primary"
                        )
                    ),
                    className="shadow-sm p-3 mb-4 bg-white rounded",
                    style={"width": "100%"}
                ),
                width=4
            )
        ], justify="between"),

        # Section Dropdown + Texte descriptif
        dbc.Row([
            # Dropdown + Graphique des néoplasmes
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='category-dropdown',
                            options=[{'label': cat, 'value': cat} for cat in categories],
                            value='Neoplasms by Site',
                            clearable=False
                        ),
                        dbc.Spinner(
                            dcc.Graph(id='top-neoplasms-graph'),
                            color="primary"
                        )
                    ]),
                    className="shadow-sm p-3 mb-4 bg-white rounded"
                ),
                width=6
            ),

            # Deux encadrés de texte descriptif
            dbc.Col([
                # Premier encadré
                dbc.Card(
                    dbc.CardBody([
                        html.P(
                            '''MeSH (Medical Subject Headings) is a controlled vocabulary 
developed by the National Library of Medicine (NLM) to index, organize, and search biomedical information 
in databases like PubMed and ClinicalTrials.gov. It follows a hierarchical structure, allowing terms to be 
classified from broad categories to more specific subcategories. For example, Neoplasms is a primary category, 
which branches into subcategories like Neoplasms by Site, Neoplasms by Histologic Type, and Cysts. 
This structure helps standardize medical terminology, improve the accuracy of search queries, 
and link related research topics.''',
                            className="text-danger",
                            style={"text-align": "justify"}
                        )
                    ]),
                    className="shadow-sm p-3 mb-3 bg-white rounded",
                    style={"height": "250px", "overflowY": "auto"}  # Texte défilable
                ),

                # Deuxième encadré
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Latest 5 Studies", className="fw-bold text-center mb-3 text-success"),
                        html.Div(study_cards, style={"height": "400px", "overflowY": "auto"})  # Scrollable
                    ]),
                    className="shadow-sm p-3 bg-white rounded",
                    style={"height": "385px", "overflowY": "auto"}  # Texte défilable
                )
            ], width=6)
        ])
    ],
    fluid=True,
    className="mt-4"
)

######################################

df_loc_grouped = df_loc.groupby("nctid").agg({
    "facility": lambda x: "\n".join(sorted(set(x.dropna()))),
    "city": lambda x: "\n".join(sorted(set(x.dropna()))),
    "country": "first"
}).reset_index()

# Fusion des DataFrames
df_combined = pd.merge(df_trials, df_loc_grouped, on="nctid", how="inner")[[
    "title", "organization", "condition", "study_type", "status", "city", "contact"
]]

# Renommer les colonnes pour plus de clarté
df_combined.rename(columns={
    "title": "Title",
    "organization": "Organization",
    "condition": "Condition",
    "study_type": "Type",
    "city": "Location",
    "status": "Status",
    "contact": "Contact"
}, inplace=True)
######################################

content2 = dbc.Container([
    html.H1("Tableau des Essais Cliniques", className="text-center my-4 fw-bold text-primary"),

    dbc.Card(
        dbc.CardBody([
            dash_table.DataTable(
                id='table',
                columns=[
                    {"name": col, "id": col, "deletable": False} 
                    for col in df_combined.columns
                ],
                data=df_combined.to_dict('records'),
                page_size=10,
                filter_action="native",  # Activation du filtrage natif
                sort_action="native",    # Activation du tri natif
                sort_mode="multi",       # Tri sur plusieurs colonnes
                column_selectable='single',  # Activation de la sélection de colonnes
                style_table={'overflowX': 'auto'},
                style_cell={
                    'whiteSpace': 'pre-line',  # Support du saut de ligne '\n'
                    'textAlign': 'left',
                    'padding': '10px',
                    'fontFamily': 'Arial'
                },
                style_header={
                    'backgroundColor': '#007BA7',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'textAlign': 'center'
                },
                style_data={
                    'backgroundColor': 'white',
                    'color': 'black'
                },
                style_data_conditional=[
                    {  # Effet zébré pour les lignes impaires
                        'if': {'row_index': 'odd'},
                        'backgroundColor': '#F9F9F9'
                    }
                ]
            )
        ]),
        className="shadow-sm p-4 bg-white rounded"
    )
], fluid=True)


######################################
content0 = dbc.Container([
    html.H1("Tableau des Essais Cliniques", className="text-center my-4 fw-bold text-primary"),])
######################################
# app.layout = html.Div([
#     dcc.Location(id="url"),
#     navbar, tabs, content, footer
# ])
@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'active_tab')
)
def display_tab_content(active_tab):
    if active_tab == 'tab-dashboard':
        return content  # Affiche le contenu du dashboard pour l'onglet "Dashboard"
    elif active_tab == 'tab-table':
        return content2  # Affiche content2 pour l'onglet "Table"
    elif active_tab == 'tab-about' :
        return content0
    return content  # Par défaut, afficher le contenu du dashboard

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar, tabs, html.Div(id='tab-content'), footer
])

server = app.server


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


