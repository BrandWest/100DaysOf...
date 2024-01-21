
'''
try:
    Try to do something here
except:
    Execute this if the try fails.
else:
    If there were no exceptions do this
finally:
    Carry out no matter what happens.
    Used to tidy up code executions.
'''

#Read errors
try:
    with open ("a_file.txt", "r") as file:
        file.read()
    a_dict = { "key": "value"}
    # value = a_dict["non_key"]
except FileNotFoundError as e:
    print(e)
    #creates the file
    open("a_file.txt", "w")
except KeyError as e:
    print(f"The key {e} does not exists")
else:
    content = open("a_file.txt", "r")
    print(content.read())
finally:
    #Will run no matter what.
    content.close()
    print("Close file")

    

'''
#Key Error
try:
    a_dict = { "key": "value"}
    value = a_dict["non_key"]
except Exception as e:
    print(e)

#index out of range
try:
    index_error = [1,2,3]
    print(index_error[19])
except Exception as e:
    print(e)

#Type Error
try:
    test_var = 9
    print(test_var + " string")
except Exception as e:
    print(e)
'''