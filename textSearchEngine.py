#Author: Junfu Cheng
#Organization: University of Florida

import numpy as np
from collections import Counter



class textSearchEngine:
    def __init__(self, vocabulary, documents, counts):
        self.words = self.openVocabulary( vocabulary)
        self.fragments = self.openDocs( documents)
        self.matrix = self.openMap( counts)

    def openVocabulary(self, vocabulary):
        with open(vocabulary, 'r') as file:
            content = file.read()
        words = np.array(content.split(','))
        print(words[:10])
        return words
        
    def openDocs(self, documents):
        # Open the file in read mode
        with open(documents, 'r', encoding='utf-8') as file:
        # Read all lines into a list, stripping any leading/trailing whitespace
            fragments = np.array([line.strip() for line in file])

        # Print the total number of fragments and the first few fragments for verification
        print(f"Total number of text fragments: {len(fragments)}")
        print("First 5 text fragments:")
        for fragment in fragments[:5]:
            print(fragment)
        return fragments
    
    def openMap(self, counts):
        # Load the data into a NumPy array
        matrix = np.loadtxt(counts, delimiter=',')
        # Print the shape of the matrix to verify
        print(f"Matrix shape: {matrix.shape}")

        # Optionally, print the first few rows and columns for verification
        print("First 5 rows of the matrix:")
        print(matrix[:5, :5])  # Print the first 5 rows and columns
        return matrix

    def encode(self, text):
        inputs = text.split()
        indices = []
        for value_to_find in inputs:
            indice = np.where(self.words == value_to_find)[0]
            # Get the first index or -1 if the value is not found
            first_index = indice[0] if indice.size > 0 else -1
            indices.append(first_index)
            print("The first index of value {} is: {}".format(value_to_find, first_index))
        print(indices)

        wordVector = [0] * len(self.words)
        indices_counter = dict(Counter(indices))
        for key, value in indices_counter.items():
            print(f"Key: {key}, Value: {value}")
            wordVector[key] = value
        wordVector = np.array(wordVector).reshape(-1, 1)
        print('wordVector is established.')
        print(wordVector)
        return wordVector

    def phiZ(self, wordVector):
        z = self.matrix @ wordVector
        # Flatten the column vector to a 1D array
        flattened_vector = z.flatten()

        # Get the indices that would sort the array in ascending order
        sorted_indices = np.argsort(flattened_vector)

        # Get the indices of the top three largest values
        top_three_indices = sorted_indices[-3:]  # The last three indices after sorting
        return top_three_indices

    def phiR(self, wordVector):
        # Compute the magnitude (Euclidean norm) of each row
        magnitudes = np.linalg.norm(self.matrix, axis=1, keepdims=True)

        # Avoid division by zero by replacing any zero magnitudes with 1
        magnitudes[magnitudes == 0] = 1

        # Divide each element by the magnitude of its row
        normalized_matrix = self.matrix / magnitudes
        normalized_matrix = normalized_matrix / magnitudes
        z =  normalized_matrix @ wordVector
        # Flatten the column vector to a 1D array
        flattened_vector = z.flatten()

        # Get the indices that would sort the array in ascending order
        sorted_indices = np.argsort(flattened_vector)

        # Get the indices of the top three largest values
        top_three_indices = sorted_indices[-3:]  # The last three indices after sorting
        return top_three_indices
    
    def phiV(self, wordVector):
        # Compute the magnitude (Euclidean norm) of each row
        magnitudes = np.linalg.norm(self.matrix, axis=1, keepdims=True)

        # Avoid division by zero by replacing any zero magnitudes with 1
        magnitudes[magnitudes == 0] = 1

        # Divide each element by the magnitude of its row
        normalized_matrix = self.matrix / magnitudes

        # Compute the magnitude (Euclidean norm) of the column vector
        magnitude = np.linalg.norm(wordVector)

        # Avoid division by zero by replacing magnitude with 1 if it is zero
        magnitude = magnitude if magnitude != 0 else 1

        normalized_matrix = normalized_matrix/magnitude

        z = normalized_matrix @ wordVector
        # Flatten the column vector to a 1D array
        flattened_vector = z.flatten()

        # Get the indices that would sort the array in ascending order
        sorted_indices = np.argsort(flattened_vector)

        # Get the indices of the top three largest values
        top_three_indices = sorted_indices[-3:]  # The last three indices after sorting
        return top_three_indices

    def showSearchResult(self, top_three_indeices):
        for index in top_three_indeices:
            print(self.fragments[index])
