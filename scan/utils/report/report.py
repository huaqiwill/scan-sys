import pandas as pd
from pandas_profiling import ProfileReport
from pydantic import AnyUrl

assert str(AnyUrl(url='https://google.com')) == 'https://google.com/'
assert str(AnyUrl(url='https://google.com/')) == 'https://google.com/'
assert str(AnyUrl(url='https://google.com/api')) == 'https://google.com/api'
assert str(AnyUrl(url='https://google.com/api/')) == 'https://google.com/api/'
df = pd.read_csv(data_file_name)
report = ProfileReport(df)
report.to_file(output_file='output.html')
