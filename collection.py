# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

#added close '}'

for author, date in authors.items():
    print ("%s" % authors + " died in " + "%s." % date)
    
#added open and closed parentheses after print
#removed '{}' added "()"
#, added after author
    
