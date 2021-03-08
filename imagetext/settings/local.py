"""Local settings for docker."""
from .base import *  # noqa: F403

# 1. APPLICATION DEFINITION

DEBUG = True
PRODUCTION = False

#INSTALLED_APPS += ['debug_toolbar']

#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]


# 2. DATABASE
# 3. STATIC FILES (CSS, JavaScript, Images)
# 4. SECURITY SETTINGS

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)


# 5. PACKAGE-SPECIFIC SETTINGS
# 6. INTERNATIONALIZATION
# 7. EMAIL SETTINGS
# 8. EXTERNAL API SETTINGS
# 9. REDIS SETTINGS
# 10. SAML SETTINGS
# 11. LOGGING SETTINGS
# 12. SESSIONS SETTINGS
# 13. DATA UPLOAD SETTINGS
