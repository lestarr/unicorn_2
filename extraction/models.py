from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, field_validator
import re

class ContactData(BaseModel):
    linkedin: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None
    email: Optional[EmailStr] = None

class Restriction(BaseModel):
    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None

    def is_empty(self) -> bool:
        return not self.include and not self.exclude

    # @field_validator('include', 'exclude')
    # def check_validity(cls, value):
    #     # Mock validation logic, replace with a call to an LLM or a database
    #     if not value:
    #         return value
    #     # Example validation: ensure the value is not an empty string and contains only letters
    #     if not re.match(r'^[A-Za-z\s]+$', value):
    #         raise ValueError(f"{value} is not a valid entry")
    #     return value

class StartupInfo(BaseModel):
    name: str
    focus_industries: Optional[List[str]] = None
    location: Optional[str]
    business_model: Optional[str]
    website: HttpUrl
    founder: Optional[str]


class TeamMember(BaseModel):
    name: str
    contact_data: ContactData

class TeamInfo(BaseModel):
    members: List[TeamMember]

class InvestorsPitchRequirements(BaseModel):
    requirements: List[str]

class LinkInfo(BaseModel):
    team: Optional[HttpUrl] = None
    portfolio: Optional[HttpUrl] = None
    contacts: Optional[HttpUrl] = None

class InvestorInfo(BaseModel):
    name: str
    contact_data: ContactData
    locations: List[str]
    industries: List[str]
    geographies: List[str]
    investment_stages: List[str]
    check_sizes: str
    revenue_requirements: str
    specialised_funds: Optional[List[str]]
    investment_restrictions: Optional[List[Restriction]] = None
    portfolio: Optional[List[StartupInfo]] = None
    #team: Optional[TeamInfo] = None
    pitch_requirements: Optional[InvestorsPitchRequirements] = None
    links: Optional[LinkInfo] = None



class GeographyRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_geo(cls, value):
        # Replace this with a call to an LLM or geographical database
        valid_geos = ["New York", "California", "Europe", "Asia"]  # Example list
        # if value not in valid_geos:
        #     raise ValueError(f"{value} is not a recognized geographical location")
        return value

class BusinessModelRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_business_model(cls, value):
        # Replace this with a call to an LLM or business model database
        valid_models = ["B2B", "B2C", "SaaS", "Marketplace"]  # Example list
        # if value not in valid_models:
        #     raise ValueError(f"{value} is not a recognized business model")
        return value

class FounderNationalityRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_nationality(cls, value):
        # Replace this with a call to an LLM or nationality database
        valid_nationalities = ["American", "German", "Indian", "Chinese"]  # Example list
        # if value not in valid_nationalities:
        #     raise ValueError(f"{value} is not a recognized nationality")
        return value

class FounderEducationRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_education(cls, value):
        # Replace this with a call to an LLM or education database
        valid_alumni = ["Harvard", "MIT", "Stanford", "Oxford"]  # Example list
        # if value not in valid_alumni:
        #     raise ValueError(f"{value} is not a recognized education institution")
        return value

class FounderMinoritiesRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_minority(cls, value):
        # Replace this with a call to an LLM or minority group database
        valid_minorities = ["Hispanic", "African American", "LGBTQ+", "Women"]  # Example list
        # if value not in valid_minorities:
        #     raise ValueError(f"{value} is not a recognized minority group")
        return value

class LegalEntityRestriction(Restriction):
    @field_validator('include', 'exclude')
    def validate_legal_entity(cls, value):
        # Replace this with a call to an LLM or legal entity database
        valid_entities = ["LLC", "Corporation", "Sole Proprietorship"]  # Example list
        # if value not in valid_entities:
        #     raise ValueError(f"{value} is not a recognized legal entity")
        return value

