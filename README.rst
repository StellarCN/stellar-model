=============
stellar-model
=============
.. image:: https://img.shields.io/github/workflow/status/StellarCN/stellar-model/GitHub%20Action/main?style=flat&maxAge=1800
    :alt: GitHub Action
    :target: https://github.com/StellarCN/stellar-model/actions

.. image:: https://img.shields.io/readthedocs/stellar-model.svg?style=flat&maxAge=1800
    :alt: Read the Docs
    :target: https://stellar-model.readthedocs.io/en/latest/

.. image:: https://img.shields.io/pypi/v/stellar-model.svg?style=flat&maxAge=1800
    :alt: PyPI
    :target: https://pypi.python.org/pypi/stellar-model

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue?style=flat
    :alt: Python - Version
    :target: https://pypi.python.org/pypi/stellar-model

`stellar-model`_ is based on `pydantic`_, you can use it to parse the JSON
returned by `Stellar Horizon`_ into Python models, through it, you can get a better
development experience in the editor with things like code completion, type hints, and more.

Installing
==========

You need to choose a suitable stellar-model version according to the Horizon version number you are using.
Please check the list `here <https://github.com/StellarCN/stellar-model/issues/20/>`_.

.. code-block:: text

    pip install stellar-model==0.4.0b0

Example
=======
.. code-block:: python

    import requests
    from stellar_model import AccountResponse

    url = "https://horizon.stellar.org/accounts/GALAXYVOIDAOPZTDLHILAJQKCVVFMD4IKLXLSZV5YHO7VY74IWZILUTO"
    raw_resp = requests.get(url).json()
    parsed_resp = AccountResponse.parse_obj(raw_resp)
    print(f"Account Sequence: {parsed_resp.sequence}")


Of course you can use it with `stellar-sdk`_.

.. code-block:: python

    from stellar_sdk import Server
    from stellar_model import AccountResponse

    server = Server("https://horizon.stellar.org")
    account_id = "GALAXYVOIDAOPZTDLHILAJQKCVVFMD4IKLXLSZV5YHO7VY74IWZILUTO"
    raw_resp = server.accounts().account_id(account_id).call()
    parsed_resp = AccountResponse.parse_obj(raw_resp)
    print(f"Account Sequence: {parsed_resp.sequence}")


Documentation
=============
stellar-model's documentation can be found at https://stellar-model.readthedocs.io


.. _stellar-model: https://github.com/StellarCN/stellar-model
.. _pydantic: https://pydantic-docs.helpmanual.io/
.. _Stellar Horizon: https://developers.stellar.org/api/resources/
.. _stellar-sdk: https://github.com/StellarCN/py-stellar-base
