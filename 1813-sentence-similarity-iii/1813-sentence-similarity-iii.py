class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure words1 is the longer list
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        len_words1 = len(words1)
        len_words2 = len(words2)

        # Check for matching from the start
        start_index = 0
        while start_index < len_words2 and words1[start_index] == words2[start_index]:
            start_index += 1

        # Check for matching from the end
        end_index = 0
        while end_index < len_words2 and words1[len_words1 - 1 - end_index] == words2[len_words2 - 1 - end_index]:
            end_index += 1

        # Check if the unmatched part of the longer sentence can accommodate the unmatched part of the shorter sentence
        return start_index + end_index >= len_words2