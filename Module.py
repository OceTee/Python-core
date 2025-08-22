def text_cleaner(text):
    """
    Cleans the input text by removing leading and trailing whitespace,
    converting it to lowercase, and replacing multiple spaces with a single space.
    
    Args:
        text (str): The input text to be cleaned.
        
    Returns:
        str: The cleaned text.
    """
    cleaned_text = ' '.join(text.strip().lower().split())
    return cleaned_text

def number_formatter(number):
    """
    Formats a number with commas as thousands separators.
    
    Args:
        number (int or float): The number to be formatted.
        
    Returns:
        str: The formatted number as a string.
    """
    return f"{number:,}"

def date_converter(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' format to 'DD/MM/YYYY'.
    
    Args:
        date_str (str): The date string in 'YYYY-MM-DD' format.
        
    Returns:
        str: The date string in 'DD/MM/YYYY' format.
    """
    year, month, day = date_str.split('-')
    return f"{day}/{month}/{year}"