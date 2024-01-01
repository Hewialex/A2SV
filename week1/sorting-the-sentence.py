class Solution:
    def sortSentence(self, s: str) -> str:
    
        words = s.split()
        reconstructed = []

        for word in words:
            position = int(word[-1])
            reconstructed.append((word[:-1], position))

        reconstructed.sort(key=lambda x: x[1])

        original_sentence = ' '.join(word[0] for word in reconstructed)

        return original_sentence    