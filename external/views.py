"""External views."""
from django.views.generic import TemplateView


class ImagetextLandingView(TemplateView):
    """Basic backend view to call frontend from."""

    template_name = "base.html"