# Item Based
# User Based
# Formula - Cosine Similarity, Euclidean, Pearson, Jaccard Distance

dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user = {"ironman", "kgf", "avengers", "thor", "the mask", "zero", "sultan", "dabang"}
# 1. compare all categories with user using Jaccard Distance
# 2. now compare jaccard score and get max score
# 3. the category containing max score will be the category that user watches most
# 4. now recommend movies of that category to user that user has not watched yet...



