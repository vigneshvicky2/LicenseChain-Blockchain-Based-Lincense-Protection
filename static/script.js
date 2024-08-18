async function createBlock() {
    const licenseKey = document.getElementById('license_key').value;
    const softwareId = document.getElementById('software_id').value;
    const userId = document.getElementById('user_id').value;
    const metadata = document.getElementById('metadata').value;

    const response = await fetch('/mine_nft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ license_key: licenseKey, software_id: softwareId, user_id: userId, metadata: metadata ? JSON.parse(metadata) : {} })
    });

    const data = await response.json();
    const messageElement = document.getElementById('message');
    if (response.status === 201) {
        messageElement.textContent = data.message;
        messageElement.style.color = 'green';
    } else {
        messageElement.textContent = data.message;
        messageElement.style.color = 'red';
    }
}

async function getBlockchain() {
    const response = await fetch('/get_chain', { method: 'GET' });
    const data = await response.json();
    const blockchainElement = document.getElementById('blockchain');
    blockchainElement.textContent = JSON.stringify(data.chain, null, 2);
}