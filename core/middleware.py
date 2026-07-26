import re

from django.shortcuts import redirect

MOBILE_UA_RE = re.compile(
    r"Mobi|Android|iPhone|iPod|IEMobile|BlackBerry|Opera Mini",
    re.IGNORECASE,
)

# desktop path -> matching mobile app path
DESKTOP_TO_APP = {
    "/": "/app/",
    "/about/": "/app/about/",
    "/feedback/": "/app/feedback/",
}

class MobileRedirectMiddleware:
    """Send phones hitting a desktop page to the matching /app/ mobile view.

    Tablets and iPads (no "Mobi" token in their UA) are left on the desktop
    site, since the /app/ views are laid out for phone-width screens.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.method == "GET"
            and request.path in DESKTOP_TO_APP
            and request.COOKIES.get("site_view") != "desktop"
            and MOBILE_UA_RE.search(request.META.get("HTTP_USER_AGENT", ""))
        ):
            target = DESKTOP_TO_APP[request.path]
            if request.META.get("QUERY_STRING"):
                target = f"{target}?{request.META['QUERY_STRING']}"
            return redirect(target)

        return self.get_response(request)
