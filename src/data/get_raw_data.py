#install libraries
!pip3 install pymysql
!pip3 install pandas

#import libraries
import pymysql
import os
import pandas as  pd 
import logging

# Database Connection details

cnx= {'host': 'localhost',
      'username': 'root',
      'password': '',
      'db': 'titanic'
} 

def getData(query, path):
    # open connection
    connection = pymysql.connect(cnx['host'],cnx['username'],cnx['password'],cnx['db'] )
    # open cursor
    cursor = connection.cursor()
    df = pd.read_sql_query(query, connection)

    with open(path, 'w') as handle:
        if len(df) > 0:
            df.to_csv(handle, header=True)
        else:
            print("err")   
    # Clean up
    cursor.close()
    connection.close()

    
                
def main(project_dir):
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
   
    # file path
    raw_data_path = os.path.join(project_dir,'data','raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')

    # extract train  and test data 
    getData("SELECT * FROM train", train_data_path)
    getData("SELECT * FROM test", test_data_path)


if __name__ == '__main__':
    # getting root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # call the main
    main(project_dir)


