class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        lyst = []
        for i in emails:
            names = i.split('@')
            localName = names[0]
            domainName = names[1]
            if '.' in localName:
                localName = localName.replace('.', '')
            if '+' in localName:
                localName = localName.split('+')
                localName = localName[0]
            name = localName + '@' + domainName
            lyst.append(name)
        return len(set(lyst))
