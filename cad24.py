import cloudconvert

cloudconvert.configure(api_key='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2Y0NGVlMjY5YjYzMDA4YTM3NDgyY2NmNzYzYWMwMWE3MzQzNTY3NGVkYjgwZjdlMTk3YTc5MTg3ZmFjN2YyZTUwNjIzM2MwNDM0ZTU3OWYiLCJpYXQiOjE3MDM0ODY3NjcuMTY4MzgsIm5iZiI6MTcwMzQ4Njc2Ny4xNjgzODIsImV4cCI6NDg1OTE2MDM2Ny4xNjQ2OTgsInN1YiI6IjY2NjE3NDQ0Iiwic2NvcGVzIjpbInVzZXIucmVhZCIsInVzZXIud3JpdGUiLCJ0YXNrLnJlYWQiLCJ0YXNrLndyaXRlIiwid2ViaG9vay5yZWFkIiwid2ViaG9vay53cml0ZSIsInByZXNldC5yZWFkIiwicHJlc2V0LndyaXRlIl19.IMjUnIGz5Zqvn5gq2WIC2AQOEgkCNU79dJTmjoP8lr7pzYSu0nqcEAxNM64crya4qYOQQHIKrpCqAG4VzaMOaIDs9nxTPyQe0keXxVFjLKgBKMGFsKFmoEMOZamWVzTJiAWqmqVPqvMKZwffWKZwKwFQe5ep7i8dDBgp6i8h2BBIfpNOmDHap-te6FBw1WZ9q1mIjajxyQcylOx3OkLssdoP8AU1ll2wxElkwe_xHo6XMFnTKGTeMEJBYpxjLc1gVHBmgGbZtvbsmbkH9MUycQypsCdCcBUq-0WIC4-qsAswCQAP_DgxIcJDLhjMHi-EtB_SITV_6xd5JHxApnjNAWbQBV68ap_bPRZGAgGnc26x6U3itFolZ6RNzl4Bli82mXRj32ufcb8K__GI5kyj6NC-Llnm5h_iJCZ19nEUYEk4NyGbHUOeNKOqh-mJRhHvbHegG7QqR43WatDAYu5p5q_mhtC8K30OYjdIRu_abgpbO5FtHTxSWsu1lzfHqe7-TilVEiNm_FYWvQ3qJSJ-6fYGtqv51DxY1SSkzCa61lf4jb-IjCtsEE8tkgQdSpEqR0MPzf6tqJQRQa2hhf_otbEomiJbfGv2xcC16iMGTG2MkR9RGQ6L-5vR0dZlIHIL6cmFQBp6MTzrTAe8WHxcxdDCuuavfRZuRrCoGfQ1elI', sandbox=False)

cloudconvert.Job.create(payload={
    "tasks": {
        'import-my-file': {
            'operation': 'import/url',
            'url': 'https://my-url'
        },
        'convert-my-file': {
            'operation': 'convert',
            'input': 'import-my-file',
            'output_format': 'pdf',
            'some_other_option': 'value'
        },
        'export-my-file': {
            'operation': 'export/url',
            'input': 'convert-my-file'
        }
    }
})

# 开始转换
process = cloudconvert.convert({
    "inputformat": "dxf",
    "outputformat": "pdf",
    "input": "upload",
    "file": open('教堂.dxf', 'rb')
})

# 等待转换完成
process.wait()

# 下载转换后的文件
process.download('output24.pdf')