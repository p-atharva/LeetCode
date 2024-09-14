class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for e in emails:
            ch, local_name = 0, ""
            local_name, domain = e.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".","")
            unique_emails.add((local_name, domain))

        return len(unique_emails)