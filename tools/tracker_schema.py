"""The tracker's tabs and columns, shared by the spreadsheet tools.

The artifact tracker uses the same collection and field names.
Plain-language descriptions of every column are in shared/tracker-columns.md.
"""

COLUMNS = {
    "companies": ["id", "company", "careersSite", "tier", "industry", "keepAnyway", "onHold", "added"],
    "coverage": ["id", "company", "industry", "sweepDate", "sweepState", "result", "detail", "skipped", "sweepProgress"],
    "listings": ["id", "company", "title", "location", "url", "reqId", "industry", "track", "family", "posted",
                 "pay", "why", "teaches", "priority", "status", "appliedDate", "postingText", "reviewReason",
                 "history", "yourNotes", "managerName", "managerTitle", "howIdentified", "confidence",
                 "profileUrl", "emailOrFormat", "connectionNote", "longMessage"],
    "answers": ["id", "topic", "question", "answer", "useWhen", "updated"],
    "settings": ["id", "tierA", "tierB", "tierC", "industryOrder", "excludedIndustries", "roleFamilies",
                 "tracks", "priorities"],
}

DEFAULT_SETTINGS = {
    "id": "main",
    "tierA": "Employer based in my home metro",
    "tierB": "Employer elsewhere with jobs open to my area",
    "tierC": "Other allowed place",
    "industryOrder": "",
    "excludedIndustries": "",
    "roleFamilies": "",
    "tracks": "Main",
    "priorities": "High; Medium; Low; On hold",
}

CHOICES = {
    ("companies", "tier"): ["A", "B", "C"],
    ("companies", "keepAnyway"): ["yes", "no"],
    ("companies", "onHold"): ["yes", "no"],
    ("coverage", "sweepState"): ["done", "partial", "not swept", "manual"],
    ("coverage", "result"): ["HIT", "NONE", "LEAD", "PENDING"],
    ("listings", "priority"): ["High", "Medium", "Low", "On hold"],
    ("listings", "status"): ["To apply", "Applied", "Followed up", "Interview", "Offer", "Review fit",
                             "On hold", "Rejected", "Closed", "expired", "filled"],
    ("listings", "confidence"): ["high", "medium", "low"],
    ("answers", "topic"): ["Contact", "Work history", "Education", "Pay", "Voluntary", "References", "Links",
                           "Work authorization", "Account", "Other"],
}

# Columns only the user writes. Tools refuse to write them.
USER_ONLY = {("listings", "yourNotes")}
# Columns that may only be appended to.
APPEND_ONLY = {("listings", "history")}
