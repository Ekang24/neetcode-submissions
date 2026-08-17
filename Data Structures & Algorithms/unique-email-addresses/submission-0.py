class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')

            local = local.split('+')[0]
            local = local.replace('.', '')

            norm = local + '@' + domain
            unique.add(norm)
        return len(unique)
        