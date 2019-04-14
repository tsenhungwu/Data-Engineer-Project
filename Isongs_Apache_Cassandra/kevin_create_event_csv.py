# Part I. ETL Pipeline for Pre-Processing the Files

# Import Python packages 
import os
import glob
import csv


def get_all_filepaths():
    '''
    Create list of filepaths to process original event csv data files.
    Output: A list object storing all file paths.
    '''
    # Get the current folder path and subfolder Data.
    filepath = os.getcwd() + '/Data'

    # Use a for loop to create a list of file paths.
    for root, dirs, files in os.walk(filepath):
    
        # Join the file path and roots with the subdirectories using glob.
        file_path_list = glob.glob(os.path.join(root,'*'))

    return file_path_list


# Processing the files to create the data file csv that will be used for Apache Casssandra tables
def creat_data_file_csv(file_path):
    '''
    file_path: A list object storing all file paths.
    Output: Create a smaller event data csv file called event_datafile_full.csv.
    '''
    total_file_paths = len(file_path)

    # Initiate an empty list of for storing data.
    full_data_rows_list = [] 
    
    # Loop into each file to extract data.
    for i in range(len(file_path)):
        print('{}/{} files have been processed.'.format(i,total_file_paths))
        # Read a csv file.
        with open(file_path[i], 'r', encoding = 'utf8', newline='') as csvfile: 
            csvreader = csv.reader(csvfile)
            # Skip the first row 
            next(csvreader)
        
            # Extract data row by row and append it into an empty list      
            for line in csvreader:
                full_data_rows_list.append(line) 
            

    # Create a smaller event data csv file called event_datafile_full.csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName',\
                        'length', 'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[12],row[13],row[16]))
    
    # Read event_datafile_new.csv and see how many records.
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print('{} of records have been stored successfully.'.format(sum(1 for line in f)))
        
def main():
    file_paths = get_all_filepaths()
    creat_data_file_csv(file_path=file_paths)

if __name__ == "__main__":
    main()