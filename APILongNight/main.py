from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.recursos.usuarios import usuarios
from models.recursos.hosters import hosters
from models.recursos.login import login as log
from models.recover_request import recover_password_request
from models.reserva import reserva
import jwt 
import motor.motor_asyncio

#instancia de la app 
app = FastAPI(title="LongNight")

archivo = open('password/password.txt', 'r')
my_secret = archivo.read()

#coneccion a la base de datos
async def connection():
    cliente = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://yashidb:2508Yuudai@cluster0.5nak7wk.mongodb.net/?retryWrites=true&w=majority')
    db = cliente['longnightDB']
    return db

#funcion para verificar el toquen
async def verify_token(request: Request):
    #tomar el roquen de la cabecera del request
    token = request.headers["Authorization"]    
    data = jwt.decode(token, my_secret, algorithms=["HS256"]) #desencriptar el toquen y almacenarlo en una variable

    db = await connection() #instanciar la coneccion de la base de datos 

    usuarios = await db.usuarios.find().to_list(1000) #almacenar todos los utuaios en una lista 
    
    for user in usuarios:
        if user["nombre_usuario"] == data["nombre_usuario"]: #comparar cada usuario con el usuario del token generado
            return True #verdadero si coinciden
        
        return False #falso si no hay coincidencias

#main page of api
@app.get('/')
def main():
    return "pagina principal"
#sing up to users table of clients
@app.post('/singup/client')
async def singupclient(usuario: usuarios):
    try:
        db = await connection() #coneccion de la base de datos

        user_data = jsonable_encoder(usuario)

        await db.usuarios.insert_one(user_data) #insersion del usuario en la base de datos
        return JSONResponse(status_code=201, content={"Message": "Usuario registrado"}) #respuesta de que el usuario fue creado

    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"}) #exepcion del programa



#sig up to users table of hosters
@app.post('/singup/host')
async def singuphost(usuario: hosters):
    try:
        db = await connection()

        user_data = jsonable_encoder(usuario)

        await db.usuarios.insert_one(user_data)
        return JSONResponse(status_code=201, content={"Message": "Usuario registrado"})
        
    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})

#login route for al users
@app.post('/login')
async def login(user_log: log):
    try: 
        db = await connection()
        
        usuarios = await db.usuarios.find().to_list(1000)

        for usuario in usuarios:
            usuario["_id"] = str(usuario["_id"])
            
            if usuario["nombre_usuario"] == user_log.nombre_usario:

                if usuario["password"] == user_log.password:
                    return jwt.encode(usuario, my_secret, algorithm="HS256")
                
                return JSONResponse(status_code=401, content={"Message":"Wrong password"})
        
        return JSONResponse(status_code=404, content={"Message":"User not found"})


    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})


#recuperar todos los clientes
@app.get('/clients')
async def get_all():
    try:
        db = await connection()

        query = {"cliente.tipo":"cliente"}

        clientes = await db.usuarios.find(query).to_list(1000)

        clients_data = []

        for cliente in clientes:
            cliente["_id"] = str(cliente["_id"])

            clients_data.append(cliente["cliente"])

        return JSONResponse(status_code=200, content=clients_data)

    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})

#recuperar un cliente 
@app.get('/cliente/{user_name}')
async def get_client(user_name: str):
    try:
        db = await connection()

        cliente = await db.usuarios.find_one({"nombre_usuario":user_name})

        if not cliente:
            return JSONResponse(status_code=404, content={"Message": "Cliente no encontrado"})

        cliente["_id"] = str(cliente["_id"])

        return JSONResponse(status_code=200, content=cliente)

    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})

@app.put('/cliente/{user_name}/edit')
async def put_client(user_name: str, cliente: usuarios):
    try:
        db = await connection()

        client = await db.usuarios.find_one({"nombre_usuario":user_name})
        
        if not client:
            return JSONResponse(status_code=404, content={"Message":"Cliente no encontrado"})

        datos = jsonable_encoder(cliente)
        
        await db.usuarios.update_one({"nombre_usuario":user_name}, {"$set":datos})

        return JSONResponse(status_code=200, content={"Message":"Usuario actualizado"})
    
    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})


@app.delete('/user/{user_name}/delete')
async def delete_cliente(user_name:str, password: str):
    try:
        db = await connection()
        client = await db.usuarios.find_one({"nombre_usuario":user_name})

        if not client:
            return JSONResponse(status_code=404, content={"Message":"Cliente no econtrado"})
        
        if client["password"] == password:
            await db.usuarios.delete_one({"nombre_usuario":user_name})

            return JSONResponse(status_code=200, content={"Message":"User deleted"})

        return JSONResponse(status_code=400, content={"Message":"Contrasenia incorrecta"})

    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error!"})

#cliente crea una reservasion
@app.post('/cliente/{user_name}/reservar')
async def post_reserva_client(user_name: str, reservasion: reserva):
    try:
        db = await connection()
        cliente = await db.usuarios.find_one({"nombre_usuario":user_name})

        if cliente["nombre_usuario"] == user_name:
            await db.reservasiones.insert_one(jsonable_encoder(reservasion))
            return JSONResponse(status_code=201, content={"Message": "Reserva creada con exito"})
        
        else:
            return JSONResponse(status_code=404, content={"Message: Cliente no exite en la base de datos"})
    
    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})

@app.delete('cliente/{user_name}/reserva/edit')
async def edit_client_reservation(user_name: str, data:reserva):
    try:
        db = await connection()

        reservation = jsonable_encoder(data)

        client = await db.usuarios.find_one({"nombre_usuario":user_name})

        if not client:
            return JSONResponse(status_code=404, content={"Message":"Data not found"})
        
        await db.reservasiones.update_one({"cliente.nombre_usuario":user_name}, {"$set":reservation})

        return JSONResponse(status_code=200, content={"Message":"Reservation updated"})
        
    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error"})

@app.get('/hosters')
async def get_all_hosters():
    try:
        db = await connection()
        hosts_data = []

        hosts = await db.usuarios.find().to_list(1000)

        if not hosts:
            return JSONResponse(status_code=404, content={"Message":"No data found"})
        
        for host in hosts:
            host["_id"] = str(host["_id"])

            if "hoster" in host:
                hosts_data.append(host["hoster"])
        
        return JSONResponse(status_code=200, content=hosts_data)
                
                
    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error!"})

@app.get('/hosters/{tipo}')
async def get_all_hosters_by_type(tipo: str):
    try:
        db = await connection()

        query = {"hoster.tipo":tipo}
        
        hosts = await db.usuarios.find(query).to_list(1000)

        if not hosts:
            return JSONResponse(status_code=404, content={"Message":"No data found."})
        
        for host in hosts:
            host["_id"] = str(host["_id"])
    
        return JSONResponse(status_code=200, content={"Data":hosts})
    
    except:
        return JSONResponse(status_code=500, content={"Message": "Internal server error!"})

@app.get('/host/{name}')
async def get_host_by_name(name: str):
    try:
        db = await connection()

        data = await db.usuarios.find_one({"hoster.nombre":name})
        host = data["hoster"]

        if not host:
            return JSONResponse(status_code=404, content={"Message":"Data not found"})
        
        return JSONResponse(status_code=200, content=host)
    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error!"})

@app.put('/hosters/{user_name}/edit')
async def put_host_data(user_name: str, data: hosters):
    try:
        db = await connection()
        host = await db.usuarios.find_one({"nombre_usuario":user_name})

        if not host:
            return JSONResponse(status_code=404, content={"Message":"Host not found"})
        
        datos = jsonable_encoder(data)
        await db.usuario.update_one({"nombre_usuario":user_name}, {"$set":datos})
        return JSONResponse(status_code=200, content={"Message":"Host Update"}), {"Data": datos}
    
    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error!"})

@app.post('/recover/password/requests')
async def post_recover_password_requests(data: recover_password_request):
    try:
        db = await connection()

        user_data = jsonable_encoder(data)
        await db.password_requests.insert_one(user_data)

        return JSONResponse(status_code=201, content={"Message":"request saved"})

    except:
        return JSONResponse(status_code=500, content={"Message":"Internal server error"})

    
