"""This code compares 2 document-based files to measure their similarity"""

from file_processing import File, CosineSimilarity, LevenshteinDistance

FILE_PATH_1 = ''
FILE_PATH_2 = ''

if __name__ == '__main__':
    file_1 = File(FILE_PATH_1)
    file_2 = File(FILE_PATH_2)

    # Calculate cosine similarity
    cosine = CosineSimilarity(file_1, file_2).calculate()
    print(f"Cosine similarity: {cosine}")

    # Calculate Levenshtein distance
    levenshtein = LevenshteinDistance(file_1, file_2).calculate()
    print(f"Levenshtein distance: {levenshtein}")
