from typing import List
from collections import defaultdict


class Solution:
    """Solution for merging user accounts with shared email addresses.

    Given a list of accounts where each element accounts[i] is a list of strings,
    the first element accounts[i][0] is the account name, and the rest are
    email addresses. Two accounts are considered to belong to the same person if
    there is at least one common email between them. After merging such accounts,
    return the resulting accounts with the name first and all unique emails
    sorted lexicographically. The order of the accounts in the result can be
    arbitrary. :contentReference[oaicite:0]{index=0}
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Merges accounts based on common emails.

        Args:
            accounts (List[List[str]]): A list of accounts, where each account
                starts with a name followed by one or more email strings.

        Returns:
            List[List[str]]: A list of merged accounts, each starting with the
                account name followed by sorted unique emails.
        """
        # accounts[i][0]  is name
        # accounts[i][1:] are emails
        # two accounts belong the same person if there is a common email to both accounts
        # people can have the same name

        email_to_indices = defaultdict(list)
        for i, entry in enumerate(accounts):
            emails = entry[1:]
            for email in emails:
                email_to_indices[email].append(i)

        rank = {i: 0 for i in range(len(accounts))}
        parent = {i: i for i in range(len(accounts))}

        def get_parent(i: int) -> int:
            if parent[i] == i:
                return i

            parent[i] = get_parent(parent[i])
            return parent[i]

        def union(a: int, b: int):
            parent_a = get_parent(a)
            parent_b = get_parent(b)

            if parent_a == parent_b:
                return

            if rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
            elif rank[parent_a] < rank[parent_b]:
                parent[parent_a] = parent_b
            else:
                parent[parent_b] = parent_a
                rank[parent_a] += 1

        for indices in email_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])

        parent_to_emails = defaultdict(set)
        for i, entry in enumerate(accounts):
            parent_idx = get_parent(i)
            for email in entry[1:]:
                parent_to_emails[parent_idx].add(email)

        res = []
        for parent_idx, emails in parent_to_emails.items():
            name = accounts[parent_idx][0]
            res.append([name] + list(sorted(emails)))

        return res
