from pathlib import Path
import json

SESSION_DIR = Path("sessions")
SESSION_DIR.mkdir(exist_ok=True)

def create_session_file(session_id: str):
    """Create a session file with the given session ID."""
    session_file = SESSION_DIR / f"{session_id}.json"
    if not session_file.exists():
        session_file.write_text(json.dumps({"session_id": session_id}))
    """Prints the session file creation status."""
    print(f"Session file created: {session_file}")
    return session_file

def delete_session_file(session_id: str):
    """Delete the session file with the given session ID."""
    session_file = SESSION_DIR / f"{session_id}.json"
    if session_file.exists():
        session_file.unlink()
    """Prints whether the session file was successfully deleted."""
    print(f"Session file {session_id} deleted: {not session_file.exists()}")
    return not session_file.exists()

