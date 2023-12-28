line = input("Enter a line :")
sub_string = input("Enter a sub string :")
sub_counts = 0
for i in line:
    if(sub_string in line):
        sub_counts += 1
print(sub_counts)


