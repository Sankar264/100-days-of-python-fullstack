
email_id="saketh@codegnan.com"
print(email_id[7:-4])
email_id=['sankar@gmail.com',
          'ekannth@gmail.com',
          'bharat@gmail.com',
          'rohith@gmail.com']
print(len(email_id))
print(email_id[-2 :])
print(type(email_id[-2 :]))
email_id.extend(['qwe@gmail.com','asd@gmail.com','zxc@gmail.com'])
for mail in email_id:
    print(mail)
    print(f'mail id of the person is {mail}')
users={}
for i in range(len(email_id)):
    users[i]=email_id[i]
print(users)
users=dict.fromkeys(email_id)
users['sankar@gmail.com']=123
print(users)

users=enumerate(email_id,3)
print(dict(users))


               

