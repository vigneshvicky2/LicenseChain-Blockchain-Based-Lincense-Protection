# LicenseChain - Blockchain-based License Management System

LicenseChain is a blockchain-powered solution designed for managing and verifying software licenses. This system ensures that software licenses are securely issued and validated, leveraging blockchain’s immutable nature. The project is built using Python for the blockchain backend and includes a front-end for users and admins to interact with the system seamlessly.

## Features

- **Blockchain-Based License Management**: Secure issuance and validation of software licenses using a blockchain ledger.
- **NFT Minting for Licenses**: Each issued license is represented as a unique NFT (Non-Fungible Token) on the blockchain, ensuring immutability and traceability.
- **License Validation**: Verify license authenticity using a blockchain-verified process.
- **License Details Retrieval**: Fetch details of any issued license using the provided license key.
- **User-Friendly Front-End**: A fully functional front-end for users and administrators to interact with the system, manage licenses, and view blockchain data.
- **Persistent Storage**: Issued licenses and NFTs are stored in a JSON file for persistence.
- **Proof of Work**: The system includes a simple proof-of-work mechanism for block validation.

## Technology Stack

### Backend:
- **Python**: Core logic for blockchain, NFT minting, and license management.
- **Hashlib**: Used for hashing license keys and blocks in the blockchain.
- **Datetime**: For timestamping blocks.
- **JSON**: Storing blockchain and license data.
- **UUID**: Generating unique identifiers for NFTs.

### Front-End:
- **React.js**: A modern and responsive front-end for user interaction with the blockchain.
- **Node.js & Express**: Backend framework supporting API calls from the front-end.
- **HTML/CSS/JavaScript**: For the structure, style, and dynamic behavior of the front-end.
  
## How It Works

1. **Minting a License (NFT)**:
    - Input a license key, software ID, and user ID.
    - The backend hashes the license key and mints an NFT representing the license.
    - The new block with the NFT and license details is added to the blockchain.

2. **Validating a License**:
    - Enter the license key, software ID, and user ID.
    - The backend verifies the authenticity of the license by checking the blockchain.

3. **Fetching License Details**:
    - Enter a license key to retrieve the associated NFT and metadata from the blockchain.

## Front-End Interaction

The front-end provides an intuitive interface for both administrators and users:
- **Admin Panel**: 
    - Mint new licenses (NFTs) for software.
    - View the blockchain's current state.
- **User Panel**: 
    - Validate software licenses by providing the necessary credentials.
    - View the details of any valid license.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vigneshvicky2/LicenseChain-Blockchain-Based-Lincense-Protection.git
    cd LicenseChain-Blockchain-Based-Lincense-Protection
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **To Run**:
    ```bash
    python app.py
    ```

## Usage

### Minting a New License
1. Go to the admin panel.
2. Enter the license key, software ID, and user ID.
3. Click "Mint License". The system will generate an NFT and store the license on the blockchain.

### Validating a License
1. Go to the user panel.
2. Enter the license key, software ID, and user ID.
3. Click "Validate License" to verify its authenticity.

### Fetching License Details
1. Enter the license key in the user panel.
2. Click "Get License Details" to retrieve the associated NFT and metadata.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
