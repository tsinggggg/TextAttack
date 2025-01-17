"""
multilingual universal sentence encoder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

import tensorflow_hub as hub
import tensorflow_text  # noqa: F401

from textattack.constraints.semantics.sentence_encoders import SentenceEncoder


class MultilingualUniversalSentenceEncoder(SentenceEncoder):
    """Constraint using similarity between sentence encodings of x and x_adv
    where the text embeddings are created using the Multilingual Universal
    Sentence Encoder."""

    def __init__(self, threshold=0.8, large=False, metric="angular", **kwargs):
        super().__init__(threshold=threshold, metric=metric, **kwargs)
        if large:
            tfhub_url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3"
        else:
            tfhub_url = (
                "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"
            )

        # TODO add QA SET. Details at: https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3

        self.model = hub.load(tfhub_url)

    def encode(self, sentences):
        return self.model(sentences).numpy()
