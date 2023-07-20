
from string import punctuation
from collections import Counter
from collections import defaultdict

post_comments_with_labels = [
    ("I love this post.", "pos"),
    ("This post is your best work.", "pos"),
    ("I really liked this post.", "pos"),
    ('I agree 100 percent. This is true', 'pos'),
    ("This post is spot on!", "pos"),
    ("So smart!", "pos"),
    ("What a good point!", "pos"),
    ("Bad stuff.", "neg"),
    ("I hate this.", "neg"),
    ("This post is horrible.", "neg"),
    ("I really disliked this post.", "neg"),
    ("What a waste of time.", "neg"),
    ("I do not agree with this post.", "neg"),
    ("I can't believe you would post this.", "neg"),
]

class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}
        self.sample_count = len(samples)
        for text, label in samples:
            self.mapping[label] += self.tokenize(text)
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []

        for token in tokens:
            pos.append(self.pos_counter[token]/self.sample_count)
            neg.append(self.neg_counter[token]/self.sample_count)
            
        
        



cl = NaiveBayesClassifier(post_comments_with_labels)

show_expected_result = False
show_hints = False

def get_sentiment(text):
    cl = NaiveBayesClassifier(post_comments_with_labels)
    return cl.classify(text)