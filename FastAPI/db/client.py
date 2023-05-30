from pymongo import MongoClient

#Conexion con base de datos local
#db_client = MongoClient().local

#Conexion con base de datos remota
db_client = MongoClient("mongodb+srv://test:test@cluster0.ztpfckq.mongodb.net/?retryWrites=true&w=majority").test