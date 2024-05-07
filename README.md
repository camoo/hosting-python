# hosting-python
SDK for python

# Usage example
```python

if __name__ == "__main__":
access_token = "your_access_token_here"  # Assume you have a valid access token
domain_manager = Domain(access_token)

    try:
        # Register a domain
        registration_result = domain_manager.register_domain(
            "example.cm", "1", "ns1.yourCompany.com,ns2.yourCompany.com",
            1112, 1223, 1223, 1223
        )
        print(registration_result)
    except Exception as e:
        print(str(e))

```
