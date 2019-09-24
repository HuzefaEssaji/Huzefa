
# to open file containing all names of students
with open('abc.txt','r') as names:
   #to open a new file where all the new email id's of students will be stored.
    with open ('abc2.txt','w') as email_id_list:
       #to import names and create a list of the names.
        name_list=names.readlines()
        #creating an empty list first.
        sep_name_list=[]
        #looping for each name in the name list.
        for item in name_list:
            itemwords=item.split()              #name got split into two words.
            sep_name_list.extend(itemwords)    #two separated words(first name and surname)got stored in the empty list.
            x=len(sep_name_list)              #finding the length of the list.
            if x==2:                    #if two word name then s.name+firstletter         

                email_id=sep_name_list[1]+sep_name_list[0][0]+"@rknec.edu"
            else :
                email_id=sep_name_list[2]+sep_name_list[0][0]+sep_name_list[1]+"@rknec.edu"   #adding the surname+first letter of name+email domain name.
            print(email_id)                      #printing the emails ids in command prompt (optional).
            sep_name_list=[]                     #sep_name_listemptying the list for the next element.
            email_id_list.write(email_id)        #writing the generated email ids to the new file.
            email_id_list.write('\n')            #printing new line for better presentation.