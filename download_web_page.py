import requests

url = "https://www.libertymutual.com/"

response = requests.get(url)

if response.status_code == requests.codes.OK:
    for header, value in response.headers.items():
        print(header, value)
    print('-' * 60)
    raw_response_data = response.content
    response_data = raw_response_data.decode()
    print(response_data[:1000])
else:
    print("GET failed -- status code:", response.status_code)

pdf_url = "https://public.libertymutual-cdn.com/lm-media-assets/documents/claims/claims-photo-guide.pdf"

response = requests.get(pdf_url)
if response.status_code == requests.codes.OK:
    with open('liberty_claim_guide.pdf', 'wb') as liberty_out:
        liberty_out.write(response.content)
else:
    print("Uh-oh:", requests.status_code)
