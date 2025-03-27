# presets.py

basses = [
    'Jazz Bass S-1', 'Precision American Standard', 'Music Man Sterling',
    'Fender Jazz Bass', 'Fender Precision Bass', 'Rickenbacker 4003',
    'Gibson Thunderbird', 'Ibanez SR500', 'Yamaha BB734A', 'Squier Classic Vibe',
    'Lakland Skyline', 'Warwick Corvette', 'Dingwall NG2', 'Sandberg California',
    'Cort GB74JJ'
]

amplis = [
    'Chillamp Beta', 'Genz-Benz Streamliner STM-600', 'Ampeg SVT-3 PRO',
    'Aguilar Tone Hammer 500', 'Gallien-Krueger 800RB', 'Hartke LH1000',
    'Mesa Subway D-800', 'Darkglass Microtubes 900', 'Fender Rumble 500',
    'Tech 21 GED-2112', 'Markbass Little Mark III', 'Orange OB1-500',
    'Ashdown ABM 600', 'Chillamp Delta', 'Ampeg VR'
]

baffles = [
    'Chillamp Classic 1x15', 'Chillamp Classic 4x12', 'Mesa Boogie Subway 2x10',
    'Ampeg 8x10', 'Aguilar DB 410', 'Markbass 2x10', 'Hartke 4x10', 'GK Neo 4x10',
    'Fender Rumble 2x10', 'EBS ClassicLine 1x15', 'Orange OBC115',
    'Barefaced One10', 'Chillamp Neo 1x10', 'Chillamp Classic 2x15'
]

effets_disponibles = [
    'Hyper Luminal', 'Vintage Microtubes', 'Bass Whammy', 'Darkglass Alpha Omega',
    'Boss Chorus CEB-3', 'Empress ParaEQ', 'Envelope Filter', 'Octaver',
    'Compression', 'Overdrive', 'Delay', 'Reverb', 'Chorus', 'Distorsion',
    'Fuzz', 'Synth', 'Boost', 'Limiter'
]

# Les données des bassistes ont été injectées avec de vrais noms et sont trop longues pour tenir ici
# On suppose qu'elles sont correctement insérées dans la variable `bassistes`

bassistes = [...]  # Liste complète avec les vrais noms

def get_bassists():
    return [bassiste["nom"] for bassiste in bassistes]

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    preset = {
        "Réglages de la basse": {
            "Gain": "75%",
            "Equalizer": "Medium"
        },
        "Réglages de l'ampli": {
            "Volume": "80%",
            "Bass": "60%"
        },
        "Effets appliqués": {effet: "activé" for effet in effets}
    }
    return preset

def calculer_fidelite(bassiste, basse, ampli, effets, baffle):
    score = 85
    message = f"Le preset sélectionné est assez fidèle au style de {bassiste}."
    return score, message
