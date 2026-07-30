from fastapi import FastAPI

app=FastAPI(title="Course Manageent System")

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/contact")
def contact():
    return {"Hello": "Contact"}

l=[]

#get-----read
@app.get("/courses")
def available_courses():
    return {"message":"The following are the courses available","courses":l}

#post----create/write
@app.post("/add_course/{course_name}")
def add_course(course_name:str):
    l.append(course_name)
    return {"message":f"Course added successfully: {course_name}"}

#put----update
@app.put("/update_course/{old_course_name}/{new_course_name}")
def update_course(old_course_name:str,new_course_name:str):
    if old_course_name in l:
        index=l.index(old_course_name)
        l[index]=new_course_name
        return {"message":f"Course updated successfully: {old_course_name} to {new_course_name}"}
    else:
        return {"message":f"Course not found: {old_course_name}"}

#delete----remove
@app.delete("/delete_course/{course_name}")
def delete_course(course_name:str):
    if course_name in l:
        l.remove(course_name)
        return {"message":f"Course deleted successfully: {course_name}"}
    else:
        return {"message":f"Course not found: {course_name}"}


@app.delete("/delete_all_courses/{course_name}")
def delete_all_courses(course_name:str):
    if course_name in l:
        l.clear()
        return {"message":f"All courses are Removed Successfully"}
    else:
        return {"message":f"Courses Not Found:{course_name}","courses":l}