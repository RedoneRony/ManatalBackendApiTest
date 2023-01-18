Database Design:

![Manatal Django Test](https://user-images.githubusercontent.com/39440576/213274805-a5234788-d8a4-4528-ac91-44f7194d1899.jpg)

Here Basically i covered two crud operations. 
1. school
2. student


Also i implement nested routers, search and filter query params.


So anyone can easily search someting based on my implemented fields.


- Endpoint `students/` will return all students (GET) and allow student creation (POST)
- Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
- Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)

- Endpoint /schools/:id/students will return students who belong to school :id (GET)
- Endpoint /schools/:id/students will allow student creation in the school :id (POST)
- nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id


Time BreakDown:

1. For creating basic boilerplate, database design, requirements specifications and corners case cheking. (1 hour)

2. Write database model,serializations and complete crud operations of individual table. overall(2 hours)

3. Logical case handling, errors handling and model viewset implementation because initially i was implemented api using api view decorator then shift to model viewset for nested routing. (2 hours)

4. Nested routing implementation,checking all cases and modify create function in serializer file, add requirements.txt file and adding search, filter quey in query params. (2.5 hours)

