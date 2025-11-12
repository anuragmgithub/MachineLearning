from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The Eiffel Tower is in Paris.",
    "The Statue of Liberty is in New York.",
    "Mount Everest is the tallest mountain."
]

embeddings = model.encode(sentences)
query = "Where is the Eiffel Tower?"

query_emb = model.encode(query)
scores = util.cos_sim(query_emb, embeddings)

for i, score in enumerate(scores[0]):
    print(sentences[i], "→", float(score))
