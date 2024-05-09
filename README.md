# hosting-python
SDK for python

# Docker Setup
To containerize the hosting-python API Client, use the following Dockerfile:

```bash
docker build -t hosting-python .

docker run -it hosting-python /bin/bash

# Within the docker 
# run
python main.py
```

# Usage example

Please visit https://api-doc.camoo.hosting/ for usage documentation


## Documentation for API Endpoints

All URIs are relative to */v1*

| Class    | Method                                                           | HTTP request                         | Description                                              |
|----------|------------------------------------------------------------------|--------------------------------------|----------------------------------------------------------|
| *Domain* | [**check_domain_availability**](docs/Api/Domain.md#availability) | **POST** /domains/availability       | Checks the availability of the specified domain name(s). |
| *Domain* | [**register_domain**](docs/Api/Domain.md#register)               | **POST** /domains/register           | Registers a domain name.                                 |
| *Domain* | [**modify_nameservers**](docs/Api/Domain.md#modify-nameservers)  | **POST** /domains/modify-nameservers | Modifies the nameservers for a specified domain.         |
| *Domain* | [**get_domain_details**](docs/Api/Domain.md#details)             | **GET** /domains/details             | Retrieves detailed information about a specified domain. |

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

## Documentation For Models
- [DomainModel](docs/models/DomainModel.md)
