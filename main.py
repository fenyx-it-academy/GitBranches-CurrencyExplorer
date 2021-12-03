import sys
from greet_user import greet_and_get_currency
from fetch_api import fetch_currency
from cleanup import cleanup_result



if __name__ == "__main__":
    try:
        currency = greet_and_get_currency()
        result_dictionary = fetch_currency(currency)
        cleanup_result(result_dictionary)
    except Exception as err:
        sys.exit(err)

