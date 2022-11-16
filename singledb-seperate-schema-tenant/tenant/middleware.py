from .utils import set_tenant_schema_for_request


class TenantMiddleware:
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        set_tenant_schema_for_request(request)
        response = self.response(request)
        return response
