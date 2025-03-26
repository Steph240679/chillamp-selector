
def get_presets_for_bassist(bassist, bass, amp, cab, effects):
    data = {
        "Nate Mendel": {
            "bass": {"Tone": "50%", "Volume": "100%"},
            "amp": {"Volume": "6", "Bass": "5", "Middle": "7", "Treble": "6"},
            "effects": {
                "Hyper Luminal": {"Blend": "70%", "Time": "10h", "Output": "11h", "Ratio": "4:1", "Mode": "BUS"},
                "Vintage Microtubes": {"Drive": "10h", "Blend": "60%", "Level": "12h", "Era": "1"},
                "Boss Reverb": {"Level": "3", "Tone": "5", "Type": "Room"}
            }
        },
        "Laurent Vernerey": {
            "bass": {"Tone": "60%", "Volume": "80%"},
            "amp": {"Volume": "4", "Bass": "6", "Middle": "5", "Treble": "6"},
            "effects": {
                "Hyper Luminal": {"Blend": "50%", "Time": "9h", "Output": "10h", "Ratio": "3:1", "Mode": "FET"},
                "Vintage Microtubes": {"Drive": "9h", "Blend": "50%", "Level": "11h", "Era": "2"},
                "Boss Reverb": {"Level": "2", "Tone": "4", "Type": "Plate"}
            }
        }
    }

    presets = {
        "bass": data[bassist]["bass"],
        "amp": data[bassist]["amp"],
        "effects": {}
    }

    for effect in effects:
        if effect in data[bassist]["effects"]:
            presets["effects"][effect] = data[bassist]["effects"][effect]

    return presets
