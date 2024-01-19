from app import mongo

class Blockchain:

    @staticmethod
    def add_blockchain(name, status, height):
        blockchain_data = {
            "name": name,
            "status": status,
            "height": height
        }
        mongo.db.blockchains.insert_one(blockchain_data)

    @staticmethod
    def get_blockchains():
        blockchains = mongo.db.blockchains.find()
        result = []
        for blockchain in blockchains:
            result.append({
                'name': blockchain['name'],
                'status': blockchain['status'],
                'height': blockchain['height']
            })
        return result
