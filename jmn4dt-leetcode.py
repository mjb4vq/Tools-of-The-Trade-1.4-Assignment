class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        
        words_list = sentence.split()
        for word in words_list:
            accumulate_word = ''
            for char in word:
                accumulate_word = accumulate_word + char
                if (accumulate_word == searchWord):
                    answer = words_list.index(word) + 1
                    return answer
        return -1