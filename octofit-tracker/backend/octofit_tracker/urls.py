from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import os


def api_root_override(request):
    """Return API endpoints anchored to Codespace URL when available."""
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f'https://{codespace}-8000.app.github.dev/api'
    else:
        # fallback to request host
        scheme = 'https' if request.is_secure() else 'http'
        base = f"{scheme}://{request.get_host()}/api"

    return JsonResponse({
        'users': f"{base}/users/",
        'activities': f"{base}/activities/",
        'teams': f"{base}/teams/",
        'workouts': f"{base}/workouts/",
        'leaderboard': f"{base}/leaderboard/",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_override),
    path('api/', include('octofit_app.urls')),
]
