ilename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     78.9 MiB     78.9 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     82.7 MiB      3.8 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     83.5 MiB      0.8 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     83.5 MiB      0.1 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     86.5 MiB     86.5 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     90.0 MiB      3.5 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     90.0 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     90.1 MiB      0.1 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     87.2 MiB     87.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     90.6 MiB      3.4 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     90.6 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     90.8 MiB      0.2 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     88.7 MiB     88.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     89.9 MiB      1.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     89.9 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     89.9 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
INFO:     127.0.0.1:65448 - "GET /perform-background-task HTTP/1.1" 200 OK
    32     90.2 MiB     90.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     90.0 MiB     -0.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     90.0 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     90.0 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     90.5 MiB     90.5 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     90.1 MiB     -0.3 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     90.1 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     90.4 MiB      0.2 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     91.6 MiB     91.6 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     88.8 MiB     -2.8 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     88.9 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     88.9 MiB      0.1 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     90.0 MiB     90.0 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     91.1 MiB      1.1 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     91.1 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     91.1 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     88.6 MiB     88.6 MiB           1   @profile
    32     90.4 MiB     90.4 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     91.1 MiB      2.6 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     91.1 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     91.2 MiB      0.0 MiB           1       return df.to_dict(orient="records")


    34     91.1 MiB      0.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     91.1 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     91.2 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     89.9 MiB     89.9 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     93.0 MiB      3.1 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     94.6 MiB      1.7 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     94.6 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

    32     89.1 MiB     89.1 MiB           1   @profile
Line #    Mem usage    Increment  Occurrences   Line Contents
    33                                         def read_excel_sheet(filepath, sheet_name):
=============================================================
    34     94.6 MiB      5.6 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    32     90.0 MiB     90.0 MiB           1   @profile
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35                                             # df = df.fillna(0)
    33                                         def read_excel_sheet(filepath, sheet_name):
    36                                             # create_studies_mappings(df=df)
    32     90.2 MiB     90.2 MiB           1   @profile
    34     94.7 MiB      4.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    33                                         def read_excel_sheet(filepath, sheet_name):
    36                                             # create_studies_mappings(df=df)
    34     94.7 MiB      4.5 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    37     94.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    35                                             # df = df.fillna(0)
    38     94.7 MiB      0.0 MiB           1       return df.to_dict(orient="records")
    36                                             # create_studies_mappings(df=df)


    37     94.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    37     94.6 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     94.7 MiB      0.0 MiB           1       return df.to_dict(orient="records")


    38     94.7 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     89.2 MiB     89.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     94.6 MiB      5.4 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     94.6 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     94.6 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     94.7 MiB     94.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     94.7 MiB      0.0 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     94.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     94.7 MiB      0.0 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     83.7 MiB     83.7 MiB           1   @profile
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     69.0 MiB    -14.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
    35                                             # df = df.fillna(0)
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
    36                                             # create_studies_mappings(df=df)
    37     70.7 MiB      1.7 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     71.0 MiB      0.2 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
    32     66.2 MiB     66.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     96.9 MiB     30.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     96.9 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     97.0 MiB      0.1 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     66.2 MiB     66.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     97.0 MiB     30.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     97.0 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     97.1 MiB      0.1 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     71.6 MiB     71.6 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     97.2 MiB     25.6 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     97.2 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     97.2 MiB      0.0 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65453 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     95.7 MiB     95.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     98.6 MiB      2.9 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     98.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     98.7 MiB      0.1 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     96.7 MiB     96.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    100.8 MiB      4.1 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    100.8 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    100.8 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     97.2 MiB     97.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    100.6 MiB      3.4 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    100.6 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    100.6 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     96.9 MiB     96.9 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    100.6 MiB      3.7 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    100.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    100.6 MiB     -0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     96.5 MiB     96.5 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    100.6 MiB      4.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    100.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    100.7 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     97.4 MiB     97.4 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    100.8 MiB      3.4 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    100.8 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    100.8 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    100.6 MiB    100.6 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     99.6 MiB     -1.0 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     99.6 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     99.6 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    100.8 MiB    100.8 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     99.7 MiB     -1.1 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     99.7 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     99.6 MiB     -0.1 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    100.8 MiB    100.8 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    101.0 MiB      0.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
    35                                             # df = df.fillna(0)
=============================================================
    36                                             # create_studies_mappings(df=df)
    32    100.6 MiB    100.6 MiB           1   @profile
    37    101.0 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    33                                         def read_excel_sheet(filepath, sheet_name):
    38    101.0 MiB      0.0 MiB           1       return df.to_dict(orient="records")


    34    101.0 MiB      0.4 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    101.0 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    101.0 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    100.7 MiB    100.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    101.2 MiB      0.5 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    101.2 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    101.2 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     99.7 MiB     99.7 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    104.2 MiB      4.5 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    104.2 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    104.2 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    101.9 MiB    101.9 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    105.5 MiB      3.6 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    105.5 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    105.5 MiB      0.0 MiB           1       return df.to_dict(orient="records")


INFO:     127.0.0.1:65520 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65520 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65520 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65520 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65526 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65526 - "GET /perform-background-task HTTP/1.1" 200 OK
INFO:     127.0.0.1:65526 - "GET /perform-background-task HTTP/1.1" 200 OK
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    112.8 MiB    112.8 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34     74.2 MiB    -38.6 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37     76.4 MiB      2.3 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38     78.1 MiB      1.6 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    113.8 MiB    113.8 MiB           1   @profile
    32     66.4 MiB     66.4 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    115.5 MiB     49.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    34    114.9 MiB      1.1 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    36                                             # create_studies_mappings(df=df)
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37    114.9 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    37    115.5 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    115.0 MiB      0.0 MiB           1       return df.to_dict(orient="records")
    38    115.6 MiB      0.0 MiB           1       return df.to_dict(orient="records")




    32     66.0 MiB     66.0 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    116.3 MiB     50.3 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    116.4 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    116.4 MiB      0.0 MiB           1       return df.to_dict(orient="records")


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     76.8 MiB     76.8 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    117.1 MiB     40.2 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    117.1 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38    117.1 MiB      0.0 MiB           1       return df.to_dict(orient="records")


    32    115.5 MiB    115.5 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    116.9 MiB      1.3 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    116.9 MiB      0.1 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    117.3 MiB      0.4 MiB           1       return df.to_dict(orient="records")


Filename: /Users/nitmurth/Documents/DCE/fastapi-memoryleak/fastapi_memoryleak/main3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32    114.2 MiB    114.2 MiB           1   @profile
    33                                         def read_excel_sheet(filepath, sheet_name):
    34    117.7 MiB      3.5 MiB           1       df = pd.read_excel(filepath, sheet_name=sheet_name)
    35                                             # df = df.fillna(0)
    36                                             # create_studies_mappings(df=df)
    37    117.8 MiB      0.0 MiB           1       memory_usage = df.memory_usage(deep=True).sum()
    38    117.8 MiB      0.0 MiB           1       return df.to_dict(orient="records")