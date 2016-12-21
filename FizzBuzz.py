class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_list = []
        for i in range(1, n+1):
            if i % 3 != 0 and i % 5 != 0:
                ret_list.append(str(i))
            else:
                if i % 3 == 0 and i % 5 == 0:
                    ret_list.append('FizzBuzz')
                elif i % 3 == 0:
                    ret_list.append('Fizz')
                else:
                    ret_list.append('Buzz')
        return ret_list