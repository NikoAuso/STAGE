# Definisci il pattern per il numero di telefono
phone_pattern = [
    {"label": "PHONE", "pattern": [
        {"TEXT": {"regex": r"^((00|\+)39[\.\s\-\/]??)"}, "OP": "?"},
        {"TEXT": {
            "regex": r"((3\d{2}[\.\s\-\/]??)((\d([\.\s\-\/]??)){7})\s??$|(\d{2,4}[\.\s\-\/]??)(\d[\.\s\-\/]??){6,8})\s??$"}}]
     }
]