
# Définition des options disponibles
basses = ["Jazz Bass S-1", "Precision American Standard"]
amplis = ["Chillamp Beta", "Genz-Benz Streamliner STM-600"]
effets_disponibles = ["Hyper Luminal", "Vintage Microtubes", "Bass Whammy"]
baffles = ["Chillamp Classic 1x15"]

def get_bassists() -> list[str]:
    """
    Retourne la liste des bassistes disponibles.
    """
    return ["Nate Mendel", "Laurent Vernerey"]

def get_presets_for_combination(
    bassiste: str, 
    basse: str, 
    ampli: str, 
    effets: list[str], 
    baffle: str
) -> dict:
    """
    Génère et retourne un dictionnaire de réglages (preset)
    en fonction de la combinaison d'options choisie.
    
    Paramètres:
      - bassiste: le nom du bassiste
      - basse: le modèle de basse sélectionné
      - ampli: le modèle d'ampli sélectionné
      - effets: la liste des effets sélectionnés
      - baffle: le modèle de baffle sélectionné
      
    Retourne:
      Un dictionnaire contenant les réglages pour la basse, l'ampli et les effets.
    """
    preset = {}

    # Réglages pour la basse
    if basse == "Jazz Bass S-1":
        preset["Basse"] = {
            "Sélecteur": "Position 1 (série)",
            "Volume": "100%",
            "Tone": "70%"
        }
    elif basse == "Precision American Standard":
        preset["Basse"] = {
            "Volume": "100%",
            "Tone": "80%"
        }

    # Réglages pour l'ampli
    if ampli == "Chillamp Beta":
        preset["Ampli"] = {
            "Volume": "4",
            "Treble": "5",
            "Medium": "6",
            "Bass": "7"
        }
    elif ampli == "Genz-Benz Streamliner STM-600":
        preset["Ampli"] = {
            "Gain": "3",
            "Volume": "5",
            "Bass": "6",
            "Mid": "5",
            "Treble": "6",
            "Master": "4"
        }

    # Réglages pour les effets
    for effet in effets:
        if effet == "Hyper Luminal":
            if bassiste == "Nate Mendel":
                preset["Hyper Luminal"] = {
                    "Blend": "60%",
                    "Time": "25%",
                    "Output": "70%",
                    "Ratio": "4:1",
                    "Mode": "FET"
                }
            elif bassiste == "Laurent Vernerey":
                preset["Hyper Luminal"] = {
                    "Blend": "50%",
                    "Time": "50%",
                    "Output": "60%",
                    "Ratio": "2:1",
                    "Mode": "BUS"
                }
        elif effet == "Vintage Microtubes":
            preset["Vintage Microtubes"] = {
                "Drive": "40%",
                "Tone": "50%",
                "Blend": "60%",
                "Level": "70%"
            }
        elif effet == "Bass Whammy":
            preset["Bass Whammy"] = {
                "Mode": "Octave Up",
                "Wet/Dry": "50%"
            }

    return preset

