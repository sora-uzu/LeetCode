class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split("@")
            newLocal = ''
            for i in local:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    newLocal += i
            res.add(newLocal + "@" + domain)
        return len(res)
