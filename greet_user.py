def greet_and_get_currency():
    """
    this function greets the user and asks the currency of their choice.
    """
    print("Welcome to CurrencyExplorer App. Please provide your currency of choice and we will fetch the latest data for you.")
    currency = input("Currency: ")
    
    return currency.upper()
