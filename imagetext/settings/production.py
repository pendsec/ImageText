"""Production settings."""
from imagetext.settings.base import *

# 1. APPLICATION DEFINITION
PRODUCTION = True
DEBUG = False


# 2. DATABASE
# 3. STATIC FILES (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# 4. SECURITY SETTINGS

ADMINS = []

CSRF_COOKIE_SECURE = True


# 5. PACKAGE-SPECIFIC SETTINGS
# 6. INTERNATIONALIZATION
# 7. EMAIL SETTINGS
# 8. EXTERNAL API SETTINGS
# 9. REDIS SETTINGS
# 10. SAML SETTINGS
# 11. LOGGING SETTINGS
# 12. SESSIONS SETTINGS

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 62400  # 24 hours


# 13. DATA UPLOAD SETTINGS
