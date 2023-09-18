import json
import os
import pandas as pd

env_dict = {'PROJECT_HOME_DIR': "D:\\Learning\\PythonLearning\\learnWebDevelopment\\displayData"}


def get_data(input_file_name):
    try:
        input_data = os.path.join(env_dict['PROJECT_HOME_DIR'], 'data_source', input_file_name)
        print(input_data)
        df = pd.read_csv(input_data)
        json_records = df.reset_index().to_json(orient='records')
        data = json.loads(json_records)
        print(data)
        return data
    except Exception as e:
        print(e)
