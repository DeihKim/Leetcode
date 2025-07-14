class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start = set()
        for city1, city2 in paths:
            start.add(city1)
        for city1, city2 in paths:
            if city2 not in start:
                return city2
        '''
        Origianl
        start = set()
        for path in paths:
            start.add(path[0])
        for path in paths:
            if path[1] not in start:
                return path[1]
        '''

