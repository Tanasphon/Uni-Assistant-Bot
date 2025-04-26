import psycopg2
from psycopg2.extras import RealDictCursor
from config import DATABASE_URL

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
            self.cursor = self.conn.cursor()
            self._create_tables()
        except Exception as e:
            print(f"Database connection error: {e}")

    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        create_tables_queries = [
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                telegram_id VARCHAR(50),
                line_id VARCHAR(50),
                student_id VARCHAR(20),
                department VARCHAR(50),
                year INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS faq (
                id SERIAL PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                category VARCHAR(50),
                department VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS schedules (
                id SERIAL PRIMARY KEY,
                student_id VARCHAR(20),
                course_code VARCHAR(20),
                course_name VARCHAR(100),
                day VARCHAR(10),
                start_time TIME,
                end_time TIME,
                room VARCHAR(50),
                semester VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                message TEXT,
                response TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]

        for query in create_tables_queries:
            try:
                self.cursor.execute(query)
                self.conn.commit()
            except Exception as e:
                print(f"Error creating table: {e}")
                self.conn.rollback()

    def add_user(self, telegram_id=None, line_id=None, student_id=None, department=None, year=None):
        """Add a new user to the database."""
        query = """
        INSERT INTO users (telegram_id, line_id, student_id, department, year)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """
        try:
            self.cursor.execute(query, (telegram_id, line_id, student_id, department, year))
            self.conn.commit()
            return self.cursor.fetchone()['id']
        except Exception as e:
            print(f"Error adding user: {e}")
            self.conn.rollback()
            return None

    def get_user(self, telegram_id=None, line_id=None):
        """Get user information."""
        query = """
        SELECT * FROM users WHERE telegram_id = %s OR line_id = %s
        """
        try:
            self.cursor.execute(query, (telegram_id, line_id))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def add_faq(self, question, answer, category, department=None):
        """Add a new FAQ entry."""
        query = """
        INSERT INTO faq (question, answer, category, department)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """
        try:
            self.cursor.execute(query, (question, answer, category, department))
            self.conn.commit()
            return self.cursor.fetchone()['id']
        except Exception as e:
            print(f"Error adding FAQ: {e}")
            self.conn.rollback()
            return None

    def get_faq(self, category=None, department=None):
        """Get FAQ entries."""
        query = """
        SELECT * FROM faq
        WHERE (%s IS NULL OR category = %s)
        AND (%s IS NULL OR department = %s)
        """
        try:
            self.cursor.execute(query, (category, category, department, department))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error getting FAQ: {e}")
            return None

    def add_schedule(self, student_id, course_code, course_name, day, start_time, end_time, room, semester):
        """Add a course schedule."""
        query = """
        INSERT INTO schedules (student_id, course_code, course_name, day, start_time, end_time, room, semester)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """
        try:
            self.cursor.execute(query, (student_id, course_code, course_name, day, start_time, end_time, room, semester))
            self.conn.commit()
            return self.cursor.fetchone()['id']
        except Exception as e:
            print(f"Error adding schedule: {e}")
            self.conn.rollback()
            return None

    def get_schedule(self, student_id, semester=None):
        """Get student's schedule."""
        query = """
        SELECT * FROM schedules
        WHERE student_id = %s
        AND (%s IS NULL OR semester = %s)
        ORDER BY day, start_time
        """
        try:
            self.cursor.execute(query, (student_id, semester, semester))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error getting schedule: {e}")
            return None

    def close(self):
        """Close database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close() 