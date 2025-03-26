
from flask import Flask, render_template, request, send_file
from fpdf import FPDF
from presets import get_presets_for_bassist
import io

app = Flask(__name__)

@app.route('/')
def index():
    bassists = ["Nate Mendel", "Laurent Vernerey"]
    basses = ["Jazz Bass S-1", "Precision Standard"]
    amps = ["Chillamp Beta"]
    cabs = ["Classic 1x15"]
    effects = ["Hyper Luminal", "Vintage Microtubes", "Boss Reverb"]
    return render_template('index.html', bassists=bassists, basses=basses, amps=amps, cabs=cabs, effects=effects)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.to_dict(flat=False)
    bassist = data.get('bassiste', [''])[0]
    bass = data.get('basse', [''])[0]
    amp = data.get('ampli', [''])[0]
    cab = data.get('baffle', [''])[0]
    selected_effects = data.get('effets', [])

    preset = get_presets_for_bassist(bassist, bass, amp, cab, selected_effects)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Chillamp Selector - {bassist}", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Basse : {bass}", ln=True)
    for param, value in preset['bass'].items():
        pdf.cell(200, 10, txt=f"  - {param} : {value}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Ampli : {amp}", ln=True)
    for param, value in preset['amp'].items():
        pdf.cell(200, 10, txt=f"  - {param} : {value}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Baffle : {cab}", ln=True)
    pdf.ln(5)

    if selected_effects:
        pdf.cell(200, 10, txt="Effets :", ln=True)
        for effect in selected_effects:
            pdf.cell(200, 10, txt=f"- {effect}", ln=True)
            for param, value in preset['effects'].get(effect, {}).items():
                pdf.cell(200, 10, txt=f"   - {param} : {value}", ln=True)
    else:
        pdf.cell(200, 10, txt="Aucun effet sélectionné", ln=True)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, as_attachment=True, download_name="preset.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
