from flask import Flask, request
import mysql.connector

app = Flask(__name__)

#Consultar parceiros que atuam naquela área
def atende_area(user_lat, user_lon, p_lat, p_lon, coverage_radius_km):
    raio_graus = coverage_radius_km / 111  # converte km para graus
    dist = ((user_lat - p_lat)**2 + (user_lon - p_lon)**2)**0.5
    return dist <= raio_graus

@app.route('/', methods=['GET'])
def home():
    html = '''
    <html>
    <head>
        <title>Consulta Delivery</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div id="logo-e-nome">
            <img id="logo" src="/static/images/delivery_logo.png">
            <h2>CONSULTA DELIVERY</h2>
        </div>
        <form method="POST" action="/consulta">
            <label>Latitude
                <input type="text" name="latitude" required placeholder="Ex: -23.550520">
            </label>
            <label>Longitude
                <input type="text" name="longitude" required placeholder="Ex: -46.633308">
            </label>
            <div id="botaoBuscar">
                <input type="submit" value="Buscar Delivery">
            </div>
        </form>
        </div>
    </body>
    </html>
    '''
    return html

@app.route('/consulta', methods=['POST'])
def consulta_delivery():
    try:
        user_lat = float(request.form['latitude'])
        user_lon = float(request.form['longitude'])
    except ValueError:
        return '''
        <head>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <div class="resultado">
            <h3>Latitude e longitude inválidos. Use números.</h3>
            <a class="botao-voltar" href="/">Voltar</a>
        </div>
        '''

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='delivery'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM parceiros")
    parceiros = cursor.fetchall()
    cursor.close()
    conn.close()

    parceiros_cobrem = []
    for p in parceiros:
        if atende_area(user_lat, user_lon, p['latitude'], p['longitude'], p['coverage_radius_km']):
            parceiros_cobrem.append(p)

    if not parceiros_cobrem:
        return '''
        <head>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <div class="resultado">
            <h3>Nenhum delivery atende sua localização.</h3>
            <a class="botao-voltar" href="/">Voltar</a>
        </div>
        '''

    #Descobre qual é o delivery mais próximo do usuário
    #Utiliza fórmula Euclediana, que calcula a distâcia do usuário até o delivery em graus
    parceiro_mais_proximo = min(
        parceiros_cobrem,
        key=lambda p: ((user_lat - p['latitude'])**2 + (user_lon - p['longitude'])**2)**0.5
    )
    dist = ((user_lat - parceiro_mais_proximo['latitude'])**2 + (user_lon - parceiro_mais_proximo['longitude'])**2)**0.5
    dist_km = dist * 111  #Convertendo graus para km

    return f'''
    <head>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <div class="resultado">
        <h3>Delivery disponível</h3>
        <div id="vendedor-info">
            <p><strong>{parceiro_mais_proximo["tradingName"]}</strong></p>
            <p>Proprietário: {parceiro_mais_proximo["ownerName"]}</p>
            <p>Distância aproximada: {dist_km:.2f} km</p>
        </div>
        <a class="botao-voltar" href="/">Fazer nova consulta</a>
    </div>
    '''

if __name__ == '__main__':
    app.run(debug=True)