import requests

def fetch_photo(query):
    api_key = "gEVf4hzi25I3j8wQP5guxJgR5HazDOMzzV4mDRvao1jMmba1ZE1PifFE"
    url = "https://api.pexels.com/v1/search"
    
    headers = {
        "authorization": api_key
    }
    
    params = {
        'query': query,
        'per_page': 1
    }
    
    response = requests.get(url, headers = headers, params = params)
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            src_original_url = photos[0]['src']['original']
            return src_original_url
        else:
            print("no photo found")
    else:
        print("error")
        
    return None
    
query = "Circular economy"

src_original_url = fetch_photo(query)

if src_original_url:
    print(f"original url for query {query} {src_original_url}")
    
# def create_word_docx(user_input, paragraph, image_input):
#     doc = Document()
#     doc.add_heading(user_input, level =1)
#     doc.add_paragraph(paragraph)
    
#     doc.add_heading('Image', level = 1)
#     image_stream = io.BytesIO()
#     image_input.save(image_stream, format = 'PNG')
#     image_input.seek(0)
#     doc.add_picture(image_stream, width = Inches(4))
#     return doc

# st.set_page_config(layout = "wide")

# def main():
#     pass

# if __name__ == "__main__":
#     main()