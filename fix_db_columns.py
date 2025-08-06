import sqlite3
import os

def fix_database_schema():
    """Add missing columns to the security_reviews table"""
    db_path = 'securearch_portal.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Database file {db_path} not found!")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check current table schema
        cursor.execute("PRAGMA table_info(security_reviews)")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"📋 Current columns: {columns}")
        
        # Add author_id column if missing
        if 'author_id' not in columns:
            print("➕ Adding author_id column...")
            cursor.execute("ALTER TABLE security_reviews ADD COLUMN author_id TEXT")
            print("✅ Added author_id column")
        else:
            print("✅ author_id column already exists")
        
        # Add field_type column if missing
        if 'field_type' not in columns:
            print("➕ Adding field_type column...")
            cursor.execute("ALTER TABLE security_reviews ADD COLUMN field_type TEXT DEFAULT 'application_review'")
            print("✅ Added field_type column")
        else:
            print("✅ field_type column already exists")
        
        # Commit changes
        conn.commit()
        
        # Verify the changes
        cursor.execute("PRAGMA table_info(security_reviews)")
        updated_columns = [row[1] for row in cursor.fetchall()]
        print(f"📋 Updated columns: {updated_columns}")
        
        print("🎉 Database schema updated successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    fix_database_schema() 