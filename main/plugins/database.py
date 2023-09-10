import datetime
import motor.motor_asyncio
from .. import MONGODB_URI, AUTH
from .. import bot as CA
from telethon import events

class Database:
  
#Connection--------------------------------------------------------------------

    def __init__(self, MONGODB_URI, SESSION_NAME):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        self.db = self._client[SESSION_NAME]
        self.col = self.db.users

#collection handling---------------------------------------------------------
  
    async def get(self, id):
        user = await self.col.find_one({'id':int(id)})
        return user

    async def update_timer(self, id):
        await self.col.update_one({'id': id}, {'$set': {'timer': 2}})
    
@CA.on(events.NewMessage(incoming=True, from_users=AUTH, pattern="/get"))
async def db_command(event):
    x = event.text.split(" ")
    SESSION_NAME = x[1]
    id = x[2]
    db = Database(MONGODB_URI, SESSION_NAME)
    edit =  await event.reply("Processing...")
    data = await db.get(int(id))
    await edit.edit(str(data))

@CA.on(events.NewMessage(incoming=True, from_users=AUTH, pattern="/upd"))
async def db_command(event):
    x = event.text.split(" ")
    SESSION_NAME = x[1]
    id = x[2]
    db = Database(MONGODB_URI, SESSION_NAME)
    edit =  await event.reply("Processing...")
    data = await db.get(int(id))
    await edit.edit("done")
