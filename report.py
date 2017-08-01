# 1. What are the most popular three articles of all time ?
#
# Which articles have been accessed the most?
# Present this information as a sorted list with the most popular
# article at the top.
#
# (ex)
# "Princess Shellfish Marries Prince Handsome" — 1201 views
# "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
# "Political Scandal Ends In Political Scandal" — 553 views

# 2. Who are the most popular article authors of all time?
#
# When you sum up all of the articles each author has written,
# which authors get the most page views?
# Present this as as sorted list with the most popular author at the top.
#
# (ex)
# Ursula La Multa — 2304 views
# Rudolf von Treppenwitz — 1985 views
# Markoff Chaney — 1723 views
# Anonymous Contributor — 1023 views

# 3. On which days did more than 1% of requests lead to errors?
#
# The log table includes a column status that indicates the HTTP status
# code that the news site sent to the user's browser.
#
# (ex)
# July 29, 2016 — 2.5% errors

import psycopg2
