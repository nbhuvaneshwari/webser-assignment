from bottle import route, run, template, get, post, request, put, delete
p_dict={}
store_info=[]

@post('/patient/create') 
def add_patient():
    idn = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    phone = request.POST['phone']
    store_info = ' '.join([name,gender,age,address,phone])
    p_dict.update({idn:store_info})
    return p_dict

@get('/patient/<idn>')
def read_patient(idn):
    return p_dict

@put('/patient/<idn>')
def update_patient(idn):
	if idn in p_dict.keys():
		 p_dict.update(name = request.POST['name'],gender = request.POST['gender'],age = request.POST['age'],address = request.POST['address'],phone = request.POST['phone'])
		 return 'Updated Sucessfull'
	else:
		return 'Not Exist'

@delete('/patient/<idn>')
def delete_patient(idn):
    if idn in p_dict.keys():
        del(p_dict[idn])
        return 'patient record deleted.'
    else:
        return 'No such record found id ',idn

run(host='localhost',port=8080)
