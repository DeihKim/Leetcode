class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            res.add(local + '@' + domain)
        return len(res)

        '''
        res = set()
        for email in emails:
            local, domain = email.split('@')
            temp = ''
            for c in local:
                if c == '+':
                    break
                elif c == '.':
                    continue
                else:
                    temp += c
            res.add(temp + '@' + domain)
        return len(res)
        '''