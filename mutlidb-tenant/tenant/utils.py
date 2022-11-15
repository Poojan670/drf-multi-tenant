def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)


def get_tenants_map():

    """
    Configure according to your database and hosts
    """
    return {
        "test.checkhost.local": "test_db",
        "development.checkhost.local": "development_db"
    }
