# DomainModel

## Properties

| Name                                  | Type           | Description                                                                                  | Notes |
|---------------------------------------|----------------|----------------------------------------------------------------------------------------------|-------|
| **id**                                | `int`          | Unique identifier for the domain.                                                            |       |
| **domain_name**                       | `string`       | The registered domain name.                                                                  |       |
| **years**                             | `int`          | The number of years the domain is registered for.                                            |       |
| **reg_contact_id**                    | `int`          | ID of the registrant contact.                                                                |       |
| **admin_contact_id**                  | `int`          | ID of the administrative contact.                                                            |       |
| **tech_contact_id**                   | `int`          | ID of the technical contact.                                                                 |       |
| **billing_contact_id**                | `int`          | ID of the billing contact.                                                                   |       |
| **whois_privacy_protection**          | `bool`         | Indicates whether WHOIS privacy protection is activated.                                     |       |
| **hidden**                            | `bool`         | Indicates if the domain is hidden pending confirmation.                                      |       |
| **extern**                            | `bool`         | Indicates if the domain is managed externally.                                               |       |
| **attr_name**                         | `string?`      | Optional custom attribute name associated with the domain.                                   |       |
| **attr_value**                        | `string?`      | Value for the optional custom attribute associated with the domain.                          |       |
| **exp_date**                          | `int`          | UNIX timestamp of the domain's expiration date.                                              |       |
| **is_included**                       | `bool`         | Indicates whether the domain is included in any service packages.                            |       |
| **catchall_email**                    | `string`       | Email address configured as the catch-all for the domain.                                    |       |
| **alias**                             | `string`       | Alias of the domain, if any.                                                                 |       |
| **reseller_customer_id**              | `int`          | Reseller customer ID associated with the domain.                                             |       |
| **auto_renew**                        | `bool`         | Indicates whether the domain is set to renew automatically.                                  |       |
| **deletion_date**                     | `int`          | UNIX timestamp of when the domain is scheduled for deletion.                                 |       |
| **pending_delete_restorable_endtime** | `int`          | UNIX timestamp until which the domain can be restored post-expiration before final deletion. |       |
| **theft_protection**                  | `bool`         | Indicates whether theft protection is enabled for the domain.                                |       |
| **suspended**                         | `bool`         | Indicates whether the domain is currently suspended.                                         |       |
| **with_api_created**                  | `bool`         | Indicates if the domain was created through an API request.                                  |       |
| **confirmed_date**                    | `datetime`     | The date when the domain was last confirmed.                                                 |       |
| **autossl_onsubdomain**               | `bool`         | Indicates whether automatic SSL is enabled for subdomains of this domain.                    |       |
| **premium_dns**                       | `bool`         | Indicates if premium DNS services are active for the domain.                                 |       |
| **updated_at**                        | `datetime`     | The last date and time when the domain details were updated.                                 |       |
| **registrar_name**                    | `string`       | The name of the registrar if the domain is registered externally.                            |       |
| **management_suspended**              | `bool`         | Indicates whether management of the domain via dashboard or API is suspended.                |       |
| **clf_proxied**                       | `bool`         | Indicates if DNS entries for the domain are automatically proxied by Cloudflare.             |       |
| **created_at**                        | `datetime`     | The date and time when the domain was originally created.                                    |       |
| **nameservers**                       | `List[string]` | List of nameservers assigned to the domain.                                                  |       |

### Notes:

- `string?` denotes optional string fields which can be null.
- `datetime` fields are represented in ISO 8601 format.
- Fields like `whois_privacy_protection`, `hidden`, and others are boolean, indicating a `True` or `False` value.

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
