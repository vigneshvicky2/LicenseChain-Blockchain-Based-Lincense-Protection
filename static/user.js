async function validateLicense() {
    const licenseKey = document.getElementById('license_key').value;
    const softwareId = document.getElementById('software_id').value;
    const userId = document.getElementById('user_id').value;

    const response = await fetch('/validate_license', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ license_key: licenseKey, software_id: softwareId, user_id: userId })
    });

    const data = await response.json();
    const messageElement = document.getElementById('message');
    if (response.status === 200) {
        messageElement.textContent = data.message;
        messageElement.style.color = 'green';
    } else {
        messageElement.textContent = data.message;
        messageElement.style.color = 'red';
    }
}