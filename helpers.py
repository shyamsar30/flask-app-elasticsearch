def gen_query_for_auto_complete(field, query):

    return {
    "bool": {
      "should": [
        {
          "multi_match": {
            "query": query,
            "type": "bool_prefix",
            "fields": [
              field,
              field + "._2gram",
              field + "._3gram"
            ],
            "operator": "and"
          }
        }
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
              "query": search_terms,
              "analyzer": "my_stop_analyzer"
            }
          }
        },
        {
          "match": {
            "handle": {
              "query": search_terms,
              "analyzer": "my_stop_analyzer"
            }
          }
        },
        {
          "match": {
            "shopify_subcategory": {
              "query": search_terms,
              "analyzer": "my_stop_analyzer"
            }
          }
        },
        {
          "match": {
            "description": {
              "query": search_terms,
              "analyzer": "my_stop_analyzer"
            }
          }
        }
      ]
    }
  }

  #   return {
  #   "bool": {
  #     "should": [
  #       {
  #         "match_phrase": {
  #           "store_name": {
  #             "query": search_terms,
  #             "boost": 10
  #           }
  #         }
  #       },
  #       {
  #         "match_phrase": {
  #           "category5_name": {
  #             "query": search_terms,
  #             "boost": 8
  #           }
  #         }
  #       },
  #       {
  #         "match_phrase": {
  #           "title": {
  #             "query": search_terms,
  #             "boost": 6
  #           }
  #         }
  #       },
  #       {
  #         "match_phrase": {
  #           "handle": {
  #             "query": search_terms,
  #             "boost": 4
  #           }
  #         }
  #       },
  #       {
  #         "match_phrase": {
  #           "shopify_subcategory": {
  #             "query": search_terms,
  #             "boost": 2
  #           }
  #         }
  #       },
  #       {
  #         "match_phrase": {
  #           "description": {
  #             "query": search_terms
  #           }
  #         }
  #       },
  #       {
  #         "match": {
  #           "category5_name": {
  #             "query": search_terms
  #           }
  #         }
  #       },
  #       {
  #         "match": {
  #           "title": {
  #             "query": search_terms
  #           }
  #         }
  #       },
  #       {
  #         "match": {
  #           "handle": {
  #             "query": search_terms
  #           }
  #         }
  #       },
  #       {
  #         "match": {
  #           "shopify_subcategory": {
  #             "query": search_terms
  #           }
  #         }
  #       },
  #       {
  #         "match": {
  #           "description": {
  #             "query": search_terms
  #           }
  #         }
  #       }
  #     ]
  #   }
  # }

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