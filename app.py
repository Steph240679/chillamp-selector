
from flask import Flask, render_template, request, send_file, abort
from fpdf import FPDF
import io
from presets import get_bassists, get_presets_for_combination, basses, amplis, effets_disponibles, baffles

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

@app.route('/generate', methods=['POST'])
def generate():
    # Récupération des données du formulaire
    bassiste = request.form.get("bassiste")
    basse = request.form.get("basse")
    ampli = request.form.get("ampli")
    effets = request.form.getlist("effets")
    baffle = request.form.get("baffle")

    # Validation des données reçues
    if not (bassiste and basse and ampli and baffle):
        abort(400, description="Données manquantes dans le formulaire.")

    # Récupération des réglages personnalisés via le preset
    try:
        preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
    except Exception as e:
        abort(500, description="Erreur lors de la génération du preset.")

    # Génération du PDF
    try:
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

        for section, reglages in preset.items():
            pdf.cell(200, 10, txt=f"{section} :", ln=True)
            for parametre, valeur in reglages.items():
                pdf.cell(200, 10, txt=f"  - {parametre} : {valeur}", ln=True)
            pdf.ln(2)

        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Chaîne du signal :", ln=True)
        pdf.set_font("Arial", size=12)
        # Construction de la chaîne du signal
        chain = f"{basse} → " + " → ".join(effets) + f" → {ampli} → {baffle}"
        pdf.multi_cell(0, 10, txt=chain)

        # Création d'un flux mémoire pour le PDF
        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
    except Exception as e:
        abort(500, description="Erreur lors de la génération du PDF.")

    # Envoi du PDF au client
    return send_file(pdf_output, download_name="preset.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
