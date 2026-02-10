"""
Tests for the Session Title Structure Module
"""

import unittest
from session_title import SessionTitle, create_session_title


class TestSessionTitle(unittest.TestCase):
    """Test cases for the SessionTitle class."""
    
    def test_full_structure(self):
        """Test a session title with all components."""
        title = SessionTitle("WIP", "Update session title structure", "improved clarity")
        expected = "[WIP] Update session title structure (improved clarity)"
        self.assertEqual(str(title), expected)
    
    def test_prefix_and_main_only(self):
        """Test a session title with prefix and main parts only."""
        title = SessionTitle("FEATURE", "Add new user authentication")
        expected = "[FEATURE] Add new user authentication"
        self.assertEqual(str(title), expected)
    
    def test_main_only(self):
        """Test a session title with only the main part."""
        title = SessionTitle(main="Daily standup meeting")
        expected = "Daily standup meeting"
        self.assertEqual(str(title), expected)
    
    def test_empty_title(self):
        """Test an empty session title."""
        title = SessionTitle()
        expected = "Untitled Session"
        self.assertEqual(str(title), expected)
    
    def test_repr(self):
        """Test the __repr__ method."""
        title = SessionTitle("BUG", "Fix login issue", "urgent")
        expected = "SessionTitle(prefix='BUG', main='Fix login issue', suffix='urgent')"
        self.assertEqual(repr(title), expected)


class TestCreateSessionTitle(unittest.TestCase):
    """Test cases for the create_session_title factory function."""
    
    def test_create_full_title(self):
        """Test creating a full session title."""
        result = create_session_title("WIP", "Update session title structure", "improved clarity")
        expected = "[WIP] Update session title structure (improved clarity)"
        self.assertEqual(result, expected)
    
    def test_create_partial_title(self):
        """Test creating a partial session title."""
        result = create_session_title("FEATURE", "Add authentication")
        expected = "[FEATURE] Add authentication"
        self.assertEqual(result, expected)
    
    def test_create_simple_title(self):
        """Test creating a simple session title."""
        result = create_session_title(main="Meeting")
        expected = "Meeting"
        self.assertEqual(result, expected)
    
    def test_create_empty_title(self):
        """Test creating an empty session title."""
        result = create_session_title()
        expected = "Untitled Session"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
