import importlib


def import_provider_tasks(provider_type):
    """Return the module for a provider.

    :param string provider_type: type of cloud provider **currently only "ec2"**
    :rtype: celery module for the provider
    :raises: :py:class:`ImportError` if the provider isn't recognized
    """
    try:
        tasks = importlib.import_module('provider.' + provider_type)
    except ImportError as e:
        raise e
    return tasks
