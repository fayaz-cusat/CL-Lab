class FiniteStateTransducer:
    def __init__(self):
        self.sounds_that_trigger_e_insertion = {'x', 's', 'z'}

    def pluralize(self, word):
        # Check if the last character is one of the triggering sounds
        if word and word[-1] in self.sounds_that_trigger_e_insertion:
            return word + 'es'  # Insert 'e' before 's' and output 'es'
        else:
            return word + 's'  # Just add 's' for other cases

# Example usage
if __name__ == "__main__":
    fst = FiniteStateTransducer()
    
    # Test cases
    singular_words = ['box', 'class', 'buzz', 'cat', 'dog', 'fox', 'bus']
    plural_forms = {word: fst.pluralize(word) for word in singular_words}
    
    # Output the results
    for singular, plural in plural_forms.items():
        print(f"{singular} -> {plural}")