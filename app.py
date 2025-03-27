from flask import Flask, render_template, request, send_file, abort, jsonify
from fpdf import FPDF
import io
from presets import (
    get_bassists,
    get_presets_for_combination,
    calculer_fidelite,
    basses,
    amplis,
    effets_disponibles,
    baffles
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        bassists=get_bassists(),
        basses=basses,
        amplis=amplis,
        effets=effets_disponibles,
        baffles=baffles
    )

@app.route('/api/fidelite')
def api_fidelite():
    bassiste = request.args.get("bassiste")
    basse = request.args.get("basse")
    ampli = request.args.get("ampli")
    effets = request.args.getlist("effets")
    baffle = request.args.get("baffle")

    if not all([bassiste, basse, ampli, baffle]):
        return jsonify({"score": 0, "message": "Paramètres manquants."}), 400

    score, message = calculer_fidelite(bassiste, basse, ampli, effets, baffle)
    return jsonify({"score": score, "message": message})

@app.route('/generate', methods=['POST'])
def generate():
    bassiste = request.form.get("bassiste")
    basse = request.form.get("basse")
    ampli = request.form.get("ampli")
    effets = request.form.getlist("effets")
    baffle = request.form.get("baffle")

    if not (bassiste and basse and ampli and baffle):
        abort(400, description="Données manquantes dans le formulaire.")

    try:
        preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
        score, message = calculer_fidelite(bassiste, basse, ampli, effets, baffle)
    except Exception as e:
        abort(500, description="Erreur lors de la génération du preset.")

    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.set_title("Chillamp Selector - Preset personnalisé")

        pdf.cell(200, 10, txt="Chillamp Selector - Preset personnalisé", ln=True, align="C")
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

        for section, reglages in preset.items():
            pdf.cell(200, 10, txt=f"{section} :", ln=True)
            for parametre, valeur in reglages.items():
                pdf.cell(200, 10, txt=f"  - {parametre} : {valeur}", ln=True)
            pdf.ln(2)

        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Chaîne du signal :", ln=True)
        pdf.set_font("Arial", size=12)
        chain = f"{basse} -> " + " -> ".join(effets) + f" -> {ampli} -> {baffle}"
        pdf.multi_cell(0, 10, txt=chain)

        pdf.ln(10)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=f"Fidélité au son de {bassiste} : {score}%", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=message)

        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
    except Exception as e:
        abort(500, description="Erreur lors de la génération du PDF.")

    return send_file(pdf_output, download_name="preset.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
