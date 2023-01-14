child_age = 2
required_age_for_schooling = 5

# question: can a child go to school?

if child_age == required_age_for_schooling:
    print ("Congratulations! Your child can join the school.")
elif child_age > required_age_for_schooling:
    print("Your child should join the higher secondary school.")
elif child_age <= 2:
    print("Your child is a baby, please take care of your baby.")
else:
    print("Your child can not go to school")