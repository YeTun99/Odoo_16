from xmlrpc import client
server_url =
db_name=
username=
password=
common=client.ServerProxy('%s/xmlrpc/2/common' %
                          server_url)
user_id=common.authenticate(db_name,username,
                            password,{})
models=client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    search_domain=[]
    partner_ids=models.execute_kw(db_name,user_id,password,'res.partner','search',[search.db_name])
    print('partner ids found',partner_ids)
    partner_data=models.execute_kw(db_name,user_id,password,'res.partner','read',[partner_ids,['name']])
    print("Partner data:",partner_ids)
else:
    print("Wrong credentials")