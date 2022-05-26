import os,sys,mysql.connector
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR

start_permission=input('\nDo you want to perform MySQL operations (YES-Y/NO-N): ')
print()

def ncpl_dbms_with_mysql():
    mysql_user_name=input('Enter your MySQL user-name: ')
    mysql_pass_word=input('Enter your MySQL pass-code: ')

    mydb=mysql.connector.connect(host="localhost",user=mysql_user_name,password=mysql_pass_word)        
    mycursor=mydb.cursor()
    mydb.autocommit=True

    while start_permission in ['YES','yes','Y','y','YeS','Yes','yES','yeS','YEs','YA','yA','Ya']:
        print('''
            1. Display Data-Bases
            2. Update Data-Base
            3. Add Data-Base
            4. Delete Data-Base
            5. EXIT !!
            6. Change your MySQL user-name  (NOT RECOMMENDED)
            7. Change your MySQL pass-code  (NOT RECOMMENDED)''')
        db_choice=int(input('What do you want to do ??: '))
        if db_choice==1:
            mycursor.execute('SHOW DATABASES')
            data=mycursor.fetchall()
            for d in data:
                print(d)

        elif db_choice==3:
            db_name=input('Enter Data-Base Name to create: ')
            cmd_to_create_db='CREATE DATABASE '+db_name
            mycursor.execute(cmd_to_create_db)
            print('\nQuery Executed Successfully !!')
            print(mycursor.rowcount,'Data-Base Inserted')

        elif db_choice==4:
            db_name=input('Enter Data-Base Name to delete: ')
            cmd_to_del_db='DROP DATABASE '+db_name
            mycursor.execute(cmd_to_del_db)
            print('\nQuery Executed Successfully !!')
            print(mycursor.rowcount+1,'Data-Base Deleted')

        elif db_choice==5:
            print('\nEXITING !!\n')
            break

        elif db_choice==6:
            verify_mysql_username=input('\nEnter your current MySQL user-name: ')
            verify_mysql_password=input('Enter your current MySQL pass-code: ')
            if verify_mysql_username==mysql_user_name and verify_mysql_password==mysql_pass_word:
                new_mysql_username=input('\nEnter your new MySQL user-name: ')
                cmd_to_change_mysql_username='UPDATE MYSQL.USER SET USER='+"'"+new_mysql_username+"'"+' WHERE USER='+"'"+verify_mysql_username+"'"
                mycursor.execute(cmd_to_change_mysql_username)
                print('\nYour user-name has been successfully changed from',mysql_user_name,'to',new_mysql_username)
                print('\nNote this somewhere safe and easily accessible as it is not retrievable and may lead to several complications')
                print('\tsuch as your MySQL DB & Tables data will need to be formatted to reset this user-name')
                def save_mysql_credentials():
                    os.chmod('MySQL_credentials.txt', S_IWUSR|S_IREAD)
                    with open('MySQL_credentials.txt','w') as file:
                        data='MySQL USERNAME - '+new_mysql_username+'\n'+'MySQL PASSWORD - '+verify_mysql_password
                        file.write(data)
                    os.chmod('MySQL_credentials.txt',S_IREAD|S_IRGRP|S_IROTH)
                try:
                    save_mysql_credentials()                    
                except FileNotFoundError:
                    with open('MySQL_credentials.txt','w') as file:
                        pass
                    save_mysql_credentials()
                    
            elif verify_mysql_username!=mysql_user_name and verify_mysql_password==mysql_pass_word:
                sys.stderr.write('\nuser-name is not verified...')
            elif verify_mysql_username==mysql_user_name and verify_mysql_password!=mysql_pass_word:
                sys.stderr.write('\nuser pass-code is not verified...')
            else:
                sys.stderr.write('\nuser-name & user pass-code are not verified...')

        elif db_choice==7:
            verify_mysql_username=input('\nEnter your current MySQL user-name: ')
            verify_mysql_password=input('Enter your current MySQL pass-code: ')
            if verify_mysql_username==mysql_user_name and verify_mysql_password==mysql_pass_word:
                new_mysql_password=input('\nEnter your new MySQL pass-code: ')
                cmd_to_change_mysql_password='ALTER USER '+mysql_user_name+'@LOCALHOST IDENTIFIED BY '+"'"+new_mysql_password+"'"
                mycursor.execute(cmd_to_change_mysql_password)
                print('\nYour pass-code has been successfully changed from',mysql_pass_word,'to',new_mysql_password)
                print('\nNote this somewhere safe and easily accessible as it is not retrievable and may lead to several complications')
                print('\tsuch as your MySQL DB & Tables data will need to be formatted to reset this pass-code')
                def save_mysql_credentials():
                    os.chmod('MySQL_credentials.txt', S_IWUSR|S_IREAD)
                    with open('MySQL_credentials.txt','w') as file:
                        data='MySQL USERNAME - '+verify_mysql_username+'\n'+'MySQL PASSWORD - '+new_mysql_password
                        file.write(data)
                    os.chmod('MySQL_credentials.txt',S_IREAD|S_IRGRP|S_IROTH)
                try:
                    save_mysql_credentials()                    
                except FileNotFoundError:
                    with open('MySQL_credentials.txt','w') as file:
                        pass
                    save_mysql_credentials()
            elif verify_mysql_username!=mysql_user_name and verify_mysql_password==mysql_pass_word:
                print('\nuser-name is not verified...')
            elif verify_mysql_username==mysql_user_name and verify_mysql_password!=mysql_pass_word:
                print('\nuser pass-code is not verified...')
            else:
                print('\nuser-name & user pass-code are not verified...')
            
        while db_choice==1 or db_choice==2:
            start_db_table_operations=input('Do you want to perform Data-Base Table operations: ')
            while start_db_table_operations in ['YES','yes','Y','y','YeS','Yes','yES','yeS','YEs']:
                db_to_use=input('Enter Data-Base to use: ')
                mydb_table=mysql.connector.connect(host="localhost",
                                           user=mysql_user_name,
                                           password=mysql_pass_word,
                                           database=db_to_use)
                mycursor_table=mydb_table.cursor()
                mydb_table.autocommit=True
                while start_db_table_operations in ['YES','yes','Y','y','YeS','Yes','yES','yeS','YEs']:
                    print('''
                    1. Display Tables
                    2. Modify Records in a Table
                    3. Add Table
                    4. Insert Records in a Table
                    5. Delete Table
                    6. Go Back in the Menu !!''')
                    db_table_choice=int(input('What do you want to do ??: '))
                    if db_table_choice==2:
                        


                        print('\nNot Available at the Moment !!\n Sorry for the inconvenience !!')


                    
                    elif db_table_choice==3:
                        table_name=input('Enter Table Name to add: ');str1=' '
                        list1=['CREATE TABLE',table_name]
                        str1=str1.join(list1)
                        print('\n\t\tOne Column is must');column_record_entry_tuple=''
                        no_of_columns=int(input('Enter no. of columns to add: '))
                        print('''\nEnter Column_Record in FORMAT : <Column_Name> <data_type(size_of_data_type)> <Primary Key / NULL / NOT NULL>
                                                Place a comma after <data_type(size_of_data_type)> for more than one entries
                                                                ALL THE SYMBOLS ARE MUST !!!!!''')
                        for j in range(no_of_columns):
                            column_record_entry=input('Enter record entry: ')

                            column_record_entry_tuple=column_record_entry_tuple+column_record_entry
                        cmd_to_add_column_record=str1+'('+column_record_entry_tuple+')'
                        mycursor_table.execute(cmd_to_add_column_record)
                        print(table_name,'Table has been created')
                        print(mycursor_table.rowcount,'Columns Inserted in the Table',table_name)

                    elif db_table_choice==4:
                        def insert_records():
                            insert_cmd_1='INSERT INTO '+table_name+' VALUES'
                            print('''Enter table_data separated by commas with no extra space and enclose words in inverted commas ''')
                            insert_cmd_2=input('Enter data to insert into table: ')
                            insert_cmd=insert_cmd_1+'('+insert_cmd_2+')'
                            mycursor.execute(insert_cmd)
                        table_name=input('Enter Table Name into insert records: ')
                        insert_records()
                        continue_insert=input('Do you want to continue inserting records: ')
                        if continue_insert in ['YES','yes','Y','y','YeS','Yes','yES','yeS','YEs']:
                            insert_records()
                        
                    elif db_table_choice==5:
                        table_name=input('Enter Table Name to delete: ')
                        cmd_to_del_table='DROP TABLE '+table_name
                        mycursor_table.execute(cmd_to_del_table)
                        print('\nQuery Executed Successfully !!')
                        print(mycursor_table.rowcount,'Rows Affected')

                    elif db_table_choice==6:
                        print('\nGoing Back !!')
                        start_db_table_operations='NO'

                    while db_table_choice==1:
                        mycursor_table.execute('SHOW TABLES;')
                        data=mycursor_table.fetchall()
                        for d in data:
                            print(d)
                        print('''
                        1. Describe Table Structure
                        2. Show inserted records
                        3. Go Back in the Menu !!''')
                        db_show_table_choice=int(input('What do you want to do ??: '))
                        if db_show_table_choice==1:
                            table_name=input('Enter Table Name to describe its structure: ')
                            cmd_to_desc_table='DESC '+table_name
                            mycursor_table.execute(cmd_to_desc_table)
                            data_table_column=mycursor_table.fetchall()
                            for d in data_table_column:
                                print(d)
                            print()

                        elif db_show_table_choice==3:
                            print('\nGoing Back !!')
                            break

                        while db_show_table_choice==2:
                            print('''
                            1. Show all inserted records
                            2. Show only some inserted records
                            3. Go Back in the Menu !!''')
                            db_inserted_records_choice=int(input('What do you want to do ??: '))
                            if db_inserted_records_choice==1:
                                table_name=input('Enter Table Name to show its inserted records: ')
                                cmd_to_show_table_records='SELECT * FROM '+table_name
                                mycursor_table.execute(cmd_to_show_table_records)
                                data_table_rows=mycursor_table.fetchall()
                                for d in data_table_rows:
                                    print(d)

                            elif db_inserted_records_choice==3:
                                print('\nGoing Back !!')
                                break

                            elif db_inserted_records_choice==2:
                                table_name=input('Enter Table Name to show its inserted records: ');str1=' '
                                column_name=input('Enter Columns Name separated by commas: ')
                                list1=['SELECT',column_name,'FROM',table_name]
                                cmd_to_show_table_records=str1.join(list1)
                                mycursor_table.execute(cmd_to_show_table_records)
                                data=mycursor_table.fetchall()
                                for d in data:
                                    print(d)

    ##                        else:
    ##                            print('You have entered incorrect value !!')
    ##                    else:
    ##                        print('You have entered incorrect value !!')
    ##                else:
    ##                    print('You have entered incorrect value !!')
    ##            else:
    ##                print('You have entered incorrect value !!')
            else:
                break
    ##    else:
    ##        print('You have entered incorrect value !!')
    else:
        print('\nEXITING !!\n')

    mycursor.close()
    mydb.close()
try:
    ncpl_dbms_with_mysql()
except Exception as e:
##    sys.stderr.write('\nYour user-name & pass-word for accessing MySQL are incorrect...\n\t\tPlease try again...!!')
    print('\n',e)
