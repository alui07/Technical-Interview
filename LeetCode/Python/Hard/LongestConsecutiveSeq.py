""" 128. Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create two dictionary copies of the list 
        # consec is the dictionary that will be changing in size
        consec = {}
        for num in nums:
            consec[num] = 0
        # refConsec is the dictionary that will be referenced and not change in
        # size
        refConsec = copy.deepcopy(consec)
        
        # I'm planning to iterate through the reference dictionary, and removing
        # elements from the other, Python won't allow me to iterate through
        # dictionaries that change size

        # The algorithm functions as follows:
        # for every key in the reference dictionary, check all elements that are
        # part of the sequence (next element = key += 1) in both directions
        # popping from the "consec" dictionary, to avoid the changing size dict
        # error, iterate over the reference dictionary.

        # after you check all consecutive elements to the left, go back to the
        # origin point, "savePoint"
        savePoint = 0

        # length of current sequence
        lenConsec = 0

        # largest length of all sequences
        maxConsec = 0

        for key in refConsec:
            # if reference key is not in changing size dictionary, move on to
            # next key
            if key not in consec: continue

            # save the current key "position" then set length of current
            # sequence to 1
            savePoint = key
            lenConsec = 1
            
            # go left
            while key - 1 in consec:
                consec.pop(key-1)
                key -= 1
                lenConsec += 1

            # reset current key position back to the "middle" or starting point
            key = savePoint

            # go right
            while key + 1 in consec:
                consec.pop(key+1)
                key += 1
                lenConsec += 1
                
            # change longest length sequence if length of current sequence is
            # longer
            if lenConsec > maxConsec: maxConsec = lenConsec
                
        return maxConsec