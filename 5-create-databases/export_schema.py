import sqlite3
import os
import sys

def export_sqlite_schema(db_path, output_file):
    """
    Extracts the schema from a SQLite database and writes it to a file.
    """
    # Validate database path
    if not os.path.isfile(db_path):
        print(f"Error: Database file '{db_path}' not found.")
        return False

    try:
        # Connect to the SQLite database (read-only mode)
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cursor = conn.cursor()

        # Retrieve schema from sqlite_master
        cursor.execute("SELECT sql FROM sqlite_master WHERE sql IS NOT NULL;")
        schema_statements = cursor.fetchall()

        if not schema_statements:
            print("No schema found in the database.")
            return False

        # Write schema to file
        with open(output_file, "w", encoding="utf-8") as f:
            for stmt in schema_statements:
                f.write(stmt[0] + ";\n\n")

        print(f"Schema successfully exported to '{output_file}'")
        return True

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_schema.py <database_path> <output_sql_file>")
        sys.exit(1)

    db_file = sys.argv[1]
    output_file = sys.argv[2]
    export_sqlite_schema(db_file, output_file)