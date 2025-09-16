# Assignment 1: AI-Generated Python Problems
# Name: [Maddox Bartoli]

"""
AI-Generated Problem Set

INSTRUCTIONS: 
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:" My classmate is having trouble understanding for-loops in Python. 
This is my code:for i in range(1, 4): print(i) can you explain this to them as if they are just now learning about loops.
Specifically, explain the purpose for loops and how the range function works and why you go from 1 to 4 to print out 1-3."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [My classmate is having trouble understanding for-loops in Python. 
This is my code:for i in range(1, 4): print(i) can you explain this to them as if they are just now learning about loops.
Specifically, explain the purpose for loops and how the range function works and why you go from 1 to 4 to print out 1-3."]

What's the PURPOSE of for-loops?
Imagine you want to print numbers 1, 2, 3. Without a loop, you'd write:
pythonprint(1)
print(2) 
print(3)
That's tedious! A for-loop says "repeat this action multiple times" - it's like having a robot do repetitive tasks for you.
How does range(1, 4) work?
Think of range() like a ticket machine:

range(1, 4) makes tickets numbered 1, 2, 3
It starts at 1 (the first number)
It stops before 4 (the second number)
So you get tickets: 1, 2, 3 (but NOT 4)

Why 1 to 4 to print 1-3?
This trips up everyone at first! Python's range() is "exclusive" of the end number:

range(1, 4) = 1, 2, 3 ✅
range(1, 3) = 1, 2 ❌ (missing the 3!)

It's like saying "drive from mile 1 to mile 4" - you pass miles 1, 2, and 3, then stop before reaching mile 4.
The loop just takes each number from range and puts it into the variable i, then runs print(i) each time!

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""




# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

def calculate_grade(score):
    """
    
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"


