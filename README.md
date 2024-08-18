# LicenseChain - Blockchain-Based License Verification System

**LicenseChain** is a blockchain-based solution for secure license management and verification, implemented entirely in Python. This system allows software vendors to issue and manage licenses using a custom blockchain ledger. It incorporates NFT (Non-Fungible Token) technology to uniquely represent each license, enhancing traceability and preventing duplicate or fraudulent licenses.

## Features

- **Blockchain-Based License Management**: LicenseChain uses a blockchain ledger to store and manage software licenses, ensuring immutability and security.
  
- **NFT Minting for Licenses**: Each license is uniquely represented as an NFT, providing a secure, non-replicable, and traceable digital asset for software licenses.
  
- **License Validation**: Software licenses can be verified against the blockchain, ensuring the license's authenticity for a specific user and software.

- **Proof of Work**: The blockchain incorporates a proof-of-work mechanism to maintain security and ensure integrity across the system.

- **Data Persistence**: LicenseChain stores issued licenses and NFTs in a JSON file (`issued_data.json`) to ensure that licenses are preserved even after a restart.

- **Genesis Block**: The system automatically generates a genesis block upon initialization, which serves as the starting point for the blockchain.

## Key Concepts

### 1. **Minting a License (NFT)**
The system allows the minting of a new license NFT when a valid software license is issued. Each NFT is uniquely tied to the license key, user ID, software ID, and metadata, and this NFT is recorded on the blockchain.

### 2. **Proof of Work**
The blockchain uses a proof-of-work mechanism where computational work is performed to create new blocks. This ensures the security of the blockchain and protects it from malicious actors.

### 3. **Validation of Licenses**
LicenseChain enables license validation by checking if the software license exists in the blockchain and if it matches the provided software ID and user ID. This helps prevent piracy or unauthorized use of software.

### 4. **Data Persistence**
Issued licenses and NFTs are saved in a JSON file (`issued_data.json`). This ensures that even if the system restarts, the data about issued licenses and NFTs will persist.

## How It Works

1. **Minting a License**: 
   - Generate a new NFT representing the license.
   - The NFT is minted using a unique `license_key`, `software_id`, `user_id`, and additional metadata.
   - This new block is added to the blockchain, ensuring the license is secure and traceable.

2. **Validating a License**: 
   - The system checks if a given license key exists for a specific user and software.
   - A cryptographic hash of the license key is compared against stored data in the blockchain to confirm its authenticity.

3. **Blockchain Integrity**: 
   - Each block contains a cryptographic hash of the previous block, ensuring that the chain is immutable. 
   - The system verifies that the blockchain has not been tampered with by checking hashes and proof-of-work across all blocks.

## Code Structure

- **LicenseChain Class**: Implements the core functionality of the blockchain and license management system.
- **Minting and Validation**: Methods to mint new NFTs (licenses) and validate existing ones.
- **Proof of Work**: A simplified consensus mechanism to ensure blockchain integrity.
- **Data Persistence**: Methods to load and save issued licenses and NFTs to/from the file system.

## Example Usage

```python
# Initialize the LicenseChain
license_chain = LicenseChain()

# Mint a new license NFT
metadata = {"product_version": "1.0", "expiry_date": "2025-12-31"}
new_nft = license_chain.mint_nft(license_key="ABC-123-XYZ", software_id="SFT-001", user_id="USER123", metadata=metadata)
print("New License NFT Minted:", new_nft)

# Validate a license
is_valid = license_chain.is_license_valid(license_key="ABC-123-XYZ", software_id="SFT-001", user_id="USER123")
print("Is the License Valid?", is_valid)

# Get license details
details = license_chain.get_license_details(license_key="ABC-123-XYZ")
print("License Details:", details)

# Check if blockchain is valid
is_chain_valid = license_chain.is_chain_valid()
print("Is the Blockchain Valid?", is_chain_valid)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LicenseChain.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LicenseChain
   ```
3. Run the Python script:
   ```bash
   python license_chain.py
   ```

## Future Improvements

- **Integration with Frontend**: Implement a web interface for users to manage and verify licenses easily.
- **Support for Multiple Proof Mechanisms**: Add support for different consensus algorithms to enhance security.
- **Interoperability with Smart Contracts**: Explore the potential for integrating with Ethereum or other blockchain platforms for smart contract functionality.

## Contributing

Contributions to LicenseChain are welcome! Feel free to fork the repository and submit pull requests for new features or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you need more adjustments!
