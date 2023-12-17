from functools import wraps

from django.shortcuts import render


def authentication():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated or not request.user.is_superuser:
                data = {
                    'message': 'Unauthorized',
                    'code': 403
                }
                return render(request, 'error.html', status=403, context=data)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator