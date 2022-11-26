import numpy as np
np.set_printoptions(precision=3, suppress=False, threshold=np.inf)

# ---------------------------------------------------------------------
# Number of criteria to evaluate.
# ---------------------------------------------------------------------
while True:
    try:
        num = int(input("Insert number of criteria (min:3, max:10): "))
        if num < 3 or num > 10:
            print("Number of criteria must be an integer number between 2 and 10.")
        else:
            break
    except ValueError:
        print("Number of criteria must be an integer number between 2 and 10.")
        pass

print("Your analysis contains " + str(num) + " criteria")

# ---------------------------------------------------------------------
# Definition of criteria 's names.
# ---------------------------------------------------------------------
criteria_names = list()
g = 1
while g <= num:
    criterion_name = input("Enter criterion " + str(g) + " name: ")
    if not criterion_name:
        print("Please use a name for your criterion!")
        continue
    criteria_names.append(criterion_name)
    g = g + 1

counter = 0
while counter < len(criteria_names):
    for criterion in criteria_names:
        print("Criterion " + str(counter + 1) + " is: " + str(criterion))
        counter = counter + 1
# ---------------------------------------------------------------------
# Number of pairwise comparisons.
# ---------------------------------------------------------------------
comparisons = int(num * (num-1)/2)
print("There will be " + str(comparisons) + " pairwise comparison(s) in this problem. ")

# ---------------------------------------------------------------------
# Define relative preferences over the criteria.
# ---------------------------------------------------------------------
# Number of criteria >=2. Comparisons for matrix's first row are n-1.
preferences = list()
for i in range(1, num):
    while True:
        try:
            pref = int(input("Enter preference of criterion 1 over criterion " + str(i+1) + ": "))
            if pref < 1 or pref > 9:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
            else:
                preferences.append(pref)
                break
        except ValueError:
            print("Your preference must be an integer number between 1-9 according to Saaty's scale")
            pass

# Number of criteria >=3. Comparisons for matrix's second row are n-2.
preferences2 = list()
if num >= 3:
    for comp in range(1, num - 2 + 1):
        while True:
            try:
                pref2 = int(input("Enter preference of criterion 2 over criterion " + str(comp+2) + ": "))
                if pref2 < 1 or pref2 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences2.append(pref2)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")

                pass

# Number of criteria >=4. Comparisons for matrix's third row are n-3.
preferences3 = list()
if num >= 4:
    for comp in range(1, num - 3 + 1):
        while True:
            try:
                pref3 = int(input("Enter preference of criterion 3 over criterion " + str(comp+3) + ": "))
                if pref3 < 1 or pref3 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences3.append(pref3)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass
# Number of criteria >=5. Comparisons for matrix's fourth row are n-4.
preferences4 = list()
if num >= 5:
    for comp in range(1, num - 4 + 1):
        while True:
            try:
                pref4 = int(input("Enter preference of criterion 4 over criterion " + str(comp+4) + ": "))
                if pref4 < 1 or pref4 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences4.append(pref4)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

# Number of criteria >=6. Comparisons for matrix's fifth row are n-5.
preferences5 = list()
if num >= 6:
    for comp in range(1, num - 5 + 1):
        while True:
            try:
                pref5 = int(input("Enter preference of criterion 5 over criterion " + str(comp+5) + ": "))
                if pref5 < 1 or pref5 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences5.append(pref5)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

# Number of criteria >=7. Comparisons for matrix's fifth row are n-6.
preferences6 = list()
if num >= 7:
    for comp in range(1, num - 6 + 1):
        while True:
            try:
                pref6 = int(input("Enter preference of criterion 6 over criterion " + str(comp+6) + ": "))
                if pref6 < 1 or pref6 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences6.append(pref6)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

# Number of criteria >=8. Comparisons for matrix's fifth row are n-7.
preferences7 = list()
if num >= 8:
    for comp in range(1, num - 7 + 1):
        while True:
            try:
                pref7 = int(input("Enter preference of criterion 7 over criterion " + str(comp+7) + ": "))
                if pref7 < 1 or pref7 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences7.append(pref7)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

# Number of criteria >=9. Comparisons for matrix's fifth row are n-8.
preferences8 = list()
if num >= 9:
    for comp in range(1, num - 8 + 1):
        while True:
            try:
                pref8 = int(input("Enter preference of criterion 8 over criterion " + str(comp+8) + ": "))
                if pref8 < 1 or pref8 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences8.append(pref8)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

# Number of criteria >=10. Comparisons for matrix's fifth row are n-9.
preferences9 = list()
if num == 10:
    for comp in range(1, num - 9 + 1):
        while True:
            try:
                pref9 = int(input("Enter preference of criterion 9 over criterion " + str(comp+9) + ": "))
                if pref9 < 1 or pref9 > 9:
                    print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                else:
                    preferences9.append(pref9)
                    break
            except ValueError:
                print("Your preference must be an integer number between 1-9 according to Saaty's scale")
                pass

a = np.ones([num, num], dtype=float)

# ____________________________________________________________
# Matching the preferences with the comparison matrix values.
# ------------------------------------------------------------
# For 2 criteria
a[0, 1] = preferences[0]
a[1, 0] = 1/preferences[0]

if num >= 3:
    a[0, 2] = preferences[1]
    a[2, 0] = 1/preferences[1]
    a[1, 2] = preferences2[0]
    a[2, 1] = 1/preferences2[0]

if num >= 4:
    a[0, 3] = preferences[2]
    a[3, 0] = 1/preferences[2]
    a[1, 3] = preferences2[1]
    a[3, 1] = 1/preferences2[1]
    a[2, 3] = preferences3[0]
    a[3, 2] = 1/preferences3[0]

if num >= 5:
    a[0, 4] = preferences[3]
    a[4, 0] = 1/preferences[3]
    a[1, 4] = preferences2[2]
    a[4, 1] = 1/preferences2[2]
    a[2, 4] = preferences3[1]
    a[4, 2] = 1/preferences3[1]
    a[3, 4] = preferences4[0]
    a[4, 3] = 1/preferences4[0]

if num >= 6:
    a[0, 5] = preferences[4]
    a[5, 0] = 1/preferences[4]
    a[1, 5] = preferences2[3]
    a[5, 1] = 1/preferences2[3]
    a[2, 5] = preferences3[2]
    a[5, 2] = 1/preferences3[2]
    a[3, 5] = preferences4[1]
    a[5, 3] = 1/preferences4[1]
    a[4, 5] = preferences5[0]
    a[5, 4] = 1/preferences5[0]

if num >= 7:
    a[0, 6] = preferences[5]
    a[6, 0] = 1/preferences[5]
    a[1, 6] = preferences2[4]
    a[6, 1] = 1/preferences2[4]
    a[2, 6] = preferences3[3]
    a[6, 2] = 1/preferences3[3]
    a[3, 6] = preferences4[2]
    a[6, 3] = 1 / preferences4[2]
    a[4, 6] = preferences5[1]
    a[6, 4] = 1 / preferences5[1]
    a[5, 6] = preferences6[0]
    a[6, 5] = 1/preferences6[0]

if num >= 8:
    a[0, 7] = preferences[6]
    a[7, 0] = 1/preferences[6]
    a[1, 7] = preferences2[5]
    a[7, 1] = 1/preferences2[5]
    a[2, 7] = preferences3[4]
    a[7, 2] = 1/preferences3[4]
    a[3, 7] = preferences4[3]
    a[7, 3] = 1 / preferences4[3]
    a[4, 7] = preferences5[2]
    a[7, 4] = 1 / preferences5[2]
    a[5, 7] = preferences6[1]
    a[7, 5] = 1/preferences6[1]
    a[6, 7] = preferences7[0]
    a[7, 6] = 1/preferences7[0]

if num >= 9:
    a[0, 8] = preferences[7]
    a[8, 0] = 1/preferences[7]
    a[1, 8] = preferences2[6]
    a[8, 1] = 1/preferences2[6]
    a[2, 8] = preferences3[5]
    a[8, 2] = 1/preferences3[5]
    a[3, 8] = preferences4[4]
    a[8, 3] = 1 / preferences4[4]
    a[4, 8] = preferences5[3]
    a[8, 4] = 1 / preferences5[3]
    a[5, 8] = preferences6[2]
    a[8, 5] = 1/preferences6[2]
    a[6, 8] = preferences7[1]
    a[8, 6] = 1/preferences7[1]
    a[7, 8] = preferences8[0]
    a[8, 7] = 1/preferences8[0]

if num == 10:
    a[0, 9] = preferences[8]
    a[9, 0] = 1/preferences[8]
    a[1, 9] = preferences2[7]
    a[9, 1] = 1/preferences2[7]
    a[2, 9] = preferences3[6]
    a[9, 2] = 1/preferences3[6]
    a[3, 9] = preferences4[5]
    a[9, 3] = 1 / preferences4[5]
    a[4, 9] = preferences5[4]
    a[9, 4] = 1 / preferences5[4]
    a[5, 9] = preferences6[3]
    a[9, 5] = 1/preferences6[3]
    a[6, 9] = preferences7[2]
    a[9, 6] = 1/preferences7[2]
    a[7, 9] = preferences8[1]
    a[9, 7] = 1/preferences8[1]
    a[8, 9] = preferences9[0]
    a[9, 8] = 1/preferences9[0]

print("Your comparison matrix is: \n" + str(a))

norm_a = a.copy()

# -------------------------------------------------
# Calculate sums of each column of the comparison matrix and then normalize the matrix
# -------------------------------------------------
# Sum of first column
sum0 = sum(norm_a[:, 0])
# Normalization  of first column
norm_a[:, 0] = norm_a[:, 0]/sum0

# Sum of second column
sum1 = sum(norm_a[:, 1])
# Normalization  of second column
norm_a[:, 1] = norm_a[:, 1]/sum1

# Sum and Normalization of third column
if num >= 3:
    sum2 = sum(norm_a[:, 2])
    norm_a[:, 2] = norm_a[:, 2]/sum2

# Sum and Normalization of fourth column
if num >= 4:
    sum3 = sum(norm_a[:, 3])
    norm_a[:, 3] = norm_a[:, 3] / sum3

# Sum and Normalization of fifth column
if num >= 5:
    sum4 = sum(norm_a[:, 4])
    norm_a[:, 4] = norm_a[:, 4] / sum4

# Sum and Normalization of sixth column
if num >= 6:
    sum5 = sum(norm_a[:, 5])
    norm_a[:, 5] = norm_a[:, 5] / sum5

# Sum and Normalization of seventh column
if num >= 7:
    sum6 = sum(norm_a[:, 6])
    norm_a[:, 6] = norm_a[:, 6] / sum6

# Sum and Normalization of eightieth column
if num >= 8:
    sum7 = sum(norm_a[:, 7])
    norm_a[:, 7] = norm_a[:, 7] / sum7

# Sum and Normalization of ninth column
if num >= 9:
    sum8 = sum(norm_a[:, 8])
    norm_a[:, 8] = norm_a[:, 8] / sum8

# Sum and Normalization of tenth column
if num == 10:
    sum9 = sum(norm_a[:, 9])
    norm_a[:, 9] = norm_a[:, 9] / sum9

# -----------------------------------------------------------------
# Calculate the eigenvector of the matrix.
# -----------------------------------------------------------------

eigenvector = np.ones((num, 1), dtype=float)
eigenvector[0] = sum(norm_a[0, :])/num
eigenvector[1] = sum(norm_a[1, :])/num

if num >= 3:
    eigenvector[2] = sum(norm_a[2, :]) / num
if num >= 4:
    eigenvector[3] = sum(norm_a[3, :]) / num
if num >= 5:
    eigenvector[4] = sum(norm_a[4, :]) / num
if num >= 6:
    eigenvector[5] = sum(norm_a[5, :]) / num
if num >= 7:
    eigenvector[6] = sum(norm_a[6, :]) / num
if num >= 8:
    eigenvector[7] = sum(norm_a[7, :]) / num
if num >= 9:
    eigenvector[8] = sum(norm_a[8, :]) / num
if num == 10:
    eigenvector[9] = sum(norm_a[9, :]) / num

print("The eigenvector of the matrix is: \n" + str(eigenvector))

# -----------------------------------------------------------------
# Calculate max eigenvalue of the matrix.
# -----------------------------------------------------------------
# Multiply the comparison matrix by the eigenvector.

matrix_b = np.dot(a, eigenvector)

# First approach of max eigenvalue estimation.
max_eigenvalue1 = sum(matrix_b[:, 0])

print("First approach of eigenvalue computation: \n λmax = " + str(max_eigenvalue1))

# Second approach of max eigenvalue estimation.
matrix_b2 = matrix_b / eigenvector

max_eigenvalue2 = sum(matrix_b2[:, 0]) / num

print("Second approach of eigenvalue computation: \n λmax = " + str(max_eigenvalue2))

# -----------------------------------------------------------------
# Consistency calculation
# -----------------------------------------------------------------

# Consistency Index calculation

ci = (max_eigenvalue2 - num) / (num - 1)
print("Consistency Index (C.I.) = " + str(ci))

# Random Index values can be found in literature tables
ri = 0

if num == 3:
    ri = 0.52

if num == 4:
    ri = 0.89

if num == 5:
    ri = 1.11

if num == 6:
    ri = 1.25

if num == 7:
    ri = 1.35

if num == 8:
    ri = 1.4

if num == 9:
    ri = 1.45

if num == 10:
    ri = 1.49

print("Random Index (R.I.) = " + str(ri))

# Consistency Ratio calculation

cr = ci / ri

print("Consistency Ratio (C.R.) = " + str(cr))

if cr < 0.1:
    print("C.R. < 0.1. Good job on your judgements! The Relative Importance Weights (RIW) for the criteria are:")
    for i in range(1, num + 1):
        print("RIW of criterion " + str(i) + " is: " + str(float(eigenvector[i-1])))
else:
    print("C.R. > 0.1. You should reconsider your pairwise comparison judgements!")
