import instructor
from openai import OpenAI
from models import InvestorInfo, TeamInfo, StartupInfo


# Initialize the OpenAI client

def extract_investor_info(messages, client: OpenAI):
    # Extract structured data from natural language
    investor_info = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=InvestorInfo,
        messages=messages,
        max_retries=2
    )

    # Filter out empty restrictions
    if investor_info.investment_restrictions:
        investor_info.investment_restrictions = [r for r in investor_info.investment_restrictions if not r.is_empty()]

    return investor_info

def extract_team_info(messages, client: OpenAI):
    
    # Extract structured data from natural language
    team_info = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=TeamInfo,
        messages=messages,
    )

    return team_info

def extract_startup_info(messages, client: OpenAI):
    
    # Extract structured data from natural language
    portfolio_info = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=StartupInfo,
        messages=messages,
    )

    return portfolio_info
