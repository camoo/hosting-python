# Domain API Endpoints

All URIs are relative to `/v1`.

| Method                                                  | HTTP request                           | Description                                              |
|---------------------------------------------------------|----------------------------------------|----------------------------------------------------------|
| [**check_domain_availability**](Domain.md#availability) | **POST** `/domains/availability`       | Checks the availability of the specified domain name(s). |
| [**register_domain**](Domain.md#register)               | **POST** `/domains/register`           | Registers a new domain name with specified details.      |
| [**modify_nameservers**](Domain.md#modify-nameservers)  | **POST** `/domains/modify-nameservers` | Modifies the nameservers for a specified domain.         |
| [**get_domain_details**](Domain.md#details)             | **GET** `/domains/details`             | Retrieves detailed information about a specified domain. |


## `availability`
> from domain import Domain

This method checks the availability of a specified domain name across multiple top-level domains (TLDs).
It requires authentication and uses an access token to query the domain registration service.

### Example Usage
```python
from access_token import AccessToken
from domain import Domain

if __name__ == "__main__":
    email = "your@email.com"
    password = "TopSecret"
    token_manager = AccessToken(email, password)

    try:
        # Authenticate and get the token
        token = token_manager.authenticate()

        # Create an instance of Domain with the fetched token
        domain_manager = Domain(token)

        # Now, check domain availability
        result = domain_manager.check_domain_availability("example", "cm,net.cm")
        print(result)
    except Exception as e:
        print(str(e))

```

### Parameters

| Name       | Type       | Description                                | Notes                          |
|------------|------------|--------------------------------------------|--------------------------------|
| **domain** | **string** | The base name of the domain to be checked. | Required. Example: "example"   |
| **tlds**   | **string** | Comma-separated list of TLDs to check.     | Required. Example: "cm,net.cm" |

### Return type

Returns: An object that typically includes the availability status of the domain for each TLD specified.

# Notes
* The availability check requires that both the domain base name and at least one TLD be specified.
* Ensure that your credentials for authentication are correct to avoid unauthorized access errors.
* Handle exceptions to manage potential errors such as network issues or incorrect input formats effectively.

## `register`
> from domain import Domain

Register a new domain name based on the specified parameters.
This process involves setting nameservers and specifying registrant,
admin, billing, and technical contacts for the domain.

### Example Usage
```python
from access_token import AccessToken
from domain import Domain

if __name__ == "__main__":
    email = "your@email.com"
    password = "TopSecret"
    token_manager = AccessToken(email, password)

    try:
        # Authenticate and get the token
        token = token_manager.authenticate()

        # Create an instance of Domain with the fetched token
        domain_manager = Domain(token)

        # Now, register domain
        registration_result = domain_manager.register_domain(
            "example.cm", "1", "ns1.yourCompany.com,ns2.yourCompany.com",
            1112, 1223, 1223, 1223
        )
        print(registration_result)
    except Exception as e:
        print(str(e))

```

### Parameters

Detailed descriptions of the parameters required to register a domain:

| Name                   | Type     | Description                                           | Notes                                                        |
|------------------------|----------|-------------------------------------------------------|--------------------------------------------------------------|
| **domain_name**        | `string` | The full domain name to be registered.                | Required. Example: "example.cm"                              |
| **years**              | `int`    | The number of years for which to register the domain. | Required. Ensure account balance is sufficient for the term. |
| **ns**                 | `string` | Comma-separated list of nameservers for the domain.   | Required. At least two nameservers must be specified.        |
| **reg-contact-id**     | `int`    | ID of the registrant contact.                         | Required. Must correspond to a valid contact ID.             |
| **admin-contact-id**   | `int`    | ID of the administrative contact.                     | Required.                                                    |
| **tech-contact-id**    | `int`    | ID of the technical contact.                          | Required.                                                    |
| **billing-contact-id** | `int`    | ID of the billing contact.                            | Required.                                                    |

                                                       |
### Return type

Returns: An object that typically includes the registration status,
transaction details, and an identifier for the newly registered domain.


# Notes
* Ensure proper error handling is in place to manage potential failures during the registration process, such as invalid contact IDs or insufficient funds.
* Validate all inputs to confirm that they meet the API requirements and domain registration policies.


## `details`
> from domain import Domain

Check the availability of the specified domain name(s).

### Example Usage
```python
from access_token import AccessToken
from domain import Domain

if __name__ == "__main__":
    email = "your@email.com"
    password = "TopSecret"
    token_manager = AccessToken(email, password)

    try:
        # Authenticate and get the token
        token = token_manager.authenticate()

        # Create an instance of Domain with the fetched token
        domain_manager = Domain(token)

        # Now, fetch domain details
        details = domain_manager.get_domain_details(1902021)
        print(details)
    except Exception as e:
        print(str(e))

```

### Parameters

| Name   | Type  | Description                                  | Notes     |
|--------|-------|----------------------------------------------|-----------|
| **id** | `int` | Identifier of the domain registration order. | Required. |

### Return type

Returns an object instance.


## `modify-nameservers`
> from domain import Domain

This method modifies the nameservers associated with a specific domain registration order.
It requires authentication and uses an access token to perform this action on the API.

### Example Usage
```python
from access_token import AccessToken
from domain import Domain

if __name__ == "__main__":
    email = "your@email.com"
    password = "TopSecret"
    token_manager = AccessToken(email, password)

    try:
        # Authenticate and get the token
        token = token_manager.authenticate()

        # Create an instance of Domain with the fetched token
        domain_manager = Domain(token)

        # Now, modifiy nameservers
        domain_id = 123  # example domain ID
        result = domain_manager.modify_nameservers(domain_id, "ns1.yourCompany.com,ns2.yourCompany.com")
        print("Modification successful:", result)
    except Exception as e:
        print(str(e))

```

### Parameters

| Name   | Type     | Description                                  | Notes                                                 |
|--------|----------|----------------------------------------------|-------------------------------------------------------|
| **id** | `int`    | Identifier of the domain registration order. | Required.                                             |
| **ns** | `string` | Comma-separated list of new nameservers.     | Required. At least two nameservers must be specified. |


### Return type

Returns: An object instance containing the response from the server,
which usually includes a status message indicating whether the nameserver update was successful or not.
If successful, additional details about the update may also be included


### Authorization

All headers necessary for the API call are automatically managed by the SDK.


[[Back to top]](#domain-api-endpoints) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
