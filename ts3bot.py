import ts3
import json
import time
import signal
import sys

with open('preferences.json', 'r') as f:
    prefs = json.load(f)
threshHold = prefs["threshHold"]
delay = prefs["delay"]
whitelistedgroups = prefs["whitelistedgroups"]
afkchannels = prefs["afkchannels"]
moveTo = prefs["moveTo"]
pokeAfterMove = prefs["pokeAfterMove"]
moveMsg = prefs["moveMsg"]
nickName = prefs["nickName"]
loginName = prefs["LoginName"]
password = prefs["Password"]

whitelistChannels=[]
whitelist=[] #Ignorieren
destination = int()
ts3conn = ""

def init(conn):
    global ts3conn
    ts3conn=conn
    signal.signal(signal.SIGINT, exit_gracefully)
    # use sid=1
    ts3conn.exec_("use", sid=1)
    ts3conn.exec_("clientupdate", client_nickname=nickName)

    resp = ts3conn.exec_("servergrouplist")
    for group in resp.parsed:
        if group['name'] in whitelistedgroups:
            clients = ts3conn.exec_("servergroupclientlist", sgid=group['sgid'])
            for client in clients.parsed:
                whitelist.append(client['cldbid'])
    global destination
    destination = ts3conn.exec_("channelfind",pattern=moveTo)[0]['cid']
    for channel in afkchannels:
        whitelistChannels.append(ts3conn.exec_("channelfind", pattern=channel)[0]['cid'])


def crawler():

    with ts3.query.TS3ServerConnection("ssh://{}:{}@localhost:10022".format(loginName, password)) as ts3conn:
        init(ts3conn)
        while True:
            ts3conn.send_keepalive()
            clients = ts3conn.exec_("clientlist", "times")
            for client in clients.parsed:
                if client["client_database_id"] in whitelist:
                    continue
                elif int(client["client_idle_time"]) >= threshHold*60000 and client['cid'] not in whitelistChannels:
                    ts3conn.exec_("clientmove", cid=destination, clid=client['clid'])
                    if pokeAfterMove:
                        try:
                            ts3conn.exec_("clientpoke", clid=client['clid'], msg=moveMsg)
                        except ts3.query.TS3QueryError:
                            pass
            time.sleep(delay)

def exit_gracefully(signal, frame):
    ts3conn.exec_("clientupdate", client_nickname=nickName + "_offline")
    ts3conn.exec_("logout")
    sys.exit(0)
      





            
if __name__ == "__main__":
    crawler()

        

#input("fertig")