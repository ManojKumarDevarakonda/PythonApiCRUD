from sanic import Sanic
from sanic.response import json,  text
from database import db, Base, engine
from models import Uploads
from sqlalchemy.orm import Session



app = Sanic("__name__")

Base.metadata.create_all(engine)
@app.route("/admin-uploads",methods=['POST'])
async def postingdata(request):
    UploadId = request.json.get('UploadId')
    UserId =request.json.get('UserId')
    Title = request.json.get('Title')
    Body = request.json.get('Body')
    Timestamp = request.json.get('Timestamp')
    user = Uploads(Title = Title, UploadId = UploadId, UserId = UserId, Body = Body, Timestamp = Timestamp)
    db.add(user)
    db.commit()
    return json({'message': 'Record inserted successfully'}) 

@app.route('/admin-get',methods=['GET'])
async def getdata(request):
    try : 
        users = db.query(Uploads).all()
        userList = [user.__dict__ for user in users]
        for user_data in userList :
            user_data.pop('_sa_instance_state',None)
            return json (userList)
    except Exception as e:
        return json({'error' : 'Internal server error'},status=500)
   
@app.route('/admin-update',methods=['PUT'])
async def updatedata(request):
    db.query(Uploads).filter(Uploads.UploadId == 1 ).update({"Title" : "ManojDevarakonda"})
    db.commit()
    return json({"message" : "Record Updated Successfully!!"})
@app.route('/admin-delete',methods=['DELETE'])
async def deletedata(request) : 
    db.query(Uploads).filter(Uploads.UserId == 1).delete()
    return json({"message":"Record Deleted Successfully!!"})

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8000)