import datetime as _dt
import hashlib as _hashlib
import json as _json
from uuid import uuid4  # For generating unique identifiers for NFTs
import os  # Importing os module for file operations

class LicenseChain:
    def __init__(self):
        self.chain = []
        self.issued_licenses = set()
        self.issued_nfts = set()

        # Load existing issued licenses and NFTs from file
        self._load_issued_data()

        # Create genesis block with initial data
        initial_block = self._create_block(
            nft_id="genesis_nft", license_key_hash=self._hash_key("genesis_license"), proof=1, previous_hash="0",
            index=1, software_id="", user_id="", metadata={}
        )
        self.chain.append(initial_block)

    def _load_issued_data(self):
        if os.path.exists('issued_data.json'):
            with open('issued_data.json', 'r') as file:
                data = _json.load(file)
                self.issued_licenses = set(data.get('issued_licenses', []))
                self.issued_nfts = set(data.get('issued_nfts', []))

    def _save_issued_data(self):
        data = {
            'issued_licenses': list(self.issued_licenses),
            'issued_nfts': list(self.issued_nfts)
        }
        with open('issued_data.json', 'w') as file:
            _json.dump(data, file)

    def _hash_key(self, license_key: str) -> str:
        """
        Hash the license key using SHA-256 and return the hash.
        """
        return _hashlib.sha256(license_key.encode()).hexdigest()

    def mint_nft(self, license_key: str, software_id: str, user_id: str, metadata: dict) -> dict:
        """
        Add a new NFT block to the blockchain after validating the proof of work.
        """
        # Hash the license key
        license_key_hash = self._hash_key(license_key)

        # Check if the license key hash has already been issued
        if license_key_hash in self.issued_licenses:
            raise ValueError(f"License key '{license_key}' has already been issued.")

        # Get the last block in the chain
        previous_block = self.get_previous_block()
        previous_proof = previous_block["proof"]
        index = len(self.chain) + 1
        
        # Proof of work for new block
        proof = self._proof_of_work(
            previous_proof=previous_proof, index=index, license_key=license_key
        )
        previous_hash = self._hash(block=previous_block)
        
        # Generate a unique NFT ID
        nft_id = str(uuid4())
        
        # Create new block with NFT info
        block = self._create_block(
            nft_id=nft_id, license_key_hash=license_key_hash, proof=proof, previous_hash=previous_hash,
            index=index, software_id=software_id, user_id=user_id, metadata=metadata
        )
        self.chain.append(block)

        # Add the issued license key hash and NFT ID to the sets
        self.issued_licenses.add(license_key_hash)
        self.issued_nfts.add(nft_id)

        # Save issued licenses and NFTs
        self._save_issued_data()

        return block

    def _create_block(
        self, nft_id: str, license_key_hash: str, proof: int, previous_hash: str, index: int,
        software_id: str, user_id: str, metadata: dict
    ) -> dict:
        """
        Create a new block with the NFT information and other metadata.
        """
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "nft_id": nft_id,
            "license_key_hash": license_key_hash,
            "software_id": software_id,
            "user_id": user_id,
            "proof": proof,
            "previous_hash": previous_hash,
            "metadata": metadata
        }
        return block

    def get_previous_block(self) -> dict:
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def _to_digest(
        self, new_proof: int, previous_proof: int, index: int, license_key: str
    ) -> bytes:
        """
        Generate a digest to be hashed, including the new proof of work and license key.
        """
        to_digest = str(new_proof ** 2 - previous_proof ** 2 + index) + self._hash_key(license_key)
        return to_digest.encode()

    def _proof_of_work(self, previous_proof: int, index: int, license_key: str) -> int:
        """
        Perform proof of work to find a valid proof that satisfies the hash condition.
        """
        new_proof = 1
        check_proof = False

        while not check_proof:
            to_digest = self._to_digest(new_proof, previous_proof, index, license_key)
            hash_operation = _hashlib.sha256(to_digest).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def _hash(self, block: dict) -> str:
        """
        Hash a block and return the cryptographic hash of the block.
        """
        encoded_block = _json.dumps(block, sort_keys=True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        """
        Check the validity of the blockchain by verifying hashes and proof of work.
        """
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block["previous_hash"] != self._hash(previous_block):
                return False

            previous_proof = previous_block["proof"]
            index, license_key_hash, proof = block["index"], block["license_key_hash"], block["proof"]
            hash_operation = _hashlib.sha256(
                self._to_digest(
                    new_proof=proof,
                    previous_proof=previous_proof,
                    index=index,
                    license_key=license_key_hash  # Use hashed license key
                )
            ).hexdigest()

            if hash_operation[:4] != "0000":
                return False

            previous_block = block
            block_index += 1

        return True

    def is_license_valid(self, license_key: str, software_id: str, user_id: str) -> bool:
        """
        Validate if a given license key exists and matches the provided software and user ID.
        """
        license_key_hash = self._hash_key(license_key)
        for block in self.chain:
            if (
                block["license_key_hash"] == license_key_hash
                and block["software_id"] == software_id
                and block["user_id"] == user_id
            ):
                return True
        return False

    def get_license_details(self, license_key: str) -> dict:
        """
        Retrieve details of a specific license key from the blockchain.
        """
        license_key_hash = self._hash_key(license_key)
        for block in self.chain:
            if block["license_key_hash"] == license_key_hash:
                return {
                    "nft_id": block["nft_id"],
                    "software_id": block["software_id"],
                    "user_id": block["user_id"],
                    "metadata": block["metadata"]
                }
        return {}

    def get_chain(self) -> list:
        """
        Return the entire blockchain for reference.
        """
        return self.chain
