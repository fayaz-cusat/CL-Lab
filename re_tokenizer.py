import re

def tokenize(text):
    # Regular expression pattern
    pattern = r"""
        \b(?:[A-Za-z]\.){2,}(?=\s|$)         # Abbreviations like U.S.A.
        | \b\w+(?:-\w+)+\b                   # Hyphenated words like ice-cream
        | \b\w+n't\b                         # Contractions ending in n't like isn't
        | \b\w+'\w+\b                        # Other contractions like I'm, you're
        | \b\w+\b                            # Regular words
        | [.,!?;:"()]                        # Punctuation
        | [\$\%\&\#@\*\+-=\/\\<>^~\|]        # Special symbols
    """
    
    # Compile the regular expression with VERBOSE mode for readability
    tokenizer = re.compile(pattern, re.VERBOSE)
    
    # Find all matches in the text
    tokens = tokenizer.findall(text)
    
    # Post-process to split contractions like "isn't" into "is" and "n't"
    processed_tokens = []
    for token in tokens:
        if re.match(r"\b\w+n't\b", token):  # Check if the token is a contraction ending in n't
            processed_tokens.append(token[:-3])  # Append the base word
            processed_tokens.append(token[-3:])  # Append n't as a separate token
        else:
            processed_tokens.append(token)
    
    return processed_tokens

# Example usage
text = "Isn't it great? I had ice-cream in the U.S.A."
tokens = tokenize(text)
print(tokens)

