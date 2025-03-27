basses = ['Jazz Bass S-1', 'Precision American Standard', 'Music Man Sterling', 'Fender Jazz Bass', 'Fender Precision Bass', 'Rickenbacker 4003', 'Gibson Thunderbird', 'Ibanez SR500', 'Yamaha BB734A', 'Squier Classic Vibe', 'Lakland Skyline', 'Warwick Corvette', 'Dingwall NG2', 'Sandberg California', 'Cort GB74JJ']

amplis = ['Chillamp Beta', 'Genz-Benz Streamliner STM-600', 'Ampeg SVT-3 PRO', 'Aguilar Tone Hammer 500', 'Gallien-Krueger 800RB', 'Hartke LH1000', 'Mesa Subway D-800', 'Darkglass Microtubes 900', 'Fender Rumble 500', 'Tech 21 GED-2112', 'Markbass Little Mark III', 'Orange OB1-500', 'Ashdown ABM 600', 'Chillamp Delta', 'Ampeg VR']

baffles = ['Chillamp Classic 1x15', 'Chillamp Classic 4x12', 'Mesa Boogie Subway 2x10', 'Ampeg 8x10', 'Aguilar DB 410', 'Markbass 2x10', 'Hartke 4x10', 'GK Neo 4x10', 'Fender Rumble 2x10', 'EBS ClassicLine 1x15', 'Orange OBC115', 'Barefaced One10', 'Chillamp Neo 1x10', 'Chillamp Classic 2x15']

effets_disponibles = ['Hyper Luminal', 'Vintage Microtubes', 'Bass Whammy', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Empress ParaEQ', 'Envelope Filter', 'Octaver', 'Compression', 'Overdrive', 'Delay', 'Reverb', 'Chorus', 'Distorsion', 'Fuzz', 'Synth', 'Boost', 'Limiter']

bassistes = [
    {
        "nom": 'Norbert "Nono" Krief',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['Hartke 4x10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Delay', 'Hyper Luminal', 'Compression'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Fender Jazz Bass'], 'effets': ['Hyper Luminal', 'Reverb', 'Fuzz'], 'amplis': ['Hartke LH1000'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 2',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['Fender Rumble 2x10', 'Hartke 4x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Darkglass Alpha Omega', 'Limiter'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Jazz Bass S-1'], 'effets': ['Empress ParaEQ', 'Octaver', 'Synth'], 'amplis': ['Orange OB1-500'], 'baffles': ['EBS ClassicLine 1x15']}
    },
    {
        "nom": 'Bassiste 3',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Barefaced One10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Delay', 'Distorsion'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Rickenbacker 4003'], 'effets': ['Boost', 'Boss Chorus CEB-3', 'Envelope Filter'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": 'Bassiste 4',
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO', 'Ampeg VR'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Barefaced One10'],
        "effets_recommandes": ['Delay', 'Fuzz', 'Synth'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Jazz Bass S-1'], 'effets': ['Empress ParaEQ', 'Delay', 'Chorus'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['EBS ClassicLine 1x15']}
    },
    {
        "nom": 'Bassiste 5',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Fuzz', 'Hyper Luminal', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Ibanez SR500'], 'effets': ['Darkglass Alpha Omega', 'Distorsion', 'Envelope Filter'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 6',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Ampeg VR'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Ampeg 8x10'],
        "effets_recommandes": ['Delay', 'Compression', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Fender Jazz Bass'], 'effets': ['Compression', 'Boost', 'Darkglass Alpha Omega'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 7',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Ampeg 8x10', 'Barefaced One10'],
        "effets_recommandes": ['Octaver', 'Reverb', 'Limiter'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Rickenbacker 4003'], 'effets': ['Reverb', 'Boost', 'Darkglass Alpha Omega'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 8',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10', 'Orange OBC115'],
        "effets_recommandes": ['Hyper Luminal', 'Limiter', 'Synth'],
        "matos_typique": {'basses': ['Precision American Standard', 'Jazz Bass S-1'], 'effets': ['Boss Chorus CEB-3', 'Hyper Luminal', 'Envelope Filter'], 'amplis': ['Hartke LH1000'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 9',
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112', 'Chillamp Beta'],
        "baffles_recommandes": ['Orange OBC115', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Compression', 'Chorus', 'Delay'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Fender Jazz Bass'], 'effets': ['Distorsion', 'Boss Chorus CEB-3', 'Overdrive'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": 'Bassiste 10',
        "origine": "International",
        "amplis_recommandes": ['Ampeg VR', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Empress ParaEQ', 'Limiter', 'Envelope Filter'],
        "matos_typique": {'basses': ['Precision American Standard', 'Music Man Sterling'], 'effets': ['Bass Whammy', 'Fuzz', 'Hyper Luminal'], 'amplis': ['Chillamp Delta'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 11',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Barefaced One10'],
        "effets_recommandes": ['Limiter', 'Bass Whammy', 'Compression'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Ibanez SR500'], 'effets': ['Reverb', 'Boost', 'Darkglass Alpha Omega'], 'amplis': ['Orange OB1-500'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 12',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Ampeg VR'],
        "baffles_recommandes": ['Hartke 4x10', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Delay', 'Synth', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Fender Jazz Bass'], 'effets': ['Boss Chorus CEB-3', 'Darkglass Alpha Omega', 'Empress ParaEQ'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 13',
        "origine": "International",
        "amplis_recommandes": ['Ampeg VR', 'Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Markbass 2x10', 'Chillamp Classic 1x15'],
        "effets_recommandes": ['Chorus', 'Octaver', 'Boost'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Lakland Skyline'], 'effets': ['Overdrive', 'Distorsion', 'Vintage Microtubes'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 14',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['Barefaced One10', 'Markbass 2x10'],
        "effets_recommandes": ['Compression', 'Chorus', 'Overdrive'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Warwick Corvette'], 'effets': ['Darkglass Alpha Omega', 'Delay', 'Boost'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 15',
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112', 'Fender Rumble 500'],
        "baffles_recommandes": ['Barefaced One10', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Vintage Microtubes', 'Distorsion', 'Chorus'],
        "matos_typique": {'basses': ['Sandberg California', 'Jazz Bass S-1'], 'effets': ['Compression', 'Hyper Luminal', 'Distorsion'], 'amplis': ['Hartke LH1000'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 16',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Aguilar DB 410', 'GK Neo 4x10'],
        "effets_recommandes": ['Fuzz', 'Overdrive', 'Bass Whammy'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Fender Jazz Bass'], 'effets': ['Vintage Microtubes', 'Limiter', 'Synth'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 17',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['Barefaced One10', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Compression', 'Overdrive', 'Envelope Filter'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Fender Precision Bass'], 'effets': ['Hyper Luminal', 'Boss Chorus CEB-3', 'Reverb'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 18',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Aguilar DB 410', 'Ampeg 8x10'],
        "effets_recommandes": ['Bass Whammy', 'Hyper Luminal', 'Limiter'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Gibson Thunderbird'], 'effets': ['Darkglass Alpha Omega', 'Overdrive', 'Octaver'], 'amplis': ['Ampeg VR'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 19',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Hartke 4x10', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Compression', 'Limiter', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Yamaha BB734A'], 'effets': ['Limiter', 'Compression', 'Vintage Microtubes'], 'amplis': ['Chillamp Beta'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 20',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Aguilar DB 410', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Compression', 'Limiter', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Rickenbacker 4003'], 'effets': ['Delay', 'Octaver', 'Synth'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 21',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Ampeg VR'],
        "baffles_recommandes": ['Hartke 4x10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Fuzz', 'Envelope Filter', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Ibanez SR500'], 'effets': ['Distorsion', 'Envelope Filter', 'Boss Chorus CEB-3'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Barefaced One10']}
    },
    {
        "nom": 'Bassiste 22',
        "origine": "International",
        "amplis_recommandes": ['Ampeg VR', 'Mesa Subway D-800'],
        "baffles_recommandes": ['Orange OBC115', 'Hartke 4x10'],
        "effets_recommandes": ['Octaver', 'Limiter', 'Boost'],
        "matos_typique": {'basses': ['Precision American Standard', 'Rickenbacker 4003'], 'effets': ['Overdrive', 'Distorsion', 'Vintage Microtubes'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 23',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Mesa Subway D-800'],
        "baffles_recommandes": ['Aguilar DB 410', 'GK Neo 4x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Envelope Filter', 'Reverb'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Music Man Sterling'], 'effets': ['Chorus', 'Distorsion', 'Fuzz'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 24',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Hartke LH1000'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Compression', 'Vintage Microtubes', 'Octaver'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Rickenbacker 4003'], 'effets': ['Vintage Microtubes', 'Synth', 'Chorus'], 'amplis': ['Ampeg VR'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 25',
        "origine": "International",
        "amplis_recommandes": ['Orange OB1-500', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Hartke 4x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Distorsion', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Sandberg California'], 'effets': ['Fuzz', 'Reverb', 'Delay'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 26',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Ampeg 8x10'],
        "effets_recommandes": ['Octaver', 'Limiter', 'Synth'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Music Man Sterling'], 'effets': ['Boost', 'Darkglass Alpha Omega', 'Octaver'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 27',
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Delay', 'Reverb', 'Chorus'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Rickenbacker 4003'], 'effets': ['Boost', 'Delay', 'Octaver'], 'amplis': ['Orange OB1-500'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 28',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Orange OB1-500'],
        "baffles_recommandes": ['Ampeg 8x10', 'GK Neo 4x10'],
        "effets_recommandes": ['Empress ParaEQ', 'Boost', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Yamaha BB734A'], 'effets': ['Boss Chorus CEB-3', 'Bass Whammy', 'Delay'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 29',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Markbass 2x10', 'Aguilar DB 410'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Fuzz', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Lakland Skyline'], 'effets': ['Fuzz', 'Reverb', 'Hyper Luminal'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 30',
        "origine": "International",
        "amplis_recommandes": ['Ampeg VR', 'Fender Rumble 500'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Octaver', 'Overdrive', 'Envelope Filter'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Lakland Skyline'], 'effets': ['Delay', 'Hyper Luminal', 'Boss Chorus CEB-3'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 31',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Hartke 4x10', 'GK Neo 4x10'],
        "effets_recommandes": ['Octaver', 'Reverb', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Precision American Standard', 'Lakland Skyline'], 'effets': ['Bass Whammy', 'Distorsion', 'Synth'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 32',
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Hartke 4x10', 'Barefaced One10'],
        "effets_recommandes": ['Octaver', 'Chorus', 'Envelope Filter'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Fender Jazz Bass'], 'effets': ['Limiter', 'Distorsion', 'Envelope Filter'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 33',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Ampeg VR'],
        "baffles_recommandes": ['Fender Rumble 2x10', 'Orange OBC115'],
        "effets_recommandes": ['Distorsion', 'Overdrive', 'Envelope Filter'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Cort GB74JJ'], 'effets': ['Envelope Filter', 'Synth', 'Compression'], 'amplis': ['Orange OB1-500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 34',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Chillamp Beta'],
        "baffles_recommandes": ['GK Neo 4x10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Chorus', 'Boss Chorus CEB-3', 'Limiter'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Squier Classic Vibe'], 'effets': ['Synth', 'Hyper Luminal', 'Distorsion'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 35',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Octaver', 'Limiter', 'Reverb'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Gibson Thunderbird'], 'effets': ['Bass Whammy', 'Envelope Filter', 'Distorsion'], 'amplis': ['Orange OB1-500'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 36',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Hartke LH1000'],
        "baffles_recommandes": ['Markbass 2x10', 'Aguilar DB 410'],
        "effets_recommandes": ['Limiter', 'Bass Whammy', 'Synth'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Gibson Thunderbird'], 'effets': ['Envelope Filter', 'Fuzz', 'Delay'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 37',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Chillamp Beta'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'Markbass 2x10'],
        "effets_recommandes": ['Fuzz', 'Synth', 'Limiter'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Lakland Skyline'], 'effets': ['Octaver', 'Reverb', 'Boss Chorus CEB-3'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 38',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Hartke LH1000'],
        "baffles_recommandes": ['Chillamp Neo 1x10', 'Aguilar DB 410'],
        "effets_recommandes": ['Hyper Luminal', 'Fuzz', 'Delay'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Warwick Corvette'], 'effets': ['Delay', 'Vintage Microtubes', 'Reverb'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 39',
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO', 'Mesa Subway D-800'],
        "baffles_recommandes": ['Hartke 4x10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Chorus', 'Distorsion', 'Bass Whammy'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Warwick Corvette'], 'effets': ['Distorsion', 'Fuzz', 'Empress ParaEQ'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": 'Bassiste 40',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Bass Whammy', 'Reverb', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Ibanez SR500'], 'effets': ['Compression', 'Limiter', 'Boss Chorus CEB-3'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 41',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10', 'Ampeg 8x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Envelope Filter', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Warwick Corvette'], 'effets': ['Fuzz', 'Reverb', 'Overdrive'], 'amplis': ['Chillamp Delta'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 42',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Ampeg VR'],
        "baffles_recommandes": ['Ampeg 8x10', 'Chillamp Classic 1x15'],
        "effets_recommandes": ['Overdrive', 'Bass Whammy', 'Fuzz'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Yamaha BB734A'], 'effets': ['Octaver', 'Reverb', 'Overdrive'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 43',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Vintage Microtubes', 'Hyper Luminal', 'Synth'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Rickenbacker 4003'], 'effets': ['Bass Whammy', 'Limiter', 'Reverb'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": 'Bassiste 44',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Barefaced One10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Envelope Filter', 'Boss Chorus CEB-3', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Fender Jazz Bass'], 'effets': ['Darkglass Alpha Omega', 'Octaver', 'Distorsion'], 'amplis': ['Ampeg VR'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 45',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Envelope Filter', 'Distorsion', 'Octaver'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Jazz Bass S-1'], 'effets': ['Boost', 'Limiter', 'Synth'], 'amplis': ['Orange OB1-500'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 46',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Chillamp Delta'],
        "baffles_recommandes": ['Hartke 4x10', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Reverb', 'Vintage Microtubes', 'Overdrive'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3', 'Empress ParaEQ', 'Vintage Microtubes'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Barefaced One10']}
    },
    {
        "nom": 'Bassiste 47',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Chillamp Delta'],
        "baffles_recommandes": ['Fender Rumble 2x10', 'Aguilar DB 410'],
        "effets_recommandes": ['Delay', 'Chorus', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Sandberg California'], 'effets': ['Bass Whammy', 'Vintage Microtubes', 'Empress ParaEQ'], 'amplis': ['Chillamp Delta'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 48',
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112', 'Fender Rumble 500'],
        "baffles_recommandes": ['Fender Rumble 2x10', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Hyper Luminal', 'Boss Chorus CEB-3', 'Limiter'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Gibson Thunderbird'], 'effets': ['Boss Chorus CEB-3', 'Hyper Luminal', 'Limiter'], 'amplis': ['Ampeg VR'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 49',
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Ampeg 8x10'],
        "effets_recommandes": ['Bass Whammy', 'Darkglass Alpha Omega', 'Compression'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Sandberg California'], 'effets': ['Hyper Luminal', 'Envelope Filter', 'Chorus'], 'amplis': ['Fender Rumble 500'], 'baffles': ['EBS ClassicLine 1x15']}
    },
    {
        "nom": 'Bassiste 50',
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Hartke 4x10'],
        "effets_recommandes": ['Synth', 'Hyper Luminal', 'Boost'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Precision American Standard'], 'effets': ['Delay', 'Reverb', 'Darkglass Alpha Omega'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 51',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Orange OBC115', 'Ampeg 8x10'],
        "effets_recommandes": ['Empress ParaEQ', 'Boost', 'Reverb'],
        "matos_typique": {'basses': ['Precision American Standard', 'Dingwall NG2'], 'effets': ['Limiter', 'Boost', 'Delay'], 'amplis': ['Chillamp Delta'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 52',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Orange OB1-500'],
        "baffles_recommandes": ['Aguilar DB 410', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Octaver', 'Boost', 'Limiter'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Jazz Bass S-1'], 'effets': ['Darkglass Alpha Omega', 'Overdrive', 'Empress ParaEQ'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 53',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Orange OB1-500'],
        "baffles_recommandes": ['GK Neo 4x10', 'Barefaced One10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Yamaha BB734A', 'Gibson Thunderbird'], 'effets': ['Fuzz', 'Envelope Filter', 'Compression'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 54',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Hartke 4x10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Hyper Luminal', 'Darkglass Alpha Omega', 'Bass Whammy'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Fender Jazz Bass'], 'effets': ['Chorus', 'Envelope Filter', 'Distorsion'], 'amplis': ['Ampeg VR'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 55',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['Barefaced One10', 'Orange OBC115'],
        "effets_recommandes": ['Reverb', 'Limiter', 'Delay'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Ibanez SR500'], 'effets': ['Darkglass Alpha Omega', 'Envelope Filter', 'Synth'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 56',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Chillamp Delta'],
        "baffles_recommandes": ['Hartke 4x10', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Envelope Filter', 'Overdrive', 'Octaver'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Cort GB74JJ'], 'effets': ['Hyper Luminal', 'Darkglass Alpha Omega', 'Reverb'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Barefaced One10']}
    },
    {
        "nom": 'Bassiste 57',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['GK Neo 4x10', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Boost', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Sandberg California', 'Ibanez SR500'], 'effets': ['Limiter', 'Delay', 'Vintage Microtubes'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 58',
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO', 'Markbass Little Mark III'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Barefaced One10'],
        "effets_recommandes": ['Limiter', 'Synth', 'Bass Whammy'],
        "matos_typique": {'basses': ['Precision American Standard', 'Fender Jazz Bass'], 'effets': ['Hyper Luminal', 'Delay', 'Envelope Filter'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 59',
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III', 'Chillamp Delta'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Empress ParaEQ', 'Octaver', 'Reverb'],
        "matos_typique": {'basses': ['Sandberg California', 'Jazz Bass S-1'], 'effets': ['Hyper Luminal', 'Bass Whammy', 'Vintage Microtubes'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": 'Bassiste 60',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Orange OB1-500'],
        "baffles_recommandes": ['Hartke 4x10', 'GK Neo 4x10'],
        "effets_recommandes": ['Bass Whammy', 'Octaver', 'Synth'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Dingwall NG2'], 'effets': ['Bass Whammy', 'Vintage Microtubes', 'Synth'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": 'Bassiste 61',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Chillamp Delta'],
        "baffles_recommandes": ['Hartke 4x10', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Vintage Microtubes', 'Bass Whammy', 'Distorsion'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Sandberg California'], 'effets': ['Boost', 'Compression', 'Limiter'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 62',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Ampeg VR'],
        "baffles_recommandes": ['Barefaced One10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Reverb', 'Vintage Microtubes', 'Limiter'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Lakland Skyline'], 'effets': ['Envelope Filter', 'Limiter', 'Darkglass Alpha Omega'], 'amplis': ['Chillamp Beta'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 63',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Markbass Little Mark III'],
        "baffles_recommandes": ['GK Neo 4x10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Empress ParaEQ', 'Distorsion', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Rickenbacker 4003'], 'effets': ['Synth', 'Darkglass Alpha Omega', 'Bass Whammy'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": 'Bassiste 64',
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112', 'Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Aguilar DB 410', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Boost', 'Distorsion', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Music Man Sterling'], 'effets': ['Darkglass Alpha Omega', 'Compression', 'Bass Whammy'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 65',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Chillamp Beta'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10', 'Aguilar DB 410'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Bass Whammy', 'Delay'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Fender Jazz Bass'], 'effets': ['Boss Chorus CEB-3', 'Limiter', 'Overdrive'], 'amplis': ['Hartke LH1000'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 66',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Chillamp Beta'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Delay', 'Bass Whammy', 'Limiter'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Jazz Bass S-1'], 'effets': ['Reverb', 'Octaver', 'Vintage Microtubes'], 'amplis': ['Orange OB1-500'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 67',
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III', 'Ampeg VR'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Aguilar DB 410'],
        "effets_recommandes": ['Envelope Filter', 'Compression', 'Fuzz'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Squier Classic Vibe'], 'effets': ['Octaver', 'Envelope Filter', 'Distorsion'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 68',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Ampeg 8x10'],
        "effets_recommandes": ['Boost', 'Bass Whammy', 'Limiter'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Dingwall NG2'], 'effets': ['Darkglass Alpha Omega', 'Reverb', 'Chorus'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 69',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Aguilar DB 410', 'Barefaced One10'],
        "effets_recommandes": ['Synth', 'Octaver', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Music Man Sterling'], 'effets': ['Empress ParaEQ', 'Boss Chorus CEB-3', 'Synth'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 70',
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900', 'Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Chillamp Neo 1x10', 'Hartke 4x10'],
        "effets_recommandes": ['Bass Whammy', 'Chorus', 'Delay'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Fender Jazz Bass'], 'effets': ['Bass Whammy', 'Boost', 'Octaver'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 71',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Chillamp Classic 2x15', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Octaver', 'Envelope Filter', 'Synth'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Lakland Skyline'], 'effets': ['Compression', 'Boss Chorus CEB-3', 'Overdrive'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 72',
        "origine": "International",
        "amplis_recommandes": ['Orange OB1-500', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Barefaced One10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Distorsion', 'Empress ParaEQ', 'Reverb'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Cort GB74JJ'], 'effets': ['Delay', 'Synth', 'Chorus'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 73',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Fender Rumble 500'],
        "baffles_recommandes": ['Ampeg 8x10', 'Barefaced One10'],
        "effets_recommandes": ['Distorsion', 'Darkglass Alpha Omega', 'Octaver'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Fender Jazz Bass'], 'effets': ['Delay', 'Vintage Microtubes', 'Synth'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 74',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10', 'Ampeg 8x10'],
        "effets_recommandes": ['Distorsion', 'Reverb', 'Chorus'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Sandberg California'], 'effets': ['Delay', 'Chorus', 'Fuzz'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 75',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Chorus', 'Boss Chorus CEB-3', 'Bass Whammy'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Dingwall NG2'], 'effets': ['Fuzz', 'Hyper Luminal', 'Delay'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 76',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['Aguilar DB 410', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Empress ParaEQ', 'Boss Chorus CEB-3', 'Fuzz'],
        "matos_typique": {'basses': ['Sandberg California', 'Jazz Bass S-1'], 'effets': ['Distorsion', 'Boost', 'Compression'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 77',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Barefaced One10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Reverb', 'Darkglass Alpha Omega', 'Chorus'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Precision American Standard'], 'effets': ['Octaver', 'Vintage Microtubes', 'Synth'], 'amplis': ['Hartke LH1000'], 'baffles': ['EBS ClassicLine 1x15']}
    },
    {
        "nom": 'Bassiste 78',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Chillamp Delta'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Barefaced One10'],
        "effets_recommandes": ['Overdrive', 'Envelope Filter', 'Compression'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Precision American Standard'], 'effets': ['Compression', 'Empress ParaEQ', 'Boost'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 79',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['GK Neo 4x10', 'EBS ClassicLine 1x15'],
        "effets_recommandes": ['Bass Whammy', 'Overdrive', 'Octaver'],
        "matos_typique": {'basses': ['Sandberg California', 'Yamaha BB734A'], 'effets': ['Vintage Microtubes', 'Octaver', 'Reverb'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 80',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Orange OB1-500'],
        "baffles_recommandes": ['GK Neo 4x10', 'Markbass 2x10'],
        "effets_recommandes": ['Envelope Filter', 'Chorus', 'Delay'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Lakland Skyline'], 'effets': ['Fuzz', 'Envelope Filter', 'Reverb'], 'amplis': ['Orange OB1-500'], 'baffles': ['Chillamp Neo 1x10']}
    },
    {
        "nom": 'Bassiste 81',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Chillamp Delta'],
        "baffles_recommandes": ['Fender Rumble 2x10', 'Ampeg 8x10'],
        "effets_recommandes": ['Delay', 'Distorsion', 'Chorus'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Sandberg California'], 'effets': ['Empress ParaEQ', 'Envelope Filter', 'Boost'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": 'Bassiste 82',
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO', 'Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Ampeg 8x10', 'GK Neo 4x10'],
        "effets_recommandes": ['Hyper Luminal', 'Boss Chorus CEB-3', 'Overdrive'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Ibanez SR500'], 'effets': ['Reverb', 'Chorus', 'Boost'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 83',
        "origine": "International",
        "amplis_recommandes": ['Ashdown ABM 600', 'Markbass Little Mark III'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Hartke 4x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Compression', 'Limiter'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Fender Jazz Bass'], 'effets': ['Fuzz', 'Boost', 'Chorus'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": 'Bassiste 84',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Chillamp Delta'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Envelope Filter', 'Darkglass Alpha Omega', 'Delay'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Sandberg California'], 'effets': ['Overdrive', 'Reverb', 'Fuzz'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Chillamp Classic 2x15']}
    },
    {
        "nom": 'Bassiste 85',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Tech 21 GED-2112'],
        "baffles_recommandes": ['Orange OBC115', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Distorsion', 'Octaver', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Sandberg California', 'Jazz Bass S-1'], 'effets': ['Octaver', 'Fuzz', 'Vintage Microtubes'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 86',
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III', 'Ampeg VR'],
        "baffles_recommandes": ['GK Neo 4x10', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Bass Whammy', 'Fuzz', 'Overdrive'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Dingwall NG2'], 'effets': ['Darkglass Alpha Omega', 'Delay', 'Hyper Luminal'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": 'Bassiste 87',
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Orange OBC115', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Limiter', 'Chorus'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Precision American Standard'], 'effets': ['Chorus', 'Distorsion', 'Synth'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 88',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Ashdown ABM 600'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Fender Rumble 2x10'],
        "effets_recommandes": ['Compression', 'Vintage Microtubes', 'Octaver'],
        "matos_typique": {'basses': ['Precision American Standard', 'Squier Classic Vibe'], 'effets': ['Distorsion', 'Boost', 'Chorus'], 'amplis': ['Hartke LH1000'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 89',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Beta', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Barefaced One10', 'Markbass 2x10'],
        "effets_recommandes": ['Delay', 'Fuzz', 'Octaver'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Yamaha BB734A'], 'effets': ['Octaver', 'Fuzz', 'Boss Chorus CEB-3'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": 'Bassiste 90',
        "origine": "International",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600', 'Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Ampeg 8x10', 'Chillamp Classic 1x15'],
        "effets_recommandes": ['Bass Whammy', 'Synth', 'Envelope Filter'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Warwick Corvette'], 'effets': ['Bass Whammy', 'Synth', 'Compression'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Barefaced One10']}
    },
    {
        "nom": 'Bassiste 91',
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500', 'Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Orange OBC115', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Distorsion', 'Reverb', 'Boost'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Squier Classic Vibe'], 'effets': ['Vintage Microtubes', 'Compression', 'Chorus'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 92',
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900', 'Fender Rumble 500'],
        "baffles_recommandes": ['EBS ClassicLine 1x15', 'Chillamp Classic 1x15'],
        "effets_recommandes": ['Reverb', 'Boost', 'Synth'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Precision American Standard'], 'effets': ['Overdrive', 'Synth', 'Empress ParaEQ'], 'amplis': ['Ashdown ABM 600'], 'baffles': ['Orange OBC115']}
    },
    {
        "nom": 'Bassiste 93',
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 4x12', 'Barefaced One10'],
        "effets_recommandes": ['Bass Whammy', 'Boss Chorus CEB-3', 'Reverb'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Lakland Skyline'], 'effets': ['Fuzz', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3'], 'amplis': ['Chillamp Beta'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 94',
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500', 'Mesa Subway D-800'],
        "baffles_recommandes": ['Ampeg 8x10', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Hyper Luminal', 'Octaver', 'Limiter'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Gibson Thunderbird'], 'effets': ['Hyper Luminal', 'Bass Whammy', 'Chorus'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": 'Bassiste 95',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Markbass Little Mark III'],
        "baffles_recommandes": ['GK Neo 4x10', 'Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Empress ParaEQ', 'Overdrive', 'Bass Whammy'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Fender Precision Bass'], 'effets': ['Overdrive', 'Compression', 'Vintage Microtubes'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 96',
        "origine": "International",
        "amplis_recommandes": ['Orange OB1-500', 'Markbass Little Mark III'],
        "baffles_recommandes": ['Barefaced One10', 'Chillamp Neo 1x10'],
        "effets_recommandes": ['Bass Whammy', 'Boss Chorus CEB-3', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Cort GB74JJ', 'Music Man Sterling'], 'effets': ['Reverb', 'Overdrive', 'Vintage Microtubes'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": 'Bassiste 97',
        "origine": "International",
        "amplis_recommandes": ['Chillamp Delta', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['Orange OBC115', 'Chillamp Classic 2x15'],
        "effets_recommandes": ['Hyper Luminal', 'Boss Chorus CEB-3', 'Boost'],
        "matos_typique": {'basses': ['Dingwall NG2', 'Warwick Corvette'], 'effets': ['Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Bass Whammy'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": 'Bassiste 98',
        "origine": "International",
        "amplis_recommandes": ['Orange OB1-500', 'Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Markbass 2x10', 'Ampeg 8x10'],
        "effets_recommandes": ['Envelope Filter', 'Vintage Microtubes', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Ibanez SR500'], 'effets': ['Boss Chorus CEB-3', 'Bass Whammy', 'Compression'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": 'Bassiste 99',
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB', 'Darkglass Microtubes 900'],
        "baffles_recommandes": ['Barefaced One10', 'Hartke 4x10'],
        "effets_recommandes": ['Overdrive', 'Limiter', 'Envelope Filter'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Lakland Skyline'], 'effets': ['Overdrive', 'Hyper Luminal', 'Reverb'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": 'Bassiste 100',
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000', 'Fender Rumble 500'],
        "baffles_recommandes": ['Hartke 4x10', 'Barefaced One10'],
        "effets_recommandes": ['Delay', 'Boost', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Sandberg California', 'Precision American Standard'], 'effets': ['Limiter', 'Boss Chorus CEB-3', 'Hyper Luminal'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
]
