"""
Module pour tracer et calculer les valeurs de la suite de Syracuse.
"""
from plotly.graph_objects import Scatter, Figure
from primes import syracuse_l, temps_de_vol, temps_de_vol_en_altitude, altitude_maximale

def syr_plot(lsyr):
    """
    Trace la suite de Syracuse avec Plotly.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))

    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()

def main():
    """
    Fonction principale qui appelle les fonctions secondaires pour
    tester la suite de Syracuse et ses propriétés.
    """

    lsyr = syracuse_l(6)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()