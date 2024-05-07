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


# Create Contact

```python
if __name__ == "__main__":
    access_token = "your_access_token_here"
    contact_manager = ContactManager(access_token)
    
    contact_data = {
        "name": "John Doe",
        "company": "Doe Ltd.",
        "email": "new-contact@domain.cm",
        "address_1": "Bastos",
        "city": "Yaounde",
        "ccode": "CM",
        "zipcode": "0000",
        "phone_cc": "237",
        "phone": "612345689",
        "state": "Centre"
    }

    try:
        result = contact_manager.add_contact(contact_data)
        if result:
            print(result)
    except Exception as e:
        print(str(e))
```
