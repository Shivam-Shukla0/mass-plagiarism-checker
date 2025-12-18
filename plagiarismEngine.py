from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def checkPlagiarismMultiple(fileTexts, fileNames, threshold=1):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidfMatrix = vectorizer.fit_transform(fileTexts)

    similarityMatrix = cosine_similarity(tfidfMatrix)

    results = []
    totalFiles = len(fileNames)

    # i < j ensures:
    # - no self comparison (i != j)
    # - no duplicate comparison (A-B but not B-A)
    for i in range(totalFiles):
        for j in range(i + 1, totalFiles):
            similarity = round(similarityMatrix[i][j] * 100, 2)

            if similarity >= threshold:
                results.append({
                    "file1": fileNames[i],
                    "file2": fileNames[j],
                    "similarity": similarity
                })

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results
