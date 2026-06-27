def get_mitre_mapping(attack_type):

    mappings = {

        "Brute Force Attack": {
            "id": "T1110"
        },

        "Port Scan": {
            "id": "T1046"
        },

        "Suspicious Login": {
            "id": "T1078"
        }

    }

    return mappings.get(
        attack_type,
        {"id": "T0000"}
    )
