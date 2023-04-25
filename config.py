class Config:
    ELASTICSEARCH_HOST_NAME = "https://192.168.1.152:9200/"
    SSL_ASSERT_FINGERPRINT = 'b5dca61e04fc664708ba468556d975ce8e5d157f8852491e276cf5fb4cfb58b6'
    USERNAME = 'shyam'
    PASSWORD = 'shyam@elastic'
    ELASTIC_INDEX_NAME = 'products_v2'
    DEFAULT_FETCH_SIZE = 20
    AUTO_COMPLETE_FIELDS = ['category5_name', 'store_name', 'shopify_subcategory', 'title']