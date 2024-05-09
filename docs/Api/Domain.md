# Domain

All URIs are relative to `/v1`.

| Method                                                  | HTTP request                   | Description                                              |
|---------------------------------------------------------|--------------------------------|----------------------------------------------------------|
| [**check_domain_availability**](Domain.md#availability) | **POST** /domains/availability | Checks the availability of the specified domain name(s). |
| [**register_domain**](Domain.md#availability)           | **POST** /domains/register     | Registers a domain name.                                 |

## `availability`
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

        # Now, check domain availability
        result = domain_manager.check_domain_availability("example", "cm,net.cm")
        print(result)
    except Exception as e:
        print(str(e))

```

### Parameters

| Name       | Type       | Description            | Notes |
|------------|------------|------------------------|-------|
| **domain** | **string** | name without extension |       |
| **tlds**   | **string** | tlds comma separated   |       |

### Return type

Returns an object instance.



## `register`
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

| Name                   | Type       | Description                 | Notes                                                        |
|------------------------|------------|-----------------------------|--------------------------------------------------------------|
| **domain-name**        | **string** | name without extension      |                                                              |
| **years**              | **int**    | years for registration      | make sure your account has enough balance for that operation |
| **ns**                 | **string** | nameservers comma separated |                                                              |
| **reg-contact-id**     | **int**    | Registrant contact ID       |                                                              |
| **admin-contact-id**   | **int**    | Admin contact ID            |                                                              |
| **billing-contact-id** | **int**    | Billing contact ID          |                                                              |
| **tech-contact-id**    | **int**    | Technical contact ID        |                                                              |

### Return type

Returns an object instance.



### Authorization

All headers necessary for the API call are automatically managed by the SDK.


[[Back to top]](#Domain) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
