import os 
import datetime

#open the file where_am_i.txt
with open('where_am_i.txt', 'r') as f:
    #read the file
    content = f.read()
    #print the content
    Current_RSE=content.split(",")[0]
    
today=datetime.datetime.now()
newest_file = None
newest_date = datetime.datetime.min

#for each RSE in the list
for RSE in os.listdir('/home/pioyar/RSE'):
    if RSE==Current_RSE:
        print(RSE)
        #if there are files in the RSE
        if os.listdir('/home/pioyar/RSE/'+RSE):
            # loop through the files in the directory
            for file_name in os.listdir('/home/pioyar/RSE/'+RSE):
                # check if the file name matches the expected pattern
                if file_name.startswith('LUND_GRIDFTP_rucio_dump_') and file_name.endswith('.txt'):
                    # extract the date from the file name
                    date_str = file_name.split('_')[-1].replace('.txt', '')
                    file_date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
                    # check if this file is newer than the current newest file
                    if file_date > newest_date:
                        newest_file = file_name
                        newest_date = file_date
            # print the name of the newest file
            print(newest_file)
            #run the bash script called dump_directories_to_file.sh with the newest file as argumetn one and the '/home/pioyar/RSE/'+RSE as argument two
            os.system("./dump_directories_to_file.sh "+"/home/pioyar/RSE/"+str(RSE)+"/"+str(newest_file)+" /home/pioyar/RSE/"+str(RSE))
        else:
            print("No files in the RSE")