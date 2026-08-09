from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] = counts.get(subdomain, 0) + count

        result = []

        for domain, count in counts.items():
            result.append(f"{count} {domain}")

        return result