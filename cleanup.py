import pprint

def cleanup_result(dictionary):
    """
    docstring
    """
    
    new_dictionary = {
        "Time of last update": dictionary['time_last_update_utc'],
        "Currency of choice": dictionary['base_code'],
        "Conversion rates": {
            "USD": dictionary['conversion_rates']["USD"],
            "EUR": dictionary['conversion_rates']["EUR"],
            "GBP": dictionary['conversion_rates']["GBP"],
            "CHF": dictionary['conversion_rates']["CHF"],
            "CAD": dictionary['conversion_rates']["CAD"],
            "TRY": dictionary['conversion_rates']["TRY"],
         }

    }

    pprint.pprint(new_dictionary, sort_dicts=False)
