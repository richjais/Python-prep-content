# Input params : 5 arguments =>
# 1. numCompetitors- an integer representing the number of competitors for the Echo device
# 2. topNCompetitors- is an integer representing the maximum number of competitors that Amazon wants to identify
# 3. competitors- a list of strings representing the competitors
# 4. numReviews- an integer representing the number of reviews from different websites that are identified by the automated webcrawler
# 5. reviews, a list of string where each element is a string that consists of space-separated words representing user reviews.
# Output: Return a list of strings representing Amazon's top N competitors in order of most frequently mentioned to least frequent.
# Note =>
# The comparison of strings is case-insensitive.
# If the value of topNCompetitors is more than the number of competitors discussed in the reviews then output the names of only the competitors mention.
# If competitors have the same count (e.g. newshop=2, shopnow=2, mymarket=4), sort alphabetically. topNCompetitors=2, Output=[mymarket, newshop]

from collections import OrderedDict


def topNCompete(competitors, reviews, top):
    d = OrderedDict()
    for sentence in reviews:
        sentence = sentence.lower()
        for word in competitors:
            if word in sentence:
                if word in d.keys():
                    d[word] += 1
                else:
                    d[word] = 1
    # print(sorted(d.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))
    res = []
    for i in range(top):
        listk = list(d.keys())
        res.append(listk[i])
    return res


numCompetitors = 6
topNCompetitors = 2
competitors = ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"]
numReviews = 6
reviews = [
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "mymarket has awesome services",
    "Thanks Newshop for the quick delivery"]
print(topNCompete(competitors, reviews, topNCompetitors))
