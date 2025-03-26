
def get_bassists():
    return [
        "Nate Mendel",
        "Laurent Vernerey"
    ]

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    presets = {}

    # Réglages spécifiques par bassiste
    if bassiste == "Nate Mendel":
        presets["Basse"] = {
            "Tone": "80%",
            "Volume": "100%"
        }
        if ampli == "Beta":
            presets["Ampli"] = {
                "Volume (1964)": "7",
                "Bass (1964)": "6",
                "Treble (1964)": "5",
                "Master": "6"
            }
        if "Empress EQ" in effets:
            presets["Empress EQ"] = {
                "Low": "+2dB",
                "Mid": "+4dB",
                "High": "+1dB",
                "Q": "Narrow",
                "Gain": "Unity"
            }
        if "Hyper Luminal" in effets:
            presets["Hyper Luminal"] = {
                "Blend": "60%",
                "Time": "50%",
                "Output": "80%",
                "Ratio": "4:1",
                "Mode": "FET"
            }

    elif bassiste == "Laurent Vernerey":
        presets["Basse"] = {
            "Tone": "50%",
            "Volume": "100%"
        }
        if ampli == "STM-600":
            presets["Ampli"] = {
                "Gain": "5",
                "Volume": "6",
                "Bass": "5",
                "Mid": "4",
                "Treble": "5",
                "Master": "6"
            }
        if "Empress EQ" in effets:
            presets["Empress EQ"] = {
                "Low": "+1dB",
                "Mid": "+3dB",
                "High": "0dB",
                "Q": "Medium",
                "Gain": "Unity"
            }
        if "Hyper Luminal" in effets:
            presets["Hyper Luminal"] = {
                "Blend": "40%",
                "Time": "40%",
                "Output": "75%",
                "Ratio": "3:1",
                "Mode": "SYM"
            }

    # Réglage par défaut pour les effets restants
    for effet in effets:
        if effet not in presets:
            presets[effet] = {
                "Réglage 1": "50%",
                "Réglage 2": "50%"
            }

    # Chaîne du signal
    presets["Chaîne du signal"] = {
        "Ordre": f"{basse} → {' → '.join(effets)} → {ampli} → {baffle}"
    }

    return presets
