from codecs import backslashreplace_errors
from distutils.util import rfc822_escape
import json
import requests
import base64
from io import StringIO
import pandas as pd

class Read_file_from_github:
    """
    https://docs.python.org/3/library/io.html#io.StringIO
    """

    def __init__(self) -> None:
        pass

    def get_content_of_file_from_github(self):
        """
        get_content_of_file_from_github
        """

        # Target file url
        url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/data/utility_costs.csv"
        req = requests.get(url)

        # Request status code
        req_stat_code = req.status_code
        print("\n"*1 + "="*30)
        print("Request status code : ", req_stat_code)

        # 
        if req_stat_code == 200: # requests.codes.ok:
            # The response is a JSON
            # Get dict from response
            req_dict = req.json()

            # req is now a dict with keys: name, encoding, url, size ... and content.
            print("\n"*3 + "="*30)
            print("req_dict type : ", type(req_dict))
            print("req_dict : ", req_dict)

            # Get content form req_dict that is encoded with base64.
            try:
                # https://stackoverflow.com/a/57645516
                content_encoded_with_base64 = base64.b64decode(req_dict['content'])

                # decode with utf-8
                content_decoded_with_utf8 = content_encoded_with_base64.decode('utf-8')
            except Exception as e:
                print("\n"*3, e)

            return content_decoded_with_utf8

        else:
            print("\n"*3 + "="*30)
            print("\n"*1, 'Content was not found.')

    def create_pandas_df_from_memory_text_buffer(self, targetString):
        """
        create_pandas_df_from_memory_text_buffer
        """

        # Get [ text stream ] using [ an in-memory text buffer ] from [ str ]
        # https://stackoverflow.com/a/57645516
        # https://docs.python.org/3/library/io.html#io.StringIO
        text_stream = StringIO(str(targetString))
        print("\n"*3 + "="*30)
        print("text_stream type : ", type(text_stream))
        print("text_stream : ", text_stream)

        # Create Pandas DataFrame from text stream
        df = pd.read_csv(text_stream, sep=",")
        print("\n"*3 + "="*30)
        print(df)
    
def main():
    rffg = Read_file_from_github()
    content_decoded_with_utf8 = rffg.get_content_of_file_from_github()
    rffg.create_pandas_df_from_memory_text_buffer(content_decoded_with_utf8)

if __name__ == "__main__":
    main()