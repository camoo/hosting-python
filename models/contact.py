from pydantic import BaseModel, EmailStr, constr, Field, validator

class ContactModel(BaseModel):
    name: constr(strip_whitespace=True, max_length=255)
    company: str
    email: EmailStr
    address_1: str = Field(..., alias="address-1")
    city: str
    ccode: constr(regex=r'^[A-Z]{2}$')
    zipcode: str
    phone_cc: constr(regex=r'^\d{1,3}$') = Field(..., alias="phone-cc")
    phone: constr(regex=r'^\d{4,12}$')
    state: str
    address_2: str = Field(None, alias="address-2")
    address_3: str = Field(None, alias="address-3")
    fax_cc: int = Field(None, alias="fax-cc")
    fax: int = Field(None, alias="fax")
    customer_id: int = Field(None, alias="customer-id")

    @validator('company')
    def validate_company(cls, v):
        if v not in ["N/A", "NA"] and not v.strip():
            raise ValueError("Invalid company name")
        return v

    class Config:
        allow_population_by_field_name = True
