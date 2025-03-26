from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io
from presets import get_bassists, get_presets_for_combination

app = Flask(__name__)

@app.route('/')
def index():
    bassists = get_bassists()
    return render_template('index.html', bassists=bassists)

@app.route('/generate', methods=['POST'])
def generate():
    bassiste = request.form.get("bassiste")
    basse = request.form.get("basse")
    ampli = request.form.get("ampli")
    effets = request.form.getlist("effets")
    baffle = request.form.get("baffle")

    preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_title("Chillamp Selector - Preset personnalisé")

    pdf.cell(200, 10, txt="🎸 Chillamp Selector - Preset personnalisé", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Bassiste : {bassiste}", ln=True)
    pdf.cell(200, 10, txt=f"Basse : {basse}", ln=True)
    pdf.cell(200, 10, txt=f"Ampli : {ampli}", ln=True)
    pdf.cell(200, 10, txt=f"Baffle : {baffle}", ln=True)
    pdf.cell(200, 10, txt="Effets :", ln=True)
    for effet in effets:
        pdf.cell(200, 10, txt=f" - {effet}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Réglages détaillés :", ln=True)
    pdf.set_font("Arial", size=12)

    for section, réglages in preset.items():
        pdf.cell(200, 10, txt=f"{section} :", ln=True)
        for paramètre, valeur in réglages.items():
            pdf.cell(200, 10, txt=f"  - {paramètre} : {valeur}", ln=True)
        pdf.ln(2)

    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Chaîne du signal :", ln=True)
    pdf.set_font("Arial", size=12)
    chain = f"{basse} → " + " → ".join(effets) + f" → {ampli} → {baffle}"
    pdf.multi_cell(0, 10, txt=chain)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, download_name="preset.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
