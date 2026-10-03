"""
DecodeLabs - Artificial Intelligence Project 3
Simple AI Recommendation System

Requirements:
1. Take user interests as input
2. Match interests with item tags
3. Calculate similarity using Jaccard similarity
4. Display recommended items
"""

# Recommendation dataset
items = [
    {
        "name": "Python for AI",
        "category": "Course",
        "tags": {"python", "ai", "programming", "machine learning"}
    },
    {
        "name": "Machine Learning Fundamentals",
        "category": "Course",
        "tags": {"python", "ai", "machine learning", "algorithms"}
    },
    {
        "name": "Deep Learning",
        "category": "Course",
        "tags": {"python", "ai", "deep learning", "neural networks"}
    },
    {
        "name": "Data Science Bootcamp",
        "category": "Course",
        "tags": {"python", "data science", "pandas", "statistics"}
    },
    {
        "name": "Web Development with Django",
        "category": "Course",
        "tags": {"python", "django", "web development", "backend"}
    },
    {
        "name": "Computer Vision Projects",
        "category": "Project",
        "tags": {"python", "ai", "computer vision", "opencv"}
    },
    {
        "name": "Natural Language Processing",
        "category": "Course",
        "tags": {"python", "ai", "nlp", "deep learning"}
    }
]


# Clean user input
def clean_text(text):
    return text.strip().lower()


# Calculate Jaccard similarity
def calculate_similarity(user_interests, item_tags):

    common = user_interests.intersection(item_tags)
    total = user_interests.union(item_tags)

    if len(total) == 0:
        return 0

    return len(common) / len(total)


# Get recommendations
def recommend(user_interests):

    results = []

    for item in items:

        score = calculate_similarity(
            user_interests,
            item["tags"]
        )

        matched = user_interests.intersection(item["tags"])

        results.append({
            "name": item["name"],
            "category": item["category"],
            "score": score,
            "matched": matched
        })

    # Highest score first
    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:5]


# Main program
print("=" * 55)
print("       DecodeLabs AI Recommendation System")
print("                 Project 3")
print("=" * 55)

print("\nExample interests:")
print("Python, AI, machine learning")
print("Data science, web development, deep learning")

while True:

    user_input = input(
        "\nEnter your interests separated by commas "
        "(or type 'exit'): "
    )

    if user_input.lower() == "exit":
        print("\nThank you for using the recommendation system!")
        break

    if not user_input.strip():
        print("Please enter at least one interest.")
        continue

    # Convert input into a set
    user_interests = {
        clean_text(interest)
        for interest in user_input.split(",")
        if clean_text(interest)
    }

    # Get recommendations
    recommendations = recommend(user_interests)

    print("\n" + "=" * 55)
    print("                 RECOMMENDATIONS")
    print("=" * 55)

    for number, item in enumerate(recommendations, start=1):

        print(f"\n{number}. {item['name']}")
        print(f"   Category: {item['category']}")
        print(f"   Similarity: {item['score'] * 100:.2f}%")

        if item["matched"]:
            print(
                "   Matched interests:",
                ", ".join(sorted(item["matched"]))
            )
        else:
            print("   Matched interests: None")

    print("=" * 55)