## my  crud app

# use  uv  to install the  dependaciers and  run it  
`uv  add`
`uv  run main.py`


* curl cmd *
```bash curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
HTTP/1.1 200 OK
date: Wed, 09 Sep 2026 20:12:48 GMT
server: uvicorn
content-length: 46
content-type: application/json

[{"id":4,"title":"Buy milk","done":false},201]`


![alt text](image.png)
![alt text](image-1.png)