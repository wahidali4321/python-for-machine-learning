import matplotlib.pyplot as plt

scores = [78, 82, 65, 90, 88, 70, 72, 95, 60, 84,
          76, 89, 91, 68, 73, 85, 79, 81, 67, 93]

count, bins, patches = plt.hist(
    scores,
    bins=8,
    edgecolor="black"
)

print("Histogram Count:", count)
print("Bin Edges:", bins)

plt.title("Histogram of Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()