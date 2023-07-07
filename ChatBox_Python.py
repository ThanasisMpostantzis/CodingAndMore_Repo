#Το Παρακάτω πρόγραμμα είναι η υλοποίηση ενός ChatBox στην Python

import re
import random

patterns = {
    r'Γεια σου': ['Γεια σου!'],
    r'Πώς είσαι;': ['Είμαι καλά, ευχαριστώ.'],
    r'Τι κάνεις;': ['Πίνω καφέ, εσυ;'],
    r'Πώς σε λένε;': ['Με λένε ChatBot, εσένα;'],
    r'Τι ώρα είναι;': ['Δεν το γνωρίζω μπορείς να κοιτάξεις το κινητό σου.'],
    r'Πού μένεις;' : ['Δεν έχω φυσική τοποθεσία, είμαι απλώς ένα πρόγραμμα.'],
    r'Ποια είναι η αγαπημένη σου τροφή;': ['Δεν έχω δυνατότητα να φάω, είμαι απλώς ένα AI!'],
    r'Τι μπορείς να κάνεις;': ['Μπορώ να απαντήσω σε ερωτήσεις και να παρέχω πληροφορίες.'],
    r'Μπορείς να με βοηθήσεις με ένα πρόβλημα;': ['Φυσικά! Πες μου το πρόβλημά σου και θα προσπαθήσω να βοηθήσω.'],
    r'Ποια είναι η ημερομηνία;': ['Η τρέχουσα ημερομηνία είναι 6 Ιουλίου 2023.'],
    r'Ποια είναι η ώρα;': ['Δεν έχω πρόσβαση σε ρολόι, αλλά μπορείς να τσεκάρεις την ώρα στον υπολογιστή σου.'],
    r'Τι είναι η τεχνητή νοημοσύνη;': ['Η τεχνητή νοημοσύνη είναι ένα πεδίο της επιστήμης που ασχολείται με το σχεδιασμό και την ανάπτυξη υπολογιστικών συστημάτων που μπορούν να εκτελούν εργασίες που απαιτούν ανθρώπινη νοημοσύνη.'],
    r'Ποια είναι η πρωτεύουσα της Ελλάδας;': ['Η πρωτεύουσα της Ελλάδας είναι η Αθήνα.'],
    r'Πόσα χρόνια έχεις;': ['Ως AI μοντέλο, δεν έχω έννοια της ηλικίας.'],
    r'Τι είναι η Python;': ['Η Python είναι μια δημοφιλής γλώσσα προγραμματισμού υψηλού επιπέδου.'],
    r'Ποια είναι η πιο δημοφιλής γλώσσα προγραμματισμού;': ['Δεν μπορώ να απαντήσω με σιγουριά, αλλά η Python είναι αρκετά δημοφιλής.'],
    r'Ποιο είναι το μεγαλύτερο κτίριο στον κόσμο;': ['Το μεγαλύτερο κτίριο στον κόσμο είναι ο Πύργος του Ντουμπάι.'],
    r'Ποιος είναι ο πρόεδρος των Ηνωμένων Πολιτειών;': ['Ο πρόεδρος των Ηνωμένων Πολιτειών είναι ο Τζο Μπάιντεν.'],
    r'Ποια είναι η χώρα με τον περισσότερο πληθυσμό στον κόσμο;': ['Η Κίνα έχει τον μεγαλύτερο πληθυσμό ανάμεσα στις χώρες του κόσμου.'],
    r'Ποιο είναι το μεγαλύτερο ποτάμι στον κόσμο;': ['Το Αμαζόνιο είναι το μεγαλύτερο ποτάμι στον κόσμο.'],
    r'Τι είναι η κλιματική αλλαγή;': ['Η κλιματική αλλαγή αναφέρεται στη μακροπρόθεσμη αλλαγή του κλίματος της Γης λόγω ανθρωπογενών δραστηριοτήτων.'],
    r'Ποιο είναι το πιο δημοφιλές άθλημα στον κόσμο;': ['Ο ποδόσφαιρος είναι το πιο δημοφιλές άθλημα στον κόσμο.']
}  

while True:
    found = False
    user = input("Ρώτησε με κάτι: ")
    for pattern, responses in patterns.items():
        m = re.match(pattern, user)
        if m:
            print(random.choice(responses))
            found = True
            break
    if not found:
        print("Μήπως μπορείς να με ρωτήσεις κάτι άλλο;;")
