"""
Session Title Structure Module

This module provides a simple structure for managing session titles
with improved clarity.
"""


class SessionTitle:
    """
    A class to represent a session title with structured components.
    
    Attributes:
        prefix (str): The prefix part of the title (e.g., category, type)
        main (str): The main part of the title
        suffix (str): Optional suffix for additional context
    """
    
    def __init__(self, prefix: str = "", main: str = "", suffix: str = ""):
        """
        Initialize a SessionTitle instance.
        
        Args:
            prefix: The prefix part of the title
            main: The main part of the title
            suffix: Optional suffix for additional context
        """
        self.prefix = prefix
        self.main = main
        self.suffix = suffix
    
    def __str__(self) -> str:
        """
        Return a formatted string representation of the session title.
        
        Returns:
            A formatted string with proper structure
        """
        parts = []
        
        if self.prefix:
            parts.append(f"[{self.prefix}]")
        
        if self.main:
            parts.append(self.main)
        
        if self.suffix:
            parts.append(f"({self.suffix})")
        
        return " ".join(parts) if parts else "Untitled Session"
    
    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"SessionTitle(prefix={self.prefix!r}, main={self.main!r}, suffix={self.suffix!r})"


def create_session_title(prefix: str = "", main: str = "", suffix: str = "") -> str:
    """
    Factory function to create a formatted session title string.
    
    Args:
        prefix: The prefix part of the title (e.g., category, type)
        main: The main part of the title
        suffix: Optional suffix for additional context
    
    Returns:
        A formatted session title string
    
    Example:
        >>> create_session_title("WIP", "Update session title structure", "improved clarity")
        '[WIP] Update session title structure (improved clarity)'
    """
    title = SessionTitle(prefix, main, suffix)
    return str(title)


if __name__ == "__main__":
    # Example usage
    print("Session Title Structure Examples:")
    print("-" * 50)
    
    # Example 1: Full structure
    title1 = create_session_title("WIP", "Update session title structure", "improved clarity")
    print(f"1. {title1}")
    
    # Example 2: Without suffix
    title2 = create_session_title("FEATURE", "Add new user authentication")
    print(f"2. {title2}")
    
    # Example 3: Simple title
    title3 = create_session_title(main="Daily standup meeting")
    print(f"3. {title3}")
    
    # Example 4: Using class directly
    session = SessionTitle("BUG", "Fix login issue", "urgent")
    print(f"4. {session}")
