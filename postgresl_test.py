import psycopg2

def open_connection():
    try:
        connection = psycopg2.connect(host = "localhost",
                                    user="josephsmith",
                                    port="5432",
                                    database="recipemanager")
        return(connection)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

def close_connection(connection):
    connection.close()
    print("PostgreSQL connection is closed")
    
        

def create_tables(connection):

    cursor = connection.cursor()

    create_table_query_1 = '''CREATE TABLE recipes
          (ID INT PRIMARY KEY     NOT NULL,
          TITLE           TEXT    NOT NULL,
          FEEDS           INT     NOT NULL,
          CALORIES        INT     NOT NULL,
          PREP_TIME       INT     NOT NULL,
          COOK_TIME       INT     NOT NULL,
          INSTRUCTIONS    TEXT    NOT NULL); '''

    create_table_query_2 = '''CREATE TABLE ingredients
          (ID INT PRIMARY KEY     NOT NULL,
          INGREDIENT      TEXT    NOT NULL); '''

    create_table_query_3 = '''CREATE TABLE recipes_ingredients
          (RECIPE_ID             INT     NOT NULL,
          INGREDIENT_ID          INT    NOT NULL,
          AMOUNT                 TEXT    NOT NULL,
          PREPARATION            TEXT    NOT NULL); '''

    create_table_query_4 = '''CREATE TABLE tags
          (ID INT PRIMARY KEY     NOT NULL,
          TAG             TEXT    NOT NULL); '''

    create_table_query_5 = '''CREATE TABLE recipes_tags
          (RECIPE_ID INT PRIMARY KEY     NOT NULL,
          TAG_ID          INT    NOT NULL); '''

    query_list = [create_table_query_1, create_table_query_2, create_table_query_3, create_table_query_4, create_table_query_5]
    for query in query_list:
        cursor.execute(query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
            

    
conn = open_connection()
create_database(conn)
create_tables(conn)
close_connection(conn)