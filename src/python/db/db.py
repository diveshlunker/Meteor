class DB:
    def __init__(self):
        pass


class Firebase(DB):
    def __init__(self):
        pass

    def initialize_db(self):
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate("C:\\Users\\ndive\\OneDrive\\Desktop\\serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

        # Initialize Firestore client
        self.db = firestore.client()

    def add_data_to_db(self, product_details):
        for product in product_details:
            data = vars(product)
            # if data["should_display"]:
            doc_ref = self.db.collection(u'sankeshwarasupermarket5').document(data["barcode"])
            doc_ref.set(data)

        print("Data added successfully!")
