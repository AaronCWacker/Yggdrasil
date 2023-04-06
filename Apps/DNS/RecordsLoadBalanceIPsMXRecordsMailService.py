import streamlit as st
import requests
from dnspython import dns, resolver

# Function to resolve DNS
def resolve_dns(domain, record_type):
    try:
        answers = resolver.resolve(domain, record_type)
        return [str(answer) for answer in answers]
    except Exception as e:
        return [str(e)]

# Streamlit app
st.title('DNS Resolution & Management Tool')

domain = st.text_input('Enter the domain name:')
record_type = st.selectbox('Select the record type:', ('A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SRV'))

if st.button('Resolve DNS'):
    result = resolve_dns(domain, record_type)
    st.write(f'Results for {domain} ({record_type}):')
    st.write(result)

st.title('DNS Record Management')
api_key = st.text_input('Enter API key for DNS provider:')
domain_to_update = st.text_input('Enter the domain name to update:')

st.write('Enter the record data:')
record_name = st.text_input('Record name:')
record_type_to_update = st.selectbox('Record type:', ('A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SRV'))
record_content = st.text_input('Record content:')
record_ttl = st.number_input('TTL (in seconds):', min_value=300, max_value=86400)

update_button = st.button('Update DNS Record')

if update_button:
    # Replace the following line with the appropriate API call for the DNS provider you're using
    response = requests.post(f'https://api.example.com/v1/domains/{domain_to_update}/records', data={
        'api_key': api_key,
        'type': record_type_to_update,
        'name': record_name,
        'content': record_content,
        'ttl': record_ttl
    })

    if response.status_code == 200:
        st.success('DNS record updated successfully')
    else:
        st.error('Error updating DNS record')

