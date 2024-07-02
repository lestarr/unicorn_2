from extract import extract_investor_info

# Example messages for extracting investor information
messages_investor_info = [
    {"role": "user", "content": "Extract the investor information from the website: example.com"},
]

# Extract the data
investor_info = extract_investor_info(messages_investor_info)

# Print the extracted information
print(investor_info)
