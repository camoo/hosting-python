from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class DomainModel(BaseModel):
    id: int
    domain_name: str = Field(..., alias='domain-name')
    years: int
    reg_contact_id: int = Field(..., alias='reg-contact-id')
    admin_contact_id: int = Field(..., alias='admin-contact-id')
    tech_contact_id: int = Field(..., alias='tech-contact-id')
    billing_contact_id: int = Field(..., alias='billing-contact-id')
    whois_privacy_protection: bool = Field(..., alias='whois_privacy_protection')
    hidden: bool
    extern: bool
    attr_name: Optional[str] = Field(None, alias='attr-name')
    attr_value: Optional[str] = Field(None, alias='attr-value')
    exp_date: int = Field(..., alias='exp-date')
    is_included: bool
    catchall_email: Optional[str]
    alias: Optional[str]
    reseller_customer_id: int
    auto_renew: bool
    deletion_date: int
    pending_delete_restorable_endtime: int = Field(..., alias='pending_delete_restorable_endtime')
    theft_protection: bool
    suspended: bool
    with_api_created: bool
    confirmed_date: datetime
    autossl_onsubdomain: bool
    premium_dns: bool
    updated_at: datetime
    registrar_name: Optional[str]
    management_suspended: bool
    clf_proxied: bool
    created_at: datetime
    nameservers: List[str] = Field(..., alias='ns')

    class Config:
        allow_population_by_field_name = True
