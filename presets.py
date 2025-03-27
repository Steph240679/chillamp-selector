basses = ['Jazz Bass S-1', 'Precision American Standard', 'Music Man Sterling', 'Fender Jazz Bass', 'Fender Precision Bass', 'Rickenbacker 4003', 'Gibson Thunderbird', 'Ibanez SR500', 'Yamaha BB734A', 'Squier Classic Vibe', 'Lakland Skyline', 'Warwick Corvette', 'Dingwall NG2', 'Sandberg California', 'Cort GB74JJ']

amplis = ['Chillamp Beta', 'Genz-Benz Streamliner STM-600', 'Ampeg SVT-3 PRO', 'Aguilar Tone Hammer 500', 'Gallien-Krueger 800RB', 'Hartke LH1000', 'Mesa Subway D-800', 'Darkglass Microtubes 900', 'Fender Rumble 500', 'Tech 21 GED-2112', 'Markbass Little Mark III', 'Orange OB1-500', 'Ashdown ABM 600', 'Chillamp Delta', 'Ampeg VR']

baffles = ['Chillamp Classic 1x15', 'Chillamp Classic 4x12', 'Mesa Boogie Subway 2x10', 'Ampeg 8x10', 'Aguilar DB 410', 'Markbass 2x10', 'Hartke 4x10', 'GK Neo 4x10', 'Fender Rumble 2x10', 'EBS ClassicLine 1x15', 'Orange OBC115', 'Barefaced One10', 'Chillamp Neo 1x10', 'Chillamp Classic 2x15']

effets_disponibles = ['Hyper Luminal', 'Vintage Microtubes', 'Bass Whammy', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Empress ParaEQ', 'Envelope Filter', 'Octaver', 'Compression', 'Overdrive', 'Delay', 'Reverb', 'Chorus', 'Distorsion', 'Fuzz', 'Synth', 'Boost', 'Limiter']

bassistes = [
    {
        "nom": "Laurent Vernerey",
        "origine": "France",
        "amplis_recommandes": ['Genz-Benz Streamliner STM-600'],
        "baffles_recommandes": ['Chillamp Classic 1x15', 'Chillamp Classic 4x12'],
        "effets_recommandes": ['Hyper Luminal', 'Bass Whammy', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Precision American Standard', 'Yamaha BB734A'], 'effets': ['Hyper Luminal', 'Bass Whammy', 'Empress ParaEQ'], 'amplis': ['Chillamp Beta'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Nate Mendel",
        "origine": "USA",
        "amplis_recommandes": ['Chillamp Beta'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Hyper Luminal', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Fender Precision Bass'], 'effets': ['Hyper Luminal', 'Vintage Microtubes'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Victoria De Angelis",
        "origine": "Italie",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive', 'Chorus'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Precision American Standard'], 'effets': ['Overdrive', 'Chorus'], 'amplis': ['Hartke LH1000'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Krist Novoselic",
        "origine": "USA",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Distorsion', 'Chorus'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Lakland Skyline'], 'effets': ['Distorsion', 'Chorus'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Paul McCartney",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Bass Whammy'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Squier Classic Vibe'], 'effets': ['Bass Whammy'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "John Deacon",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Reverb'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Fender Jazz Bass'], 'effets': ['Reverb'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Cliff Burton",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Compression', 'Delay', 'Octaver'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Gibson Thunderbird'], 'effets': ['Compression', 'Delay', 'Octaver'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Geezer Butler",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Bass Whammy'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Precision American Standard'], 'effets': ['Bass Whammy'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Sting",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Delay', 'Overdrive'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Gibson Thunderbird'], 'effets': ['Delay', 'Overdrive'], 'amplis': ['Chillamp Beta'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "John Myung",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive'],
        "matos_typique": {'basses': ['Precision American Standard', 'Warwick Corvette'], 'effets': ['Overdrive'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Phil Lynott",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Vintage Microtubes', 'Bass Whammy', 'Overdrive'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Music Man Sterling'], 'effets': ['Vintage Microtubes', 'Bass Whammy', 'Overdrive'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Kim Deal",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Delay', 'Overdrive'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Ibanez SR500'], 'effets': ['Delay', 'Overdrive'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Tal Wilkenfeld",
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Hyper Luminal', 'Empress ParaEQ', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Lakland Skyline'], 'effets': ['Hyper Luminal', 'Empress ParaEQ', 'Boss Chorus CEB-3'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Esperanza Spalding",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Envelope Filter', 'Delay', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Fender Jazz Bass'], 'effets': ['Envelope Filter', 'Delay', 'Empress ParaEQ'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Nathan East",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Reverb'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Precision American Standard'], 'effets': ['Darkglass Alpha Omega', 'Reverb'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Pino Palladino",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Delay'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Squier Classic Vibe'], 'effets': ['Delay'], 'amplis': ['Ampeg VR'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Carol Kaye",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Compression', 'Hyper Luminal', 'Overdrive'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Rickenbacker 4003'], 'effets': ['Darkglass Alpha Omega', 'Compression', 'Hyper Luminal', 'Overdrive'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Donald Duck Dunn",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Compression'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Precision American Standard'], 'effets': ['Compression'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Les Claypool",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Precision American Standard', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Billy Sheehan",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Hyper Luminal', 'Bass Whammy'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Gibson Thunderbird'], 'effets': ['Hyper Luminal', 'Bass Whammy'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Tony Kanal",
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Overdrive'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Rickenbacker 4003'], 'effets': ['Darkglass Alpha Omega', 'Overdrive'], 'amplis': ['Ampeg VR'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Adam Clayton",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Overdrive', 'Compression'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Jazz Bass S-1'], 'effets': ['Overdrive', 'Compression'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Robert Trujillo",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Yamaha BB734A', 'Squier Classic Vibe'], 'effets': ['Boss Chorus CEB-3'], 'amplis': ['Hartke LH1000'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Jason Newsted",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Compression', 'Reverb', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Lakland Skyline'], 'effets': ['Compression', 'Reverb', 'Hyper Luminal'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Mike Dirnt",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Overdrive'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Music Man Sterling'], 'effets': ['Overdrive'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Duff McKagan",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Compression'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Fender Jazz Bass'], 'effets': ['Compression'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Peter Hook",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Reverb', 'Overdrive', 'Delay'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Precision American Standard'], 'effets': ['Reverb', 'Overdrive', 'Delay'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Chris Wolstenholme",
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Hyper Luminal'],
        "matos_typique": {'basses': ['Precision American Standard', 'Fender Jazz Bass'], 'effets': ['Hyper Luminal'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Tim Commerford",
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Delay', 'Reverb', 'Boss Chorus CEB-3', 'Compression'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Lakland Skyline'], 'effets': ['Delay', 'Reverb', 'Boss Chorus CEB-3', 'Compression'], 'amplis': ['Hartke LH1000'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Tina Weymouth",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Octaver'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Ibanez SR500'], 'effets': ['Octaver'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Jack Bruce",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Reverb', 'Boss Chorus CEB-3', 'Bass Whammy'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Lakland Skyline'], 'effets': ['Reverb', 'Boss Chorus CEB-3', 'Bass Whammy'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Glenn Hughes",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Envelope Filter'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Precision American Standard'], 'effets': ['Envelope Filter'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Graham Maby",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Vintage Microtubes', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Warwick Corvette'], 'effets': ['Vintage Microtubes', 'Darkglass Alpha Omega'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Jack Casady",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Bass Whammy', 'Envelope Filter', 'Overdrive', 'Reverb'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Fender Precision Bass'], 'effets': ['Bass Whammy', 'Envelope Filter', 'Overdrive', 'Reverb'], 'amplis': ['Chillamp Beta'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Boz Burrell",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Compression', 'Hyper Luminal', 'Boss Chorus CEB-3', 'Envelope Filter'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Yamaha BB734A'], 'effets': ['Compression', 'Hyper Luminal', 'Boss Chorus CEB-3', 'Envelope Filter'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Roger Waters",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Lakland Skyline'], 'effets': ['Overdrive'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Tom Hamilton",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Overdrive', 'Bass Whammy', 'Vintage Microtubes', 'Octaver'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Fender Jazz Bass'], 'effets': ['Overdrive', 'Bass Whammy', 'Vintage Microtubes', 'Octaver'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Verdine White",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3', 'Hyper Luminal'], 'amplis': ['Chillamp Beta'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Richard Bona",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Envelope Filter', 'Boss Chorus CEB-3', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Music Man Sterling'], 'effets': ['Envelope Filter', 'Boss Chorus CEB-3', 'Hyper Luminal'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Dave Holland",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Lakland Skyline'], 'effets': ['Boss Chorus CEB-3'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Gary Willis",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Compression', 'Octaver', 'Reverb'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Ibanez SR500'], 'effets': ['Compression', 'Octaver', 'Reverb'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Jimmy Haslip",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Reverb', 'Darkglass Alpha Omega', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Precision American Standard', 'Rickenbacker 4003'], 'effets': ['Reverb', 'Darkglass Alpha Omega', 'Hyper Luminal'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Stanley Clarke",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Empress ParaEQ', 'Darkglass Alpha Omega', 'Compression'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3', 'Empress ParaEQ', 'Darkglass Alpha Omega', 'Compression'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "John Patitucci",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Fender Jazz Bass'], 'effets': ['Overdrive', 'Hyper Luminal'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Ron Carter",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Reverb', 'Bass Whammy', 'Hyper Luminal', 'Overdrive'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Rickenbacker 4003'], 'effets': ['Reverb', 'Bass Whammy', 'Hyper Luminal', 'Overdrive'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Will Lee",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Fender Jazz Bass'], 'effets': ['Boss Chorus CEB-3'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Mark King",
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Compression', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Lakland Skyline'], 'effets': ['Compression', 'Empress ParaEQ'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Rocco Prestia",
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Reverb', 'Envelope Filter', 'Compression', 'Delay'],
        "matos_typique": {'basses': ['Yamaha BB734A', 'Rickenbacker 4003'], 'effets': ['Reverb', 'Envelope Filter', 'Compression', 'Delay'], 'amplis': ['Hartke LH1000'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Johan De Farfalla",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Vintage Microtubes', 'Octaver'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3', 'Vintage Microtubes', 'Octaver'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "James LoMenzo",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Vintage Microtubes', 'Overdrive', 'Octaver'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Warwick Corvette'], 'effets': ['Vintage Microtubes', 'Overdrive', 'Octaver'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Mel Schacher",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Reverb', 'Overdrive'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Yamaha BB734A'], 'effets': ['Reverb', 'Overdrive'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Klaus Voormann",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Reverb', 'Overdrive'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Gibson Thunderbird'], 'effets': ['Reverb', 'Overdrive'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Mike Watt",
        "origine": "International",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Envelope Filter', 'Delay', 'Overdrive'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Gibson Thunderbird'], 'effets': ['Envelope Filter', 'Delay', 'Overdrive'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Doug Wimbish",
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Octaver', 'Hyper Luminal', 'Reverb'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Yamaha BB734A'], 'effets': ['Octaver', 'Hyper Luminal', 'Reverb'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Nick Beggs",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Envelope Filter', 'Darkglass Alpha Omega', 'Reverb', 'Empress ParaEQ'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Precision American Standard'], 'effets': ['Envelope Filter', 'Darkglass Alpha Omega', 'Reverb', 'Empress ParaEQ'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "John Taylor",
        "origine": "International",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Reverb', 'Bass Whammy', 'Overdrive', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Gibson Thunderbird'], 'effets': ['Reverb', 'Bass Whammy', 'Overdrive', 'Darkglass Alpha Omega'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Paul Simonon",
        "origine": "International",
        "amplis_recommandes": ['Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Jazz Bass S-1'], 'effets': ['Darkglass Alpha Omega'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Colin Greenwood",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Octaver', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Reverb'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Gibson Thunderbird'], 'effets': ['Octaver', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Reverb'], 'amplis': ['Chillamp Beta'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Jack Lawrence",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Reverb'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Gibson Thunderbird'], 'effets': ['Reverb'], 'amplis': ['Ampeg VR'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Alain Caron",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Delay', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Fender Precision Bass'], 'effets': ['Delay', 'Darkglass Alpha Omega'], 'amplis': ['Chillamp Beta'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Dominique Di Piazza",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Reverb', 'Overdrive'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Yamaha BB734A'], 'effets': ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Reverb', 'Overdrive'], 'amplis': ['Chillamp Beta'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Franck Hermanny",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Overdrive'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Rickenbacker 4003'], 'effets': ['Overdrive'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Etienne Mbappé",
        "origine": "France",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Delay', 'Bass Whammy'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Yamaha BB734A'], 'effets': ['Delay', 'Bass Whammy'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Michel Alibo",
        "origine": "France",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Envelope Filter', 'Empress ParaEQ', 'Overdrive', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Gibson Thunderbird'], 'effets': ['Envelope Filter', 'Empress ParaEQ', 'Overdrive', 'Vintage Microtubes'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Guy Nsangué",
        "origine": "France",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Rickenbacker 4003'], 'effets': ['Darkglass Alpha Omega'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Fred Dupont",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Envelope Filter', 'Vintage Microtubes', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Lakland Skyline'], 'effets': ['Envelope Filter', 'Vintage Microtubes', 'Darkglass Alpha Omega'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Julien Herné",
        "origine": "France",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Reverb', 'Bass Whammy'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Precision American Standard'], 'effets': ['Reverb', 'Bass Whammy'], 'amplis': ['Chillamp Beta'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Laurent David",
        "origine": "France",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Delay', 'Reverb'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Rickenbacker 4003'], 'effets': ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Delay', 'Reverb'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Fifi Chayeb",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Hyper Luminal', 'Boss Chorus CEB-3', 'Delay'],
        "matos_typique": {'basses': ['Jazz Bass S-1', 'Warwick Corvette'], 'effets': ['Hyper Luminal', 'Boss Chorus CEB-3', 'Delay'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Fred Monestier",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Vintage Microtubes', 'Delay', 'Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Yamaha BB734A', 'Ibanez SR500'], 'effets': ['Vintage Microtubes', 'Delay', 'Darkglass Alpha Omega'], 'amplis': ['Chillamp Beta'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Nicolas Fiszman",
        "origine": "International",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Ibanez SR500'], 'effets': ['Darkglass Alpha Omega'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Sylvain Daniel",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive', 'Boss Chorus CEB-3', 'Octaver'],
        "matos_typique": {'basses': ['Precision American Standard', 'Yamaha BB734A'], 'effets': ['Overdrive', 'Boss Chorus CEB-3', 'Octaver'], 'amplis': ['Chillamp Beta'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Jean Bisello",
        "origine": "France",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Octaver', 'Overdrive'],
        "matos_typique": {'basses': ['Fender Jazz Bass', 'Fender Precision Bass'], 'effets': ['Octaver', 'Overdrive'], 'amplis': ['Chillamp Beta'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Rémi Vignolo",
        "origine": "France",
        "amplis_recommandes": ['Ampeg SVT-3 PRO'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Boss Chorus CEB-3', 'Compression', 'Overdrive', 'Octaver'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Lakland Skyline'], 'effets': ['Boss Chorus CEB-3', 'Compression', 'Overdrive', 'Octaver'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Norbert "Nono" Krief",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Octaver'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Jazz Bass S-1'], 'effets': ['Octaver'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Yves Carbonne",
        "origine": "International",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Compression', 'Darkglass Alpha Omega', 'Bass Whammy'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Yamaha BB734A'], 'effets': ['Compression', 'Darkglass Alpha Omega', 'Bass Whammy'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Alain Perez",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Compression', 'Octaver'],
        "matos_typique": {'basses': ['Precision American Standard', 'Yamaha BB734A'], 'effets': ['Compression', 'Octaver'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Jean-Michel Kajdan",
        "origine": "France",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Rickenbacker 4003'], 'effets': ['Boss Chorus CEB-3'], 'amplis': ['Ampeg VR'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Jean-Marc Jafet",
        "origine": "France",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Overdrive', 'Envelope Filter'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Precision American Standard'], 'effets': ['Overdrive', 'Envelope Filter'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Bernard Paganotti",
        "origine": "International",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Delay', 'Compression'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Fender Jazz Bass'], 'effets': ['Delay', 'Compression'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Francis Moze",
        "origine": "International",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Chillamp Classic 4x12'],
        "effets_recommandes": ['Reverb', 'Delay', 'Boss Chorus CEB-3'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Precision American Standard'], 'effets': ['Reverb', 'Delay', 'Boss Chorus CEB-3'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Jean-Claude Naimro",
        "origine": "France",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Octaver', 'Compression'],
        "matos_typique": {'basses': ['Precision American Standard', 'Squier Classic Vibe'], 'effets': ['Octaver', 'Compression'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Fender Rumble 2x10']}
    },
    {
        "nom": "Renaud Garcia-Fons",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Gibson Thunderbird', 'Rickenbacker 4003'], 'effets': ['Darkglass Alpha Omega'], 'amplis': ['Gallien-Krueger 800RB'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Pascal Mulot",
        "origine": "France",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Compression', 'Octaver', 'Empress ParaEQ', 'Envelope Filter'],
        "matos_typique": {'basses': ['Precision American Standard', 'Music Man Sterling'], 'effets': ['Compression', 'Octaver', 'Empress ParaEQ', 'Envelope Filter'], 'amplis': ['Ampeg VR'], 'baffles': ['Markbass 2x10']}
    },
    {
        "nom": "Hervé Brault",
        "origine": "France",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Fender Rumble 2x10'],
        "effets_recommandes": ['Bass Whammy', 'Darkglass Alpha Omega', 'Octaver', 'Hyper Luminal'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Warwick Corvette'], 'effets': ['Bass Whammy', 'Darkglass Alpha Omega', 'Octaver', 'Hyper Luminal'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Philippe Chayeb",
        "origine": "France",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Markbass 2x10'],
        "effets_recommandes": ['Bass Whammy', 'Reverb', 'Hyper Luminal', 'Overdrive'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Music Man Sterling'], 'effets': ['Bass Whammy', 'Reverb', 'Hyper Luminal', 'Overdrive'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Thierry Fanfant",
        "origine": "France",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Bass Whammy', 'Empress ParaEQ', 'Delay', 'Octaver'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Music Man Sterling'], 'effets': ['Bass Whammy', 'Empress ParaEQ', 'Delay', 'Octaver'], 'amplis': ['Markbass Little Mark III'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Sébastien Chouard",
        "origine": "France",
        "amplis_recommandes": ['Aguilar Tone Hammer 500'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Darkglass Alpha Omega'],
        "matos_typique": {'basses': ['Rickenbacker 4003', 'Fender Jazz Bass'], 'effets': ['Darkglass Alpha Omega'], 'amplis': ['Mesa Subway D-800'], 'baffles': ['GK Neo 4x10']}
    },
    {
        "nom": "Jean-Jacques Milteau",
        "origine": "France",
        "amplis_recommandes": ['Fender Rumble 500'],
        "baffles_recommandes": ['Ampeg 8x10'],
        "effets_recommandes": ['Overdrive', 'Vintage Microtubes', 'Envelope Filter'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Lakland Skyline'], 'effets': ['Overdrive', 'Vintage Microtubes', 'Envelope Filter'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Aguilar DB 410']}
    },
    {
        "nom": "Frédéric Monino",
        "origine": "France",
        "amplis_recommandes": ['Gallien-Krueger 800RB'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Octaver', 'Vintage Microtubes', 'Boss Chorus CEB-3', 'Compression'],
        "matos_typique": {'basses': ['Precision American Standard', 'Jazz Bass S-1'], 'effets': ['Octaver', 'Vintage Microtubes', 'Boss Chorus CEB-3', 'Compression'], 'amplis': ['Tech 21 GED-2112'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Jean-Philippe Viret",
        "origine": "France",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Bass Whammy', 'Octaver'],
        "matos_typique": {'basses': ['Music Man Sterling', 'Rickenbacker 4003'], 'effets': ['Bass Whammy', 'Octaver'], 'amplis': ['Darkglass Microtubes 900'], 'baffles': ['Hartke 4x10']}
    },
    {
        "nom": "Thierry Eliez",
        "origine": "France",
        "amplis_recommandes": ['Markbass Little Mark III'],
        "baffles_recommandes": ['EBS ClassicLine 1x15'],
        "effets_recommandes": ['Overdrive'],
        "matos_typique": {'basses': ['Fender Precision Bass', 'Precision American Standard'], 'effets': ['Overdrive'], 'amplis': ['Ampeg SVT-3 PRO'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Pierre Bensusan",
        "origine": "International",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['GK Neo 4x10'],
        "effets_recommandes": ['Reverb', 'Bass Whammy', 'Vintage Microtubes'],
        "matos_typique": {'basses': ['Squier Classic Vibe', 'Gibson Thunderbird'], 'effets': ['Reverb', 'Bass Whammy', 'Vintage Microtubes'], 'amplis': ['Hartke LH1000'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Jean-Luc Ponty",
        "origine": "France",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Bass Whammy'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Fender Jazz Bass'], 'effets': ['Bass Whammy'], 'amplis': ['Genz-Benz Streamliner STM-600'], 'baffles': ['Chillamp Classic 4x12']}
    },
    {
        "nom": "Claude Engel",
        "origine": "France",
        "amplis_recommandes": ['Hartke LH1000'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Bass Whammy', 'Reverb', 'Envelope Filter'],
        "matos_typique": {'basses': ['Warwick Corvette', 'Gibson Thunderbird'], 'effets': ['Bass Whammy', 'Reverb', 'Envelope Filter'], 'amplis': ['Aguilar Tone Hammer 500'], 'baffles': ['Mesa Boogie Subway 2x10']}
    },
    {
        "nom": "Denis Cuniot",
        "origine": "International",
        "amplis_recommandes": ['Tech 21 GED-2112'],
        "baffles_recommandes": ['Mesa Boogie Subway 2x10'],
        "effets_recommandes": ['Octaver', 'Bass Whammy', 'Delay'],
        "matos_typique": {'basses': ['Lakland Skyline', 'Fender Jazz Bass'], 'effets': ['Octaver', 'Bass Whammy', 'Delay'], 'amplis': ['Hartke LH1000'], 'baffles': ['Ampeg 8x10']}
    },
    {
        "nom": "Marc Berthoumieux",
        "origine": "France",
        "amplis_recommandes": ['Mesa Subway D-800'],
        "baffles_recommandes": ['Hartke 4x10'],
        "effets_recommandes": ['Octaver', 'Compression'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Fender Precision Bass'], 'effets': ['Octaver', 'Compression'], 'amplis': ['Ampeg VR'], 'baffles': ['Chillamp Classic 1x15']}
    },
    {
        "nom": "Philippe Bussonnet",
        "origine": "France",
        "amplis_recommandes": ['Darkglass Microtubes 900'],
        "baffles_recommandes": ['Aguilar DB 410'],
        "effets_recommandes": ['Octaver'],
        "matos_typique": {'basses': ['Ibanez SR500', 'Music Man Sterling'], 'effets': ['Octaver'], 'amplis': ['Fender Rumble 500'], 'baffles': ['Markbass 2x10']}
    },
]

effets_par_bassiste = {
    "Laurent Vernerey": ['Hyper Luminal', 'Bass Whammy', 'Empress ParaEQ'],
    "Nate Mendel": ['Hyper Luminal', 'Vintage Microtubes'],
    "Victoria De Angelis": ['Overdrive', 'Chorus'],
    "Krist Novoselic": ['Distorsion', 'Chorus'],
    "Paul McCartney": ['Bass Whammy'],
    "John Deacon": ['Reverb'],
    "Cliff Burton": ['Compression', 'Delay', 'Octaver'],
    "Geezer Butler": ['Bass Whammy'],
    "Sting": ['Delay', 'Overdrive'],
    "John Myung": ['Overdrive'],
    "Phil Lynott": ['Vintage Microtubes', 'Bass Whammy', 'Overdrive'],
    "Kim Deal": ['Delay', 'Overdrive'],
    "Tal Wilkenfeld": ['Hyper Luminal', 'Empress ParaEQ', 'Boss Chorus CEB-3'],
    "Esperanza Spalding": ['Envelope Filter', 'Delay', 'Empress ParaEQ'],
    "Nathan East": ['Darkglass Alpha Omega', 'Reverb'],
    "Pino Palladino": ['Delay'],
    "Carol Kaye": ['Darkglass Alpha Omega', 'Compression', 'Hyper Luminal', 'Overdrive'],
    "Donald Duck Dunn": ['Compression'],
    "Les Claypool": ['Boss Chorus CEB-3'],
    "Billy Sheehan": ['Hyper Luminal', 'Bass Whammy'],
    "Tony Kanal": ['Darkglass Alpha Omega', 'Overdrive'],
    "Adam Clayton": ['Overdrive', 'Compression'],
    "Robert Trujillo": ['Boss Chorus CEB-3'],
    "Jason Newsted": ['Compression', 'Reverb', 'Hyper Luminal'],
    "Mike Dirnt": ['Overdrive'],
    "Duff McKagan": ['Compression'],
    "Peter Hook": ['Reverb', 'Overdrive', 'Delay'],
    "Chris Wolstenholme": ['Hyper Luminal'],
    "Tim Commerford": ['Delay', 'Reverb', 'Boss Chorus CEB-3', 'Compression'],
    "Tina Weymouth": ['Octaver'],
    "Jack Bruce": ['Reverb', 'Boss Chorus CEB-3', 'Bass Whammy'],
    "Glenn Hughes": ['Envelope Filter'],
    "Graham Maby": ['Vintage Microtubes', 'Darkglass Alpha Omega'],
    "Jack Casady": ['Bass Whammy', 'Envelope Filter', 'Overdrive', 'Reverb'],
    "Boz Burrell": ['Compression', 'Hyper Luminal', 'Boss Chorus CEB-3', 'Envelope Filter'],
    "Roger Waters": ['Overdrive'],
    "Tom Hamilton": ['Overdrive', 'Bass Whammy', 'Vintage Microtubes', 'Octaver'],
    "Verdine White": ['Boss Chorus CEB-3', 'Hyper Luminal'],
    "Richard Bona": ['Envelope Filter', 'Boss Chorus CEB-3', 'Hyper Luminal'],
    "Dave Holland": ['Boss Chorus CEB-3'],
    "Gary Willis": ['Compression', 'Octaver', 'Reverb'],
    "Jimmy Haslip": ['Reverb', 'Darkglass Alpha Omega', 'Hyper Luminal'],
    "Stanley Clarke": ['Boss Chorus CEB-3', 'Empress ParaEQ', 'Darkglass Alpha Omega', 'Compression'],
    "John Patitucci": ['Overdrive', 'Hyper Luminal'],
    "Ron Carter": ['Reverb', 'Bass Whammy', 'Hyper Luminal', 'Overdrive'],
    "Will Lee": ['Boss Chorus CEB-3'],
    "Mark King": ['Compression', 'Empress ParaEQ'],
    "Rocco Prestia": ['Reverb', 'Envelope Filter', 'Compression', 'Delay'],
    "Johan De Farfalla": ['Boss Chorus CEB-3', 'Vintage Microtubes', 'Octaver'],
    "James LoMenzo": ['Vintage Microtubes', 'Overdrive', 'Octaver'],
    "Mel Schacher": ['Reverb', 'Overdrive'],
    "Klaus Voormann": ['Reverb', 'Overdrive'],
    "Mike Watt": ['Envelope Filter', 'Delay', 'Overdrive'],
    "Doug Wimbish": ['Octaver', 'Hyper Luminal', 'Reverb'],
    "Nick Beggs": ['Envelope Filter', 'Darkglass Alpha Omega', 'Reverb', 'Empress ParaEQ'],
    "John Taylor": ['Reverb', 'Bass Whammy', 'Overdrive', 'Darkglass Alpha Omega'],
    "Paul Simonon": ['Darkglass Alpha Omega'],
    "Colin Greenwood": ['Octaver', 'Darkglass Alpha Omega', 'Boss Chorus CEB-3', 'Reverb'],
    "Jack Lawrence": ['Reverb'],
    "Alain Caron": ['Delay', 'Darkglass Alpha Omega'],
    "Dominique Di Piazza": ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Reverb', 'Overdrive'],
    "Franck Hermanny": ['Overdrive'],
    "Etienne Mbappé": ['Delay', 'Bass Whammy'],
    "Michel Alibo": ['Envelope Filter', 'Empress ParaEQ', 'Overdrive', 'Vintage Microtubes'],
    "Guy Nsangué": ['Darkglass Alpha Omega'],
    "Fred Dupont": ['Envelope Filter', 'Vintage Microtubes', 'Darkglass Alpha Omega'],
    "Julien Herné": ['Reverb', 'Bass Whammy'],
    "Laurent David": ['Darkglass Alpha Omega', 'Vintage Microtubes', 'Delay', 'Reverb'],
    "Fifi Chayeb": ['Hyper Luminal', 'Boss Chorus CEB-3', 'Delay'],
    "Fred Monestier": ['Vintage Microtubes', 'Delay', 'Darkglass Alpha Omega'],
    "Nicolas Fiszman": ['Darkglass Alpha Omega'],
    "Sylvain Daniel": ['Overdrive', 'Boss Chorus CEB-3', 'Octaver'],
    "Jean Bisello": ['Octaver', 'Overdrive'],
    "Rémi Vignolo": ['Boss Chorus CEB-3', 'Compression', 'Overdrive', 'Octaver'],
    "Norbert "Nono" Krief": ['Octaver'],
    "Yves Carbonne": ['Compression', 'Darkglass Alpha Omega', 'Bass Whammy'],
    "Alain Perez": ['Compression', 'Octaver'],
    "Jean-Michel Kajdan": ['Boss Chorus CEB-3'],
    "Jean-Marc Jafet": ['Overdrive', 'Envelope Filter'],
    "Bernard Paganotti": ['Delay', 'Compression'],
    "Francis Moze": ['Reverb', 'Delay', 'Boss Chorus CEB-3'],
    "Jean-Claude Naimro": ['Octaver', 'Compression'],
    "Renaud Garcia-Fons": ['Darkglass Alpha Omega'],
    "Pascal Mulot": ['Compression', 'Octaver', 'Empress ParaEQ', 'Envelope Filter'],
    "Hervé Brault": ['Bass Whammy', 'Darkglass Alpha Omega', 'Octaver', 'Hyper Luminal'],
    "Philippe Chayeb": ['Bass Whammy', 'Reverb', 'Hyper Luminal', 'Overdrive'],
    "Thierry Fanfant": ['Bass Whammy', 'Empress ParaEQ', 'Delay', 'Octaver'],
    "Sébastien Chouard": ['Darkglass Alpha Omega'],
    "Jean-Jacques Milteau": ['Overdrive', 'Vintage Microtubes', 'Envelope Filter'],
    "Frédéric Monino": ['Octaver', 'Vintage Microtubes', 'Boss Chorus CEB-3', 'Compression'],
    "Jean-Philippe Viret": ['Bass Whammy', 'Octaver'],
    "Thierry Eliez": ['Overdrive'],
    "Pierre Bensusan": ['Reverb', 'Bass Whammy', 'Vintage Microtubes'],
    "Jean-Luc Ponty": ['Bass Whammy'],
    "Claude Engel": ['Bass Whammy', 'Reverb', 'Envelope Filter'],
    "Denis Cuniot": ['Octaver', 'Bass Whammy', 'Delay'],
    "Marc Berthoumieux": ['Octaver', 'Compression'],
    "Philippe Bussonnet": ['Octaver'],
}

def get_bassists():
    return [b["nom"] for b in bassistes]

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    preset = {}

    if basse == "Jazz Bass S-1":
        preset["Basse"] = {"Sélecteur": "Position 1 (série)", "Volume": "100%", "Tone": "70%"}
    elif basse == "Precision American Standard":
        preset["Basse"] = {"Volume": "100%", "Tone": "80%"}
    elif basse == "Music Man Sterling":
        preset["Basse"] = {"Volume": "100%", "EQ": "Flat", "Sélecteur": "Middle position"}
    else:
        preset["Basse"] = {"Réglages": "Standard", "Volume": "100%", "Tone": "50%"}

    if ampli == "Chillamp Beta":
        preset["Ampli"] = {"Volume": "4", "Treble": "5", "Medium": "6", "Bass": "7"}
    elif ampli == "Genz-Benz Streamliner STM-600":
        preset["Ampli"] = {"Gain": "3", "Volume": "5", "Bass": "6", "Mid": "5", "Treble": "6", "Master": "4"}
    elif ampli == "Chillamp Delta":
        preset["Ampli"] = {"Gain": "5", "Bass": "6", "Mid": "5", "Treble": "6", "Master": "5"}
    elif ampli == "Ampeg VR":
        preset["Ampli"] = {"Gain": "6", "Bass": "7", "Mid": "5", "Treble": "6", "Master": "5"}
    else:
        preset["Ampli"] = {"Réglages": "Classiques", "Master": "5"}

    for effet in effets:
        if effet == "Hyper Luminal":
            preset[effet] = {"Blend": "60%", "Time": "40%", "Output": "70%", "Ratio": "4:1", "Mode": "FET"}
        elif effet == "Vintage Microtubes":
            preset[effet] = {"Drive": "40%", "Tone": "50%", "Blend": "60%", "Level": "70%"}
        elif effet == "Bass Whammy":
            preset[effet] = {"Mode": "Octave Up", "Wet/Dry": "50%"}
        elif effet == "Empress ParaEQ":
            preset[effet] = {"Low": "+2dB", "Mid": "+1dB", "High": "0dB", "Q": "large"}
        else:
            preset[effet] = {"Réglage": "Standard"}

    return preset
