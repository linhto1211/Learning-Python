mport csv
compromised_users=[]
with open('passwords.csv') as password_file:
  password_csv=csv.DictReader(password_file)
  password_row={}
  for row in password_csv:
    password_row.update(row)
    compromised_users.append(password_row['Username'])
print(compromised_users)
with open('compromised_users.txt','w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

import json
boss_message_dict={"recipient":"The Boss", "Message": "Mission Success"}
with open('boss_message.json','w') as boss_message:
  json.dump(boss_message_dict, boss_message)
slash_null_sig="""
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""

with open("new_passwords.csv",'w') as new_passwords_obj:
  new_passwords_obj = csv.DictWriter(new_passwords_obj,slash_null_sig)
print(new_passwords_obj)
