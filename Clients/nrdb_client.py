from requests import request

class NrdbClient:
    """
    API Client class for calling the NetrunnerDB API: https://netrunnerdb.com/api/2.0/doc
    API v2 Documentation: https://netrunnerdb.com/api/doc
    API v3-preview Documentation: https://api-preview.netrunnerdb.com/api/docs/

    v2 Base URL: https://netrunnerdb.com/
    Supported API Endpoints:
        /api/2.0/public/card/{card_code}
        /api/2.0/public/deck/{deck_id}  # might need to use /api/2.0/public/decklist/{decklist_id} instead
        /api/2.0/public/factions
        /api/2.0/public/faction/{faction_code}

    Unsupported API Endpoints:
        There are lots.  Check them all out here: https://netrunnerdb.com/api/doc

    Authentication: None, for public APIs.  This app does not use private APIs.
    """
    
    """
    Card 01001 is defined as:
    {"imageUrlTemplate":"https://static.nrdbassets.com/v1/large/{code}.jpg",
    "data":
        [{"base_link":0,
        "code":"01001",
        "deck_limit":1,
        "faction_code":"anarch",
        "faction_cost":0,
        "flavor":"\"Watch this. It'll be funny.\"",
        "illustrator":"Ralph Beisner",
        "influence_limit":15,
        "keywords":"G-mod",
        "minimum_deck_size":45,
        "pack_code":"core",
        "position":1,
        "quantity":1,
        "side_code":"runner",
        "stripped_text":"Whenever you install a virus program, the Corp trashes the top card of R&D.",
        "stripped_title":"Noise: Hacker Extraordinaire",
        "text":"Whenever you install a <strong>virus</strong> program, the Corp trashes the top card of R&D.",
        "title":"Noise: Hacker Extraordinaire",
        "type_code":"identity",
        "uniqueness":false}],
    "total":1,
    "success":true,
    "version_number":"2.0",
    "last_updated":"2021-03-13T05:08:22+00:00"}
    """
        
    def get_card(self, code)
        return https://netrunnerdb.com/api/2.0/public/card/01001
        
        
        
        
