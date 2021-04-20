from psdi.server import MXServer
from psdi.mbo import MboConstants
from psdi.mbo import MboValue
from java.sql import Statement;
from java.sql import PreparedStatement;
from java.sql import Connection;
from java.sql import ResultSet;
from psdi.mbo import Mbo;
import time;
mxserver = MXServer.getMXServer()
#userInfo = mbo.getUserInfo()
userInfo = mxserver.getSystemUserInfo()
#Check if there is any logged in users, not to start anything further if no user is logged in
sessionSetRemote = mxserver.getMboSet("MAXSESSION", userInfo)
count=sessionSetRemote.count()
if count !=0:
    timestamp = mxserver.getDate()
    currentSet = mxserver.getMboSet("MAXUSER",userInfo)
    currentMbo = currentSet.getMbo(0)
    con = currentMbo.getMboServer().getDBConnection(userInfo.getConnectionKey())
    sessionQuery = ['select distinct(userid) "userid" from maxsession where active = 1']
    sessionQuery =''.join(sessionQuery)
    s = con.createStatement()
    rs1 = s.executeQuery(sessionQuery)
    my_file = open('c:\\temp\\MASusageLog.csv','a')
    while(rs1.next()):
	    userid=rs1.getString('userid')
	    userSetRemote = mxserver.getMboSet("MAXUSER",userInfo)
	    userSetRemote.setWhere("USERID ='"+ userid + "'")
	    user = userSetRemote.getMbo(0)
	    usertype = user.getString("TYPE")
	    apppoint=0
	    #Rule engine below to also put nr of points per user. Edit this and add your user types
	    if usertype =="TYPE 1": apppoint=5
	    elif usertype =="TYPE 2": apppoint=10
	    elif usertype =="TYPE 3": apppoint=10
	    my_file.write(str(timestamp) + ','+ userid + ','+ usertype + ','+ str(apppoint)+ '\n')
    my_file.flush()
    my_file.close()
    rs1.close()
