def calculate_average(scores):
    """Calculate the average of scores."""
    total = 0
    for s in scores:
        total += s
    return total / len(scores)


def find_highest(scores):
    """Find the highest score."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest


def find_lowest(scores):
    """Find the lowest score."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Process scores and display statistics."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

if __name__=="__main__":
        scores=[85,90,95,65,70]
        process_scores(scores)

