"""
Contraction is a short form of a formal phrase:
You are -> You're
We are -> We're
Did not -> Didn't
and so on.

This test code aims to recognise contractions and expansions as one text.

Dictionary will be used to map contractions to their expansions and vice versa.
1. Dictionary of contractions.
2. Search the keys based on user input.
3. Output the item of the key.

I tried to use an alternative approach which requires the following module:
pycontractions
However, I couldn't install it due to IDE/PIP errors. 
"""

contractions = {
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he's": "he is / he has",
    "I'd": "I would / I had",
    "I'll": "I will",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it's": "it is / it has",
    "let's": "let us",
    "she's": "she is / she has",
    "shouldn't": "should not",
    "that's": "that is / that has",
    "there's": "there is / there has",
    "they'd": "they would / they had",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would / we had",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what's": "what is / what has",
    "where's": "where is / where has",
    "who's": "who is / who has",
    "won't": "will not",
    "wouldn't": "would not",
    "you're": "you are",
    "you've": "you have"
}

while True:
    user_input = input("Please enter a contraction: ")

    expansion = contractions.get(user_input, "Expansion for this contraction was not found.")

    print(expansion)