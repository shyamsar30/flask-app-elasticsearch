class Config:
    ELASTICSEARCH_HOST_NAME = "https://192.168.1.9:9200/"
    SSL_ASSERT_FINGERPRINT = 'SSL_ASSERT_FINGERPRINT_HERE'
    USERNAME = 'shyam'
    PASSWORD = 'ASKSHYAMFORPASSWORD'
    ELASTIC_INDEX_NAME = 'products_v2'
    DEFAULT_FETCH_SIZE = 20
    AUTO_COMPLETE_FIELDS = ['category5_name', 'store_name', 'shopify_subcategory', 'title']
