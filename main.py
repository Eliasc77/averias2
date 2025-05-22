from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

averias = [
    {
        "Solicitud": "250310-120327",
        "TipoSS": "Mantenimiento",
        "NroOT": "677122",
        "UbiTecnica": "Lineas de Amoniaco",
        "Descripcion": "se realizo la descarga del amoniaco de la planta de frio para que se pueda realizar trabajos de soldadura.",
        "InicioAveria": "10/3/2025 12:08:00",
        "FinAveria": "",
        "NotificadoA": "Javier Paz",
        "Repercusion": "No afecta produccion",
        "Notificacion": "10/3/2025 12:08:00",
        "ATCs": [
            {"Nro": "1056822", "Proveedor": "WORLD MOTOR SAC", "Estado": "Cancelado"},
            {"Nro": "1056823", "Proveedor": "INIAR E.I.R.L.", "Estado": "Cancelado"},
            {"Nro": "1056824", "Proveedor": "YULE ELECTRICIDAD S.A.C.", "Estado": "Cancelado"}
        ]
    },
    {
        "Solicitud": "250307-170756",
        "TipoSS": "Mantenimiento",
        "NroOT": "676847",
        "UbiTecnica": "Tuberias / Manifold y valvulas Agua salada",
        "Descripcion": "se solicita cambio de tuberia de medida de nivel de agua tk kastre proa er",
        "InicioAveria": "7/3/2025 17:07:00",
        "FinAveria": "",
        "NotificadoA": "Javier Paz",
        "Repercusion": "No afecta produccion",
        "Notificacion": "7/3/2025 17:07:00",
        "ATCs": [
            {"Nro": "1056822", "Proveedor": "WORLD MOTOR SAC", "Estado": "Cancelado"},
            {"Nro": "1056823", "Proveedor": "INIAR E.I.R.L.", "Estado": "Cancelado"},
            {"Nro": "1056824", "Proveedor": "YULE ELECTRICIDAD S.A.C.", "Estado": "Cancelado"}
        ]
    },
    {
        "Solicitud": "250305-141507",
        "TipoSS": "Mantenimiento",
        "NroOT": "676303",
        "UbiTecnica": "Comedor",
        "Descripcion": "Cambiar zocalo de cajon de asiento del comedor por encontrarse en mal estado",
        "InicioAveria": "5/3/2025 14:15:00",
        "FinAveria": "",
        "NotificadoA": "David Delgado Gonzales",
        "Repercusion": "No afecta produccion",
        "Notificacion": "5/3/2025 14:15:00",
        "ATCs": [
            {"Nro": "1056822", "Proveedor": "WORLD MOTOR SAC", "Estado": "Cancelado"},
            {"Nro": "1056823", "Proveedor": "INIAR E.I.R.L.", "Estado": "Cancelado"},
            {"Nro": "1056824", "Proveedor": "YULE ELECTRICIDAD S.A.C.", "Estado": "Cancelado"}
        ]
    }
]

 

@app.route("/averias", methods=["GET"])
def get_averias():
    return jsonify(averias), 200



if __name__ == "__main__":
    app.run()