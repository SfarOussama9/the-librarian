"""The embedding model, loaded through fastembed (ONNX, no PyTorch needed)."""

import os

from fastembed import TextEmbedding
from fastembed.common.model_description import ModelSource, PoolingType

MODEL = "intfloat/multilingual-e5-small"
DIM = 384

# fastembed does not ship multilingual-e5-small, but the model repo publishes an
# ONNX export, so we register it ourselves.
try:
    TextEmbedding.add_custom_model(
        model=MODEL,
        pooling=PoolingType.MEAN,
        normalization=True,
        sources=ModelSource(hf=MODEL),
        dim=DIM,
        model_file="onnx/model.onnx",
    )
except ValueError:
    pass  # already registered in this process

# In a container, ONNX Runtime sees all of the host's cores and oversubscribes the
# few the container may use; ONNX_THREADS caps it (set in deploy/modal_app.py).
THREADS = int(os.environ["ONNX_THREADS"]) if os.getenv("ONNX_THREADS") else None

_model = None


def model():
    global _model
    if _model is None:
        _model = TextEmbedding(MODEL, threads=THREADS)
    return _model


# e5 models are trained with these prefixes; leaving them out hurts retrieval.
def embed_passages(texts, batch_size=32):
    return list(model().embed([f"passage: {t}" for t in texts], batch_size=batch_size))


def embed_query(text):
    return next(iter(model().embed([f"query: {text}"])))
