import collections
from itertools import combinations
from typing import List


class Solution:
    def analyzeUserWebsiteVisitPatterns(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        website_by_user = {}
        for user in username:
            website_by_user[user] = []
            for site in website:
                website_by_user[user].append(site)

        max_pattern = ['aaa', float('-inf')]
        pattern_scores = {}
        for user in website_by_user.keys():
            sites_for_user = website_by_user[user]
            left = 0 
            right = 2
            while right < len(sites_for_user):
                pattern = tuple(sites_for_user[left:right + 1])
                pattern_scores[pattern] = pattern_scores.get(pattern, 0) + 1
                if pattern_scores[pattern] > max_pattern[1]:
                    max_pattern[0] = pattern
                    max_pattern[1] = pattern_scores[pattern]

                left += 1
                right += 1

        return max_pattern[0]


    def optimalSolution(self, username, timestamp, website):
        users = collections.defaultdict(list)

        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            users[user].append(site)

        patterns = collections.Counter()

        for user, sites in users.items():
            patterns.update(collections.Counter(set(combinations(sites, 3))))

        return max(sorted(patterns), key = patterns.get)

    def explainOptimal(self, username, timestamp, website):
        def combinations(lst):
            res = set()
            for i in range(len(lst) - 2):
                for j in range(i + 1, len(lst) - 1):
                    for k in range(j + 1, len(lst)):
                        res.add((lst[i], lst[j], lst[k]))

            return res

        # step 1: sort the entire stream and hash into dict
        # O(nlogn)
        user_site_history = collections.defaultdict(list) # {user: [site1, site2, site3]}
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            user_site_history[user].append(site)

        # step 2: combinations
        # O(n^3)
        seq_freq = collections.Counter()
        for user, sites in user_site_history.items():
            combination_set = combinations(sites)
            seq_freq.update(combination_set)

        # step 3: return highest occuring pattern
        return max(sorted(seq_freq), key=seq_freq.get) 


if __name__ == '__main__':
    username = ['joe', 'joe', 'joe', 'james', 'james', 'james', 'mary', 'mary', 'mary']
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']
    s = Solution()
    print(s.explainOptimal(username, timestamp, website))