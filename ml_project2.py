'''                                         AI Text Generator - Next Word Predictor
a probability machine which lerns the pattern based on the previous words and predicts the most likely next word.'''

#LSTM = Long-Term Short Memory; gets rid of the vanishing gradient problem in Recurrent Neural Networks.
#n-gram sequence creation => using one case as multiple training sample.

#working with Marry Shelly's "Frankenstein or The Modern Prometheus"; downloaded from 'The Project Gutenberg'

try:
    with open('frankenstein.txt','r', encoding='utf-8') as f:
        data = f.read()
        print(f"No. of characters: {len(data)}")
        d = data.split()
        print(f"No. of words (punctuation included): {len(d)}")
except FileNotFoundError:
    print("File not found.")