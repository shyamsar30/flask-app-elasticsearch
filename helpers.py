def get_auto_search(search_term) :
    
    return {
      # "match_phrase": {
      #   "title": {
      #     "query": search_term,
      #     "boost": 10
      #   }
      # }
      "multi_match": {
            "query": search_term,
            "fields": [
                "store_name^5",
                "title"
            ]
        }
    }

def get_elastic_query(search_terms):

    return {
    "bool": {
      "should": [
        {
          "match_phrase": {
            "store_name": {
              "query": search_terms,
              "boost": 10
            }
          }
        },
        {
          "match_phrase": {
            "category5_name": {
              "query": search_terms,
              "boost": 8
            }
          }
        },
        {
          "match_phrase": {
            "title": {
              "query": search_terms,
              "boost": 6
            }
          }
        },
        {
          "match_phrase": {
            "handle": {
              "query": search_terms,
              "boost": 4
            }
          }
        },
        {
          "match_phrase": {
            "shopify_subcategory": {
              "query": search_terms,
              "boost": 2
            }
          }
        },
        {
          "match_phrase": {
            "description": {
              "query": search_terms
            }
          }
        },
        {
          "match": {
            "category5_name": {
              "query": search_terms
            }
          }
        },
        {
          "match": {
            "title": {
              "query": search_terms
            }
          }
        },
        {
          "match": {
            "handle": {
              "query": search_terms
            }
          }
        },
        {
          "match": {
            "shopify_subcategory": {
              "query": search_terms
            }
          }
        },
        {
          "match": {
            "description": {
              "query": search_terms
            }
          }
        }
      ]
    }
  }

    ##########################################################33
    # return {
    #         "multi_match": {
    #             "query": search_terms,
    #             "fields": [
    #                 "title^5",
    #                 "description",
    #                 "category5_name^2",
    #                 "handle^4",
    #                 "shopify_subcategory^3",
    #                 "store_name"
    #             ]
    #         }
    #     }


    ########################################################
#     return {
#     "bool": {
#       "should": [
#         {
#           "match_phrase": {
#             "store_name": {
#               "query": search_terms,
#               "boost": 3
#             }
#           }
#         },
#         {
#           "match": {
#             "category5_name": {
#               "query": search_terms,
#               "boost": 2
#             }
#           }
#         },
#         {
#           "match": {
#             "title": {
#               "query": search_terms
#             }
#           }
#         },
#         {
#           "match": {
#             "handle": {
#               "query": search_terms
#             }
#           }
#         },
#         {
#           "match": {
#             "shopify_subcategory": {
#               "query": search_terms
#             }
#           }
#         },
#         {
#           "match": {
#             "description": {
#               "query": search_terms
#             }
#           }
#         }
#       ]
#     }
#   }