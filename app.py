from flask import Flask, render_template, request, redirect
from urllib.parse import quote
from datetime import datetime

app = Flask(__name__)

# ESTO TE FALTABA: La ruta para entrar a la página
@app.route('/')
def home():
    return render_template('index.html')

import csv # Importamos esta librería para manejar archivos

@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form.get('cliente')
    fecha_str = request.form.get('dia')
    hora = request.form.get('hora')
    
    if not nombre or not fecha_str or not hora:
        return "Error: Faltan datos", 400

    # --- NUEVO: GUARDAR EN ARCHIVO ---
    # Abrimos (o creamos) un archivo llamado turnos.csv
    with open('turnos.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        # Guardamos: Nombre, Fecha, Hora y el momento exacto de la reserva
        escritor.writerow([nombre, fecha_str, hora, datetime.now()])
    # ---------------------------------

    telefono = "5491126651328" 
    mensaje = f"¡Hola! Soy {nombre}. Reservé un turno para el {fecha_str} a las {hora} hs."
    mensaje_codificado = quote(mensaje)
    link_whatsapp = f"https://wa.me/{telefono}?text={mensaje_codificado}"

    return redirect(link_whatsapp)
# ESTO TE FALTABA: El "encendido" del servidor

if __name__ == '__main__':
    app.run(debug=True, port=8080)