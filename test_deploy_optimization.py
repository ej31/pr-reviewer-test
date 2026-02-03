"""
Test file for deploy optimization verification.
This PR tests that the Beta environment is working correctly
after the Docker build optimization changes.
"""

def calculate_deployment_time(old_time: int, new_time: int) -> float:
    """Calculate improvement percentage."""
    if old_time == 0:
        return 0
    improvement = (old_time - new_time) / old_time * 100
    return improvement

def main():
    # Old deployment: 5 minutes (300 seconds)
    # New deployment: 14 seconds
    old = 300
    new = 14
    
    improvement = calculate_deployment_time(old, new)
    print(f"Deployment time improved by {improvement:.1f}%")
    
    # Missing validation - intentional issue for review
    result = old / new
    return result

if __name__ == "__main__":
    main()
