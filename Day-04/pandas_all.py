import pandas as pd

# Create DataFrame
data = {
    "Name": ["Manoj", "Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "Branch": ["ECE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Python": [85, 92, 76, 65, 88, 72],
    "SQL": [78, 85, 82, 70, 91, 68],
    "ML": [72, 90, 68, 60, 84, 75],
    "Attendance": [88, 95, 80, 72, 93, 85]
}

df = pd.DataFrame(data)

# 1. Display complete DataFrame
print("\n1. Complete DataFrame:")
print(df)


# 2. Display Name, Python and ML
print(df[["Name", "Python", "ML"]])


# 3. Students with Python > 80
print("\n3. Python > 80:")
print(df[df["Python"] > 80])


# 4. Students with Attendance >= 85
print("\n4. Attendance >= 85:")
print(df[df["Attendance"] >= 85])


# 5. Create Average column
df["Average"] = df[["Python", "SQL", "ML"]].mean(axis=1)

print("\n5. Average column:")
print(df)


# 7. Average Python score
print("\n7. Average Python score:")
print(df["Python"].mean())


# 8. Average ML score for each branch
print("\n8. Average ML score by Branch:")
print(df.groupby("Branch")["ML"].mean())


# 9. Sort by Average highest to lowest
print("\n9. Sorted by Average:")
print(df.sort_values("Average", ascending=False))


# 10. Python > 80 AND ML > 75
print("\n10. Python > 80 AND ML > 75:")
print(df[(df["Python"] > 80) & (df["ML"] > 75)])


# 11. Number of students in each branch
print("\n11. Number of students in each Branch:")
print(df["Branch"].value_counts())


# 12. Student with lowest attendance
print("\n12. Student with lowest Attendance:")
print(df.loc[df["Attendance"].idxmin()])


# 13. Create Status column
def get_status(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    else:
        return "Needs Improvement"


df["Status"] = df["Average"].apply(get_status)

print("\n13. Status:")
print(df)


# 14. Display Name, Branch, Average, Status
print("\n14. Final result:")
print(df[["Name", "Branch", "Average", "Status"]])


# BONUS: Top 2 students from each branch
top_2 = (
    df.sort_values(["Branch", "Average"], ascending=[True, False])
      .groupby("Branch")
      .head(2)
)

print("\nBONUS: Top 2 students from each Branch:")
print(top_2[["Name", "Branch", "Average"]])