"""
1. Digit at the beginning and a digit at the end of the string:
		Regular expression: ^\d.*\d$

	^: Matches the start of the string.
	\d: Matches any digit character(0-9).
	.*: Matches any characters zero or more times (including digits, letters, and symbols).
	\d: Matches another digit character.
	$: Matches the end of the string.

2. String containing only whitespace characters or word characters:
		Regular expression: ^[ \t]*[\w \t]*$

	^: Matches the start of the string.
	[\t]*: Matches zero or more whitespace characters (spaces or tabs).
	[\w \t]*: Matches zero or more word characters (letters, digits, or underscores) or whitespace characters.
	$: Matches the end of the string.

3. String containing no whitespace characters:
		Regular expression: ^\S*$

	^: Matches the start of the string.
	\S: Matches one or more characters that are not whitespace characters.
	*: Matches zero or more occurrences of the preceding character (in this case, non-whitespace characters).
	$: Matches the end of the string."""
