
YOUR_S3_BUCKET = "django-home-buying"

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
AWS_S3_BUCKET_NAME_STATIC = YOUR_S3_BUCKET

# These next two lines will serve the static files directly
# from the s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % YOUR_S3_BUCKET
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

print(STATIC_URL)
