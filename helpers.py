def get_elastic_query(search_terms):
    return {
            "multi_match": {
                "query": search_terms,
                "fields": [
                    "title^5",
                    "description",
                    "category5_name^2",
                    "handle^4",
                    "shopify_subcategory^3",
                    "store_name"
                ]
            }
        }