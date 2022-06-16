import json
import sqlite3

def main():
    try:
        #connect to database
        database = sqlite3.connect('./cma-artworks.db')

        #instantiate cursor
        cursor = database.cursor()

        #dict to be dumped
        dict = {
        }

        #find where artwork/creator overlap, as well as artwork/department overlap
        query = '''
                SELECT DISTINCT
                a.id,
                a.title,
                a.tombstone,
                a.accession_number,
                c.id,
                c.role,
                c.description,
                d.id,
                d.name
                FROM artwork AS a
                INNER JOIN artwork__creator AS ac ON ac.artwork_id = a.id
                INNER JOIN creator AS c ON c.id = ac.creator_id
                INNER JOIN artwork__department AS ad ON ad.artwork_id = a.id
                INNER JOIN department AS d ON d.id = ad.department_id
                ORDER BY a.id
                '''

        cursor.execute(query)
        table = cursor.fetchall()

        #put contents of table into dictionary
        for tup in table:
            if not tup[0] in dict:
                dict[tup[0]] = {
                        "title" : tup[1],
                        "tombstone" : tup[2],
                        "accession number" : tup[3],
                        "creator(s)" : [{
                            "role" : tup[5].capitalize(),
                            "description" : tup[6]
                            }],
                        "department name" : tup[8]
                        }
            #if there is more than one creator
            else:
                dict[tup[0]]["creator(s)"].append({
                    "role" : tup[5].capitalize(),
                    "description" : tup[6]
                    })

        #write to json file
        json_object = json.dumps(dict, indent = 4)
        with open("representation.json", "x") as outfile:
            outfile.write(json_object)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table,", error)

    finally:
        if database:
            database.close()

main()
