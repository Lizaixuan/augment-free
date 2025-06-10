from printer import Printer
import sqlite3
import shutil
import os


class StateDB:

    def __init__(self, file_path, printer: Printer):
        self.file_path = file_path
        self.printer = printer

    def backup_file(self) -> str:
        """
        Create a backup of the state database file.

        Returns:
            str: Path to the backup file
        """
        # Create backup path by adding .bak suffix
        backup_path = self.file_path + ".bak"

        # Create the backup
        shutil.copy2(self.file_path, backup_path)

        return backup_path

    def reset(self):
        """
        Reset the state database by removing all augment-related entries.
        First creates a backup, then deletes all entries with keys containing 'augment',
        and finally verifies deletion by checking if any keys containing 'Augment' remain.
        """
        conn = None
        try:
            # Backup the database first
            if os.path.exists(self.file_path):
                backup_path = self.backup_file()
                self.printer.success(f"Backup state.vscdb to: {backup_path}")

            # Connect to the SQLite database
            conn = sqlite3.connect(self.file_path)
            cursor = conn.cursor()

            # Delete all entries with keys containing 'augment'
            cursor.execute("DELETE FROM ItemTable WHERE key LIKE '%augment%'")
            deleted_count = cursor.rowcount
            self.printer.info(f"Deleted {deleted_count} augment-related entries")

            # Commit the changes
            conn.commit()

            # Verify deletion by checking if any keys containing 'Augment' remain
            cursor.execute(
                "SELECT key, value FROM ItemTable WHERE key LIKE '%Augment%'"
            )
            remaining = cursor.fetchall()

            if not remaining:
                self.printer.success("Reset state.vscdb completed successfully")
            else:
                self.printer.warning(
                    f"Reset incomplete: {len(remaining)} augment-related entries still exist"
                )
                for key, value in remaining:
                    self.printer.info(f"Remaining entry: {key}")

            return len(remaining) == 0

        except sqlite3.Error as e:
            self.printer.error(f"SQLite error during reset: {e}")
            return False
        except Exception as e:
            self.printer.error(f"Error during reset: {e}")
            return False
        finally:
            # Ensure connection is closed even if an exception occurs
            if conn:
                conn.close()
