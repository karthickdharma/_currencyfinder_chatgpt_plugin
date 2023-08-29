import openai
import requests

def find_currency_with_api_key(country, api_key):
    try:
        # Set up the OpenAI API key
        openai.api_key = api_key

        # Make a GET request to the REST Countries API
        response = requests.get(f'https://restcountries.com/v3.1/name/{country}')
        data = response.json()

        # Check if the API returned valid data
        if response.ok and data:
            # Extract currency information from the API response
            currencies = data[0].get('currencies', {})

            # Extract currency codes
            currency_codes = ', '.join(currencies.keys())

            return f'Currency of {country}: {currency_codes}'
        else:
            return f'Currency not found for {country}'
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

# Example usage of the external plugin
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    api_key = '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'

    # Get user input for the country name
    user_input = input('Enter a country name: ')

    # Call the external plugin function to find and display the currency
    result = find_currency_with_api_key(user_input, api_key)

    if result:
        print(result)
